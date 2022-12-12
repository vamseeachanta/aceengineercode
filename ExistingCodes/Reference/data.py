"""
This module implements commonly used data access methods.
"""

import json
import math
import os
from abc import ABC, abstractmethod
from datetime import date, datetime
from typing import Union
from urllib.parse import quote_plus

import cx_Oracle  # noqa: F401
import numpy as np
import pandas
import pyodbc  # noqa: F401
from sqlalchemy import create_engine, event
from sqlalchemy import types as sql_types
from sqlalchemy.engine import Engine, ResultProxy

from .config import CipherConfig


def _date_encoder(obj):
    if isinstance(obj, (datetime, date)):
        return (obj.isoformat() + 'Z')
    elif isinstance(obj, np.datetime64):
        return (obj.item().isoformat() + 'Z')
    else:
        return json.JSONEncoder().default(obj)


class CipherData(ABC):
    """
    Represents a configured connection to a data source, providing methods for underlying data access.

    An application does not create an instance of `CipherData` directly, but instead uses `CipherData.get(...)` or `CipherData.byConfig(...)` \
    to create an instance of a class that implements `CipherData` for the appropriate data source type.

    Additionally, a set of static convenience methods are also provided in \
    `CipherData.fromCsv`, `CipherData.toCsv`, `CipherData.readFile`, `CipherData.loadSqlFile`, `CipherData.compileSql`, `CipherData.toJson`, and `CipherData.fromJson`

    :param serverName: Server name
    :type serverName: str

    :param databaseName: Database name
    :type databaseName: str

    :param userName: User name
    :type userName: str

    :param userPassword: Password
    :type userPassword: str

    :param chunkSize: Chunk size to use for bulk inserts
    :type chunkSize: int
    """

    __engine = None
    serverName = None
    databaseName = None
    userName = None
    userPassword = None
    chunksize = 1000

    def __init__(self, serverName: str = None, databaseName: str = None, userName: str = None, userPassword: str = None, chunksize=1000):
        self.serverName = serverName
        self.databaseName = databaseName
        self.userName = userName
        self.userPassword = userPassword
        self.chunksize = chunksize
        super().__init__()

    @property
    def engine(self) -> Engine:
        """
        Returns the underlying DBMS `sqlalchemy.Engine` connection object. \
        Can be used for more direct control into the database connection connections and to manage transactions.

        For more information, refer to the sqlalchemy documentation:
        <http://docs.sqlalchemy.org/en/latest/core/connections.html>
        """
        if self.__engine is None:
            self.__engine = self._init_engine()
        return self.__engine

    @abstractmethod
    def _init_engine(self):
        pass

    @abstractmethod
    def load(self, sql_or_csvpath: str, **kwargs) -> pandas.DataFrame:
        """Loads data from the associated data source and returns as a `pandas.DataFrame`."""
        pass

    @abstractmethod
    def save(self, dataframe: pandas.DataFrame, tablename_or_filename: str, **kwargs):
        """Saves data from a 'pandas.DataFrame' back to the associated data source."""
        pass

    @staticmethod
    def get(serverType: str, serverName: str = None, databaseName: str = None, userName: str = None, userPassword: str = None, highAvailability: bool = False, chunksize=1000):
        """
        A convenience static method to directly construct the appropriate type of `CipherData` object using the special `serverType` parameter \
        with value of either "MSSQL", "ORACLE", or "CSV". All other parameters are passed on to the underlying constructor.
        """
        if serverType.upper() == "MSSQL":
            return CipherMsSqlData(serverName, databaseName, userName, userPassword, highAvailability, chunksize)
        elif serverType.upper() == "ORACLE":
            return CipherOracleData(serverName, userName, userPassword, chunksize)
        elif serverType.upper() == "CSV":
            return CipherCsvData(chunksize)

    __servers = {}

    @staticmethod
    def byConfig(sourcename: str, username: str, env: str=None, country: str=None, config: Union[list, dict]=None, configfilename="servers.json", search_location: str=None):
        """
        Searches for and returns a connection configuration from a list of connection configuration dictionaries using provided parameters.

        Each connection configuration provides the following key-values: \
        ["DBSource", "UserName", "Environment", "Country", "DBServerName", "DBName", "SQLType", "Password"], \
        and is located by the matching the [`sourcename`, `username`, `env`, and `country`] parameters against the four keys of the configuration: \
        ["DBSource", "UserName", "Environment", "Country"]

        If `env` or `country` are not specified, `CipherConfig.Environment` and `CipherConfig.Country` are used, respectively.

        If `config` is a `list`, it will be treated as an already loaded array of configurations.
        If `config` is a `dict`, it will look for config search parameters in the dictionary, or else treat it as the specific config to use.

        If `config` is `None`, a configuration file will be located using the `configfilename` and `search_location` parameters. \
        A valid configuration file is a JSON file containing an array of configuration objects.

        :param sourcename: Search for a configuration with {"DBSource": sourcename}
        :type sourcename: str

        :param username: Search for a configuration with {"UserName": username}
        :type username: str

        :param env: Search for a configuration with {"Environment": env}
        :type env: str

        :param country: Search for a configuration with {"Country": country}
        :type country: str

        :param config: Specifies how to find the configuration.
        :type config: list|dict|None

        :param configfilename: the file name to search for configuration (ignored if `config` is not None)
        :type configfilename: str

        :param search_location: a folder path to include in the configuration search (ignored if `config` is not None)
        :type search_location: str

        :return: a configured CipherData instance
        """
        server = None
        # if config is of type list use it directly, otherwise:
        if type(config) is not list:
            # if config is a dictionary check if it specifies where to load config from, otherwise treat it as a single connection config entry
            if type(config) is dict:
                if "ConnectionConfigFileName" not in config and "ConfigSearchPath" not in config and "DBSource" in config:
                    server = config
                else:
                    configfilename = configfilename if "ConnectionConfigFileName" not in config else config["ConnectionConfigFileName"]
                    search_location = search_location if "ConfigSearchPath" not in config else config["ConfigSearchPath"]
                    cache_key = search_location + configfilename
                    config = CipherData.__servers.get(cache_key)
                    # if the config search path parameters were not passed in, use the dict as the config
                    if config is None:
                        config = CipherData.__servers[cache_key] = CipherConfig.loadConnections(configpath=configfilename, search_location=search_location)
            # if config_or_path is a str or None, treat it as a search location path
            elif search_location is None or type(search_location) is str:
                cache_key = search_location + configfilename if search_location is not None else configfilename
                if cache_key is None:
                    cache_key = ""
                # check to see if the configuration is already cached
                config = CipherData.__servers.get(cache_key)
                if config is None:
                    config = CipherData.__servers[cache_key] = CipherConfig.loadConnections(configpath=configfilename, search_location=search_location)

        # server will be not None if config was passed as a single connection config entry, otherwise:
        if server is None:
            if env is None:
                env = CipherConfig.Environment

            if country is None:
                country = CipherConfig.Country

            server = next((c for c in config if c["DBSource"] == sourcename and c["UserName"] == username and c["Environment"] == env and c["Country"] == country), None)

            if server is None:
                raise LookupError("Could not find connection configuration using DBSource: %s, UserName: %s, Environment: %s, Country: %s." % (sourcename, username, env, country))

        highAvailability = ("HighAvailability" in server and server["HighAvailability"])
        return CipherData.get(server["SQLType"], server["DBServerName"], server["DBName"], server["UserName"], server["Password"], highAvailability)

    @staticmethod
    def fromCsv(path: str, **kwargs) -> pandas.DataFrame:
        """
        A convenience shortcut method to load a CSV and get back a DataFrame in one step.

        Refer to `CipherData.load` for more information on the `**kwargs` parameter.
        """
        csv = CipherCsvData()
        return csv.load(path, **kwargs)

    @staticmethod
    def toCsv(path: str, dataframe: pandas.DataFrame, **kwargs):
        """
        A convenience shortcut method to save a DataFrame to a CSV file path in one step.

        Refer to `CipherData.save` for more information on the `**kwargs` parameter.
        """
        csv = CipherCsvData()
        csv.save(dataframe, path, **kwargs)

    @staticmethod
    def readFile(path: str) -> str:
        """
        A convenience shortcut method to read a file and return it as a string.
        """
        with open(path, 'r') as text_f:
            return text_f.read()

    @staticmethod
    def loadSqlFile(path: str, params: dict = None, **kwargs) -> str:
        """
        A convenience shortcut method to read a file containing a SQL query and return it as a string.

        Named parameters in the file of the format {ParameterKey} are replaced with corresponding values from the \
        `params` dictionary parameter if they are found.
        """
        sql = CipherData.readFile(path)
        return CipherData.compileSql(sql, params, **kwargs)

    @staticmethod
    def compileSql(sql: str, params: dict = None, **kwargs) -> str:
        """
        A convenience shortcut method to replace named parameters in a string of the format {ParameterKey} \
        to be replaced with corresponding values from the `params` dictionary parameter if they are found.
        """
        if params is None:
            params = kwargs
        return sql.format(**params)

    @staticmethod
    def toJson(data: Union[pandas.DataFrame, dict],
               rowindex=None,
               double_precision=10,
               default_handler=_date_encoder,
               orient='records',
               date_format='epoch',
               skipkeys=True,
               ensure_ascii=False,
               check_circular=True,
               allow_nan=True,
               indent=None,
               separators=(',', ':'),
               sort_keys=False) -> str:
        """
        Serializes a dictionary or a DataFrame into a JSON string representation.

        For a dictionary, refer here for extra optional parameters to control how the JSON is serialized:
        <https://docs.python.org/3/library/json.html>

        For a DataFrame, refer here for extra optional parameters to control how the JSON is serialized:
        <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html>
        """
        if type(data) is dict:
            # https://docs.python.org/2/library/json.html
            return json.dumps(data, default=default_handler, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, indent=indent, separators=separators, sort_keys=sort_keys)
        else:
            # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html
            return data.to_json(orient=orient, date_format=date_format, double_precision=double_precision, default_handler=default_handler)

    @staticmethod
    def fromJson(json_str: str, orient="records", toDict=False, **kwargs) -> Union[pandas.DataFrame, dict]:
        """
        Deserializes a JSON string into either a DataFrame or a dictionary.

        For a dictionary, refer here for extra optional parameters to control how the JSON is deserialized:
        <https://docs.python.org/3/library/json.html>

        For a DataFrame, refer here for extra optional parameters to control how the JSON is deserialized:
        <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_json.html>
        """
        if(toDict):
            return json.loads(json_str, **kwargs)
        else:
            return pandas.read_json(json_str, orient=orient, **kwargs)


class CipherDbData(CipherData):
    """An intermediate base class used to abstract data access methods between various DBMS system."""
    def __init__(self, serverName: str = None, databaseName: str = None, userName: str = None, userPassword: str = None, chunksize=1000):
        super().__init__(serverName, databaseName, userName, userPassword, chunksize)

    def load(self, sql: str, **kwargs) -> pandas.DataFrame:
        """
        Executes a SQL statement against the DBMS and returns a pandas.DataFrame.

        `**kwargs` can supply additional parameters to the underlying engine:
        <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sql.html>
        """
        return pandas.read_sql(sql, self.engine, **kwargs)

    def save(self, dataframe: pandas.DataFrame, tablename: str, **kwargs):
        """
        Bulk inserts all the rows of the `pandas.DataFrame` into the specified table. \
        If the table does not already exist, it will be created automatically based on the schema of the DataFrame.

        Behaviors can be overridden using `**kwargs` as documented here:
        <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html>

        Especially note the documented `if_exists`, index, and `dtype` parameters.
        """
        if_exists = 'append' if 'if_exists' not in kwargs else kwargs.pop('if_exists')
        if dataframe.shape[0] > self.chunksize:
            chunk_count = int(math.ceil(dataframe.shape[0] / self.chunksize))
            dataframes = np.array_split(dataframe, chunk_count)
            self.df_to_sql(dataframes[0], tablename, if_exists=if_exists, **kwargs)
            for df in dataframes[1:]:
                self.df_to_sql(df, tablename, if_exists='append', **kwargs)
        else:
            self.df_to_sql(dataframe, tablename, if_exists=if_exists, chunksize=self.chunksize, **kwargs)

    def df_to_sql(self, dataframe: pandas.DataFrame, tablename: str, if_exists='append', **kwargs):
        index = False if 'index' not in kwargs else kwargs.pop('index')
        dataframe.to_sql(tablename, self.engine, if_exists=if_exists, index=index, **kwargs)

    def executeSql(self, sql: str, *multiparams, **params) -> ResultProxy:
        """
        Executes a SQL statement directly and returns a `sqlalchemy.ResultProxy`. \
        Allows for named parameters in the format ":param_name or ?".

        For more information, refer to the sqlalchemy documentation:
        <https://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.Connection.execute>
        <http://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.ResultProxy>
        """
        return self.engine.execute(sql, *multiparams, **params)

    def executeSqlFile(self, sqlpath: str, *multiparams, **params) -> ResultProxy:
        """
        Loads and executes a SQL statement from a text file and and returns a `sqlalchemy.ResultProxy`. \
        Allows for named parameters in the format ":param_name or ?".

        For more information, refer to the sqlalchemy documentation:
        <https://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.Connection.execute>
        <http://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.ResultProxy>
        """
        with open(sqlpath, "r") as sql_f:
            sql = sql_f.read()
        return self.executeSql(sql, *multiparams, **params)

    def executeScalar(self, sql: str, *multiparams, **params):
        """
        Executes a SQL statement directly and returns the single scalar value result. \
        Allows for named parameters in the format ":param_name or ?".
        """
        return self.engine.scalar(sql, *multiparams, **params)

    def executeNonQuery(self, sql: str, *multiparams, **params) -> int:
        """
        Executes a SQL statement directly and returns the number of rows affected. \
        Allows for named parameters in the format ":param_name or ?".

        For more information, refer to the sqlalchemy documentation:
        <https://docs.sqlalchemy.org/en/latest/core/connections.html?highlight=scalar#sqlalchemy.engine.ResultProxy.rowcount>
        <https://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.Connection.execute>
        """
        results = self.executeSql(sql, *multiparams, **params)
        return results.rowcount


class CipherMsSqlData(CipherDbData):
    """An implementation of `CipherData` and `CipherDbData` which wraps the MSSQL ODBC engine."""

    def __init__(self, serverName: str = None, databaseName: str = None, userName: str = None, userPassword: str = None, highAvailability: bool = False, chunksize=1000):
        super().__init__(serverName, databaseName, userName, userPassword, chunksize)
        self.highAvailability = highAvailability

    def _init_engine(self):
        connection_string = "Driver={ODBC Driver 13 for SQL Server};Server=" + self.serverName + ";Database=" + self.databaseName + ";Uid=" + self.userName + ";Pwd=" + self.userPassword + ";"
        if self.highAvailability:
            connection_string = connection_string + "MultiSubnetFailover=Yes;"
        connection_string = "mssql+pyodbc:///?odbc_connect=" + quote_plus(connection_string)
        engine = create_engine(connection_string, encoding='utf-8', echo=False)

        @event.listens_for(engine, 'before_cursor_execute')
        def receive_before_cursor_execute(conn, cursor, statement, params, context, executemany):
            if executemany:
                # performance hack to force underlying pyodbc engine to use fast_executemany method
                cursor.fast_executemany = True

        return engine


class CipherOracleData(CipherDbData):
    """An implementation of `CipherData` and `CipherDbData` which wraps the cx_Oracle engine."""

    def __init__(self, serverName: str = None, userName: str = None, userPassword: str = None, chunksize=1000):
        super().__init__(serverName, None, userName, userPassword, chunksize)

    def _init_engine(self):
        os.environ["NLS_LANG"] = "AMERICAN_AMERICA.WE8MSWIN1252"
        connection_string = "oracle+cx_oracle://" + self.userName + ":" + self.userPassword + "@" + self.serverName
        engine = create_engine(connection_string, encoding='utf-8', coerce_to_unicode=False, echo=False)
        return engine

    def df_to_sql(self, dataframe: pandas.DataFrame, tablename: str, if_exists='append', **kwargs):
        # performance hack to handle 'object' columns as VARCHAR instead of CLOB
        dtype = {c: sql_types.VARCHAR(dataframe[c].str.len().max()) for c in dataframe.columns[dataframe.dtypes == 'object'].tolist()}
        dataframe.to_sql(tablename, self.engine, dtype=dtype, if_exists=if_exists, index=False, **kwargs)


class CipherCsvData(CipherData):
    """An implementation of `CipherData` which provides load and save methods for CSV files."""

    def __init__(self, chunksize=1000):
        super().__init__(chunksize=chunksize)

    def _init_engine(self):
        return None

    def load(self, csvpath: str, **kwargs) -> pandas.DataFrame:
        """
        Loads a CSV file and returns a `pandas.DataFrame`.

        `**kwargs` can supply additional parameters to the underlying engine:
        <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html>
        """
        return pandas.read_csv(csvpath, **kwargs)

    def save(self, dataframe: pandas.DataFrame, filename: str, truncate=False, **kwargs):
        """
        Bulk inserts all the rows of the DataFrame into a CSV file.

        Behaviors can be overridden using `**kwargs` as documented here:
        <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html>

        Especially note the documented `index` parameter.
        """
        dataframe.to_csv(filename, index=False, **kwargs)


class DataFrameBuilder():
    """
    A utility to build up a new `pandas.DataFrame` by providing one dictionary at a time to the `.append` method.
    """

    def __init__(self, columns=[]):
        self._columns = set(columns)
        self._rows = dict()
        self._count = 0
        for col in self._columns:
            self._rows[col] = []

    def append(self, row: dict):
        """
        Adds a dictionary representing a row of data to the builder.

        Any previously unseen columns will be automatically added to the resulting `pandas.DataFrame`.
        """
        if row is None:
            return

        for col in row.keys():
            if col not in self._columns:
                self._columns.add(col)
                self._rows[col] = [None for i in range(0, self._count)]

        for col in self._columns:
            val = row.get(col)
            self._rows[col].append(val)

        self._count = self._count + 1

    def to_dataframe(self):
        """Generates a `pandas.DataFrame` instance."""
        return pandas.DataFrame.from_dict(self._rows)


class AttributeDict(dict):
    """A dictionary object with attributes support."""
    def __init__(self, *args, **kwargs):
        self.__dict__ = self
        dict.__init__(self, *args, **kwargs)
