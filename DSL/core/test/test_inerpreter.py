import pytest
from DSL.core.interpreter import Interpreter
from DSL.util.logger import get_core_logger

@pytest.mark.unittest
class TestInterpreter:
    logger = get_core_logger()
    test_sentence = [
        'step a',
        'step b',
        'step 1b'
    ]
    def test_parse_one_sentence(self):
        interpreter = Interpreter()
        self.logger.debug("start test (parse_one_sentence)")
        for s in self.test_sentence:
            result = interpreter.parse_one_sentence(s)
            self.logger.debug("{} : {}".format(s, result))
    
    

