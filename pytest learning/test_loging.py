import logging


def test_loggingdemo():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("A warning statement is executed")
    logger.error("An error statement is executed")
    logger.critical("Critical issue")
