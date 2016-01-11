import os
import logging

from camellia.util import define
from camellia.util import system as s

INFO_COLOR = '\033[94m'
DEBUG_COLOR = '\033[92m'
WARNING_COLOR = '\033[93m'
ERROR_COLOR = '\033[91m'
CRITICAL_COLOR = '\033[95m'
END_COLOR = '\033[0m'

class Log(object):
    def __init__(self, name,
                 console=True,
                 format=define.BASE_FORMAT,
                 level=define.BASE_LEVEL,
                 shell=True):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.shell = shell
        if console:
            self.__addHandler(self.consoleHandler(format, level))

    def __addHandler(self, handler):
        self.logger.addHandler(handler)

    def consoleHandler(self, format, level):
        f = logging.Formatter(format)
        h = logging.StreamHandler()
        h.setLevel(level)
        h.setFormatter(f)
        return h

    def debug(self, message):
        if message != None:
            if self.shell: self.logger.debug(DEBUG_COLOR + message + END_COLOR)
            else: self.logger.debug(message)

    def warning(self, message):
        if message != None:
            if self.shell: self.logger.warning(WARNING_COLOR + message + END_COLOR)
            else: self.logger.warning(message)

    def info(self, message):
        if message != None:
            if self.shell: self.logger.info(INFO_COLOR + message + END_COLOR)
            else: self.logger.info(message)

    def critical(self, message):
        if message != None:
            if self.shell: self.logger.critical(CRITICAL_COLOR + message + END_COLOR)
            else: self.logger.critical(message)

    def error(self, message):
        if message != None:
            if self.shell: self.logger.error(ERROR_COLOR + message + END_COLOR)
            else: self.logger.error(message)

    def __del__(self):
        del self

LOG = Log(define.BASE_NAME)

if __name__ == "__main__":
    logger = LOG
    logger.debug("debug")
    logger.warning("warning")
    logger.info("info")
    logger.critical("critical")
    logger.error("error")
