from _pytest.mark import param
import pytest
from DSL.core.parser import Parser
from DSL.util.logger import get_core_logger

@pytest.mark.unittest
class TestInterpreter:
    logger = get_core_logger("interpreter")
    test_sentence = [
        'step a',
        'step b',
        'step 1b'
    ]
    def test_parse_one_sentence(self):
        pass
    


