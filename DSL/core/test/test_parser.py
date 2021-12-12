import pytest
from DSL.core.parser import Parser
from DSL.util.logger import get_core_logger

@pytest.mark.parser
class TestParser:
    logger = get_core_logger("parser_test")
    test_sentence_error = [
        'step 1b',
        'overstep',
        'stepover:as',
        'import',
        'speak:a',
        'listen: $',
        'branch: "  a"',
        'switch: ac',
        'swicth: $1+$2'
        'set: ac,ac'
        'set: $a+$a," as "'
    ]
    test_sentence_correct = [
        'listen: $12',
        'step: a',
        'step: abc # step abc',
        'stepover   ',
        'import: test.svl # test.svl',
        'speak:"  a" + $1',
        'speak:"a"',
        'branch: $b,a',
        'branch: "a "+$a, a',
        'switch: $a',
        'set: $a,"a"',
        'default: stpA'
    ]
    parser = Parser()

    def test_parse(self):
        self.logger.debug("test_correct_sentence")
        for item in self.test_sentence_correct:
            self.logger.debug(item)
            self.logger.debug(str(self.parser.parse(item)))

        self.logger.debug("test_erro_sentence")
        for item in self.test_sentence_error:
            self.logger.debug(item)
            self.logger.debug(str(self.parser.parse(item)))

        
            
    


