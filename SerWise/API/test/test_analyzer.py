import pytest
from DSL.API.analyzer import Analyzer_dict
from DSL.util.logger import get_core_logger


@pytest.mark.analyzer
def test_analyzer():
    logger = get_core_logger("analyzer_test")
    test = [
        ('12','12'),
        ('5', '00000', 'len'),
        ('合法姓名', 'zjl'),
        ('合法姓名', '郑金亮')
    ]
    for analyzer in Analyzer_dict.values():
        for t in test:
            kwarg = t[2:]
            result = analyzer(t[0], t[1], kwarg)
            logger.info(f"{t} : {result}")
                
