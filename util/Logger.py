import inspect
import logging
import logging.config
import os

path = os.getcwd()

path = path+"\\resources\config\Logger.conf"


def getlogger():
    try:
        logging.config.fileConfig(fname=path, disable_existing_loggers=False)
        calling_function = inspect.stack()[1][3]
        logger = logging.getLogger(calling_function)
        return logger
    except Exception as e:
        print("Exception Occurred", e)
