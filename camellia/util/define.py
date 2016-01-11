import os
import logging

APP_UTIL = os.path.normpath(os.path.dirname(__file__))
APP_ROOT = os.path.normpath(os.path.dirname(APP_UTIL))
APP_LIB = os.path.normpath(os.path.join(APP_ROOT, "lib"))

BASE_NAME = "Camellia"
BASE_LEVEL = logging.DEBUG
BASE_FORMAT = '%(processName)s.%(name)s ( PID %(process)d ) : %(asctime)s - %(levelname)s - %(message)s'
