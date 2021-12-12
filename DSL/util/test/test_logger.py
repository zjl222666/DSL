import pytest
from DSL.util.logger import get_core_logger,get_user_logger

@pytest.mark.logger
class TestLogger:
    def test_get_core_logger(self):
        logger1 = get_core_logger("logger_test_1")
        logger2 = get_core_logger("logger_test_2")
        logger1.info(f"{logger1 is logger2}")
        logger1.info("yes")
        logger1.debug("yes")
        logger1.error("yes")
        logger2.info("no")
        logger2.debug("no")
        logger2.error("no")
    
    def test_get_user_logger(self):
        logger1 = get_user_logger("logger_test_3")
        logger2 = get_user_logger("logger_test_4")
        logger1.info(f"{logger1 is logger2}")
        logger1.info("yes")
        logger1.debug("yes")
        logger1.error("yes")
        logger2.info("no")
        logger2.debug("no")
        logger2.error("no")