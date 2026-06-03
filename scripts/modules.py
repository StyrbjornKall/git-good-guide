from my_cool_package.logger.setup_logger import setup_logger
from my_cool_package.utils.test_module import test_logger

if __name__ == "__main__":
    logger = setup_logger()
    logger.info("This is a log message from the modules script.")

    test_logger()
