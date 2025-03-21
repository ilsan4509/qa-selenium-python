import logging

def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) #filehandler object

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happend")
    logger.critical("Critical issue")

