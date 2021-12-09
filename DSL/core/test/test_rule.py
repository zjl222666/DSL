import pytest
from DSL.util.logger import get_core_logger
from DSL.core.rules import variables

@pytest.mark.unittest
class testRules:
    def test_variables():
        vars = [
            f'"string_constant"',
            f'$var',
            f'$var + "string_constant" + $22'
        ]
        error_vars = [
            f'"error_string'
            f'""'
        ]