import json
import os
import sys

import yaml
from pydash import defaults_deep


class CipherConfig():
    """Utilities used for managing application configuration."""

    Environment = "Development"
    """
    Specifies the environment of the server. Could be either "Development", "Staging", or "Production"

    **Config Key**: "CipherEnvironment"

    **Default Value**: "Development"
    """

    Country = "US"
    """
    Specifies the country of the server.

    **Config Key**: "CipherCountry"

    **Default Value**: "US"
    """

    DefaultSearchLocation = None
    """
    Specifies a location to include when searching for connection "server.json" configuration files, and environment "environment.json" files.

    **Config Key**: "ConfigSearchPath"

    **Default Value**: "D:\\\\apps" or "P:\\\\"
    """

    @staticmethod
    def get_DefaultSearchLocation():
        return CipherConfig.DefaultSearchLocation if CipherConfig.DefaultSearchLocation is not None else ["D:\\apps", "P:\\"]

    @staticmethod
    def load(filepath: str, checkForEnvTransforms=True, ignoreConfigSearchPathKey=False) -> dict:
        """
        Loads a YAML file and returns it as a dictionary.

        If the dictionary contains any of the config keys for the three properties of CipherConfig listed above,
        they will be set and used going forward.

        If the ``checkForEnvTransforms`` argument is True or unspecified,
        it will additionally load any current environment specific files if they exist.
        For example, if the current environment is configured as ``Development`` and filepath is ``parameters.yaml``,
        a file named ``parameters.development.yaml`` will be loaded and merged with ``parameters.yaml``.
        Values in the environment transform file will override values in the main file.
        """
        config = None
        with open(filepath, "r") as ymlfile:
            config = yaml.load(ymlfile)

        if checkForEnvTransforms:
            (root, ext) = os.path.splitext(filepath)
            path = root + "." + CipherConfig.Environment.lower() + ext
            if os.path.isfile(path):
                with open(path, "r") as ymlfile:
                    env_config = yaml.load(ymlfile)
                    config = defaults_deep({}, env_config, config)

        if not ignoreConfigSearchPathKey:
            if "ConfigSearchPath" in config:
                CipherConfig.DefaultSearchLocation = config["ConfigSearchPath"]
                CipherConfig.loadEnvironment()
            if "CipherEnvironment" in config:
                CipherConfig.Environment = config["CipherEnvironment"]
            if "CipherCountry" in config:
                CipherConfig.Country = config["CipherCountry"]

        return config

    @staticmethod
    def loadConnections(configpath="servers.json", search_location=None) -> list:
        """
        Typically only used internally by CipherData to locate and load a servers.json file and return a list of connection configurations.
        """
        if search_location is None:
            search_location = CipherConfig.get_DefaultSearchLocation()

        __location__ = CipherConfig.__searchPath(configpath, search_location)

        if __location__ is None:
            raise FileNotFoundError("Could not find servers.json in " + str(search_location))

        with open(__location__, 'r') as f:
            return json.load(f)

    @staticmethod
    def loadEnvironment(configpath="environment.json", search_location=None, ignoreEnvVars=False):
        """
        Typically only used internally by CipherConfig to locate and load an environment.json file and set the Environment and Country properties on application start.

        This method is called on the first import of the module and uses the DefaultSearchLocation property default value first.
        If the config key “ConfigSearchPath” is present in a file loaded by the CipherConfig.load method,
        this method will be called again to try to locate and load environment.json again.
        """

        os_env = os.getenv("Cipher_Environment", None) if not ignoreEnvVars else None
        os_country = os.getenv("Cipher_Country", None) if not ignoreEnvVars else None

        if os_env is None or os_country is None:
            __location__ = CipherConfig.__searchPath(configpath, search_location)

            if __location__ is None:
                return

            with open(__location__, 'r') as f:
                config = json.load(f)
                if "Environment" in config:
                    CipherConfig.Environment = config["Environment"]
                if "Country" in config:
                    CipherConfig.Country = config["Country"]

        CipherConfig.Environment = os_env if os_env is not None else CipherConfig.Environment
        CipherConfig.Country = os_country if os_country is not None else CipherConfig.Country

    @staticmethod
    def __searchPath(path, search_location):
        if os.path.isfile(path):
            __location__ = path
        else:
            if search_location is None:
                search_location = CipherConfig.get_DefaultSearchLocation()
            __location__ = None
            search_locations = list(sys.path)
            if type(search_location) is list:
                search_locations = search_location + search_locations
            else:
                search_locations.insert(1, search_location)
            for dirname in search_locations:
                candidate = os.path.join(dirname, path)
                if os.path.isfile(candidate):
                    __location__ = candidate
                    break

        return __location__


CipherConfig.loadEnvironment()
