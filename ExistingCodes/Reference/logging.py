import logging
import socket
import sys
from datetime import datetime
from logging import FileHandler
from pathlib import Path

import pandas as pd
from ciphercommon.data import CipherData


class CipherLog():
    """A wrapper around a default instance of a python logger, providing sensible default and configurable handlers.."""

    @staticmethod
    def configure(config: dict = {}, logname=__name__):
        """
        Configures the default instance of the `Logger`
        """
        Logger.get(logname).configure(config)

    @staticmethod
    def get(logname=__name__):
        return Logger.get(logname)

    @staticmethod
    def log(lvl: int, msg: str, *args: tuple, **kwargs: dict):
        """
        Log 'msg % args' with the integer severity 'level'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.log(level, "We have a %s", "mysterious problem", exc_info=1)
        """
        CipherLog.get().log(lvl, msg, *args, **kwargs)

    @staticmethod
    def debug(msg, *args: tuple, **kwargs: dict):
        """
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        CipherLog.get().debug(msg, *args, **kwargs)

    @staticmethod
    def info(msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """
        CipherLog.get().info(msg, *args, **kwargs)

    @staticmethod
    def warn(msg, *args, **kwargs):
        CipherLog.get().warning(msg, *args, **kwargs)

    @staticmethod
    def warning(msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)
        """
        CipherLog.get().warning(msg, *args, **kwargs)

    @staticmethod
    def error(msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info=1)
        """
        CipherLog.get().error(msg, *args, **kwargs)

    @staticmethod
    def critical(msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.critical("Houston, we have a %s", "major disaster", exc_info=1)
        """
        CipherLog.get().critical(msg, *args, **kwargs)


logcache = {}


class Logger():
    """A wrapper around the python `logger` object, providing sensible default and configurable handlers."""

    @staticmethod
    def get(logname: str):
        if logname not in logcache:
            logcache[logname] = Logger(logname)
        return logcache[logname]

    def __init__(self, logname: str, config: dict = None):
        self.logname = logname
        if logname not in logcache:
            logcache[logname] = self
        self.__logger = logging.getLogger(logname)
        if config is not None:
            self.configure(config)

    def getLogFilename(self):
        logger = self.__logger
        if not hasattr(logger, "filename"):
            return None
        return logger.filename

    def configure(self, config: dict = {}):
        self.clearHandlers()
        logger = self.__logger
        logger.setLevel(1)

        if "Logging" not in config:
            self.addConsoleLog(logging.DEBUG)
            return

        settings = config["Logging"]

        if "Console" in settings:
            if "Enabled" not in settings["Console"] or settings["Console"]["Enabled"]:
                lvl = logging.INFO if "Level" not in settings["Console"] else getattr(logging, str.upper(settings["Console"]["Level"]))
                self.addConsoleLog(lvl)

        if "File" in settings:
            if "Enabled" not in settings["File"] or settings["File"]["Enabled"]:
                lvl = logging.INFO if "Level" not in settings["File"] else getattr(logging, str.upper(settings["File"]["Level"]))
                path = Path(".\Logs" if "Path" not in settings["File"] else settings["File"]["Path"])

                filemask = "{logdate}.log" if "FileMask" not in settings["File"] else settings["File"]["FileMask"]
                filedatemask = "%Y%m%d_%H%M" if "FileDateMask" not in settings["File"] else settings["File"]["FileDateMask"]
                filedate = datetime.now().strftime(filedatemask)
                filename = Path(filemask.format(logdate=filedate))

                if not path.is_absolute() and not path.exists():
                    path.mkdir(parents=True, exist_ok=True)

                fullpath = Path(path, filename)

                self.addFileLog(str(fullpath), lvl)
                logger = self.__logger
                logger.filename = str(filename)

    def addHandler(self, handler: logging.Handler):
        """Add the specified handler to this logger."""
        self.__logger.addHandler(handler)

    def removeHandler(self, handler: logging.Handler):
        """Remove the specified handler from this logger."""
        self.__logger.removeHandler(handler)

    def clearHandlers(self):
        """Clears all handlers from this logger."""
        logger = self.__logger
        if (logger.hasHandlers()):
            logger.handlers.clear()
        return logger

    def addConsoleLog(self, lvl=logging.INFO, fmt='%(asctime)s - %(levelname)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S"):
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(lvl)
        formatter = logging.Formatter(fmt, datefmt)
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)

    def addFileLog(self, path, lvl=logging.INFO, fmt='%(asctime)s - %(levelname)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S", **kwargs):
        handler = FileHandler(path, **kwargs)
        handler.setLevel(lvl)
        formatter = logging.Formatter(fmt, datefmt)
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)

    def log(self, lvl: int, msg: str, *args: tuple, **kwargs: dict):
        """
        Log 'msg % args' with the integer severity 'level'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.log(level, "We have a %s", "mysterious problem", exc_info=1)
        """
        self.__logger.log(lvl, msg, *args, **kwargs)

    def debug(self, msg, *args: tuple, **kwargs: dict):
        """
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        self.__logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """
        self.__logger.info(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        self.__logger.warning(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)
        """
        self.__logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info=1)
        """
        self.__logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.critical("Houston, we have a %s", "major disaster", exc_info=1)
        """
        self.__logger.critical(msg, *args, **kwargs)


CipherLog.configure()


class ExecutionSummaryLog():
    def __init__(self, appname: str, execution_id: str, logToDb: CipherData = None, logTableName="ExecutionSummary", logger=CipherLog.get()):
        self.appname = appname
        self.execution_id = execution_id
        self.hostname = socket.gethostname()
        self.starttime = datetime.utcnow()
        self.recordsAffected = 0
        self.runstatus = "Good"
        self.logToDb = logToDb
        self.logTableName = logTableName
        self.logger = logger

    def addRecordsAffected(self, count=1):
        self.recordsAffected = self.recordsAffected + count

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        endtime = datetime.utcnow()
        runtime = endtime - self.starttime
        self.logger.info("Total running time is %s, and %s records were affected.", runtime, self.recordsAffected)
        if self.logToDb is not None:
            self.save(endtime=endtime)

    def toDataFrame(self, endtime=None):
        if endtime is None:
            endtime = datetime.utcnow()
        return pd.DataFrame.from_dict([{
            "ExecutionId": self.execution_id,
            "ApplicationName": self.appname,
            "ServerName": self.hostname,
            "StartTime": self.starttime,
            "EndTime": endtime,
            "RecordsAffected": self.recordsAffected,
            "RunStatus": self.runstatus
        }])

    def save(self, logToDb: CipherData = None, logTableName: str = None, endtime=None):
        if logToDb is None:
            logToDb = self.logToDb
        if logTableName is None:
            logTableName = self.logTableName
        logToDb.save(self.toDataFrame(endtime), logTableName)
