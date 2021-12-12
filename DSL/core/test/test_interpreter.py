from DSL.core.interpreter import Interpreter
from DSL.util.logger import get_core_logger
import pytest


@pytest.mark.interpreter
class TestInterpreter:
    i = Interpreter()
    def test_calculate_expr(self):
        expr = [
            '$a + " 1 2"',
            '"12" + "12"',
            '"1221" + ds',
            '$a + $b',
            '$ + "1 21"'
        ]
        self.i.var_cache["$a"] = "$a"
        for e in expr:
            try:
                r = self.i.calculate_expr(e, "")
                self.i.core_logger.debug(f"{e}:")
                self.i.core_logger.debug(f"{r}")
            except:
                self.i.core_logger.debug("failed")

    def test_interprete(self):
        pass