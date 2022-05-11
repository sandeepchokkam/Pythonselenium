import inspect
import logging


class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('filelog.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
        # logger.debug("A debug statement is executed")
        # logger.info("Information statement")
        # logger.warning("A warning statement is executed")
        # logger.error("An error statement is executed")
        # logger.critical("Critical issue")
        return logger
