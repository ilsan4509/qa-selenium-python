import inspect
import logging


class BaseClass:
    def get_logger(self):
        # logger = logging.getLogger(__name__)

        logger_name = inspect.stack()[1][3] # instead of __name__
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
