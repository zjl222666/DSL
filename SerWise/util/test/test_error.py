import pytest
from DSL.util.error import raise_error

@pytest.mark.error
class TestError:
    error_name = [
        'syntax error',
        'compile error',
        'running error'
    ]
    error_content = [
        'unkonwn command',
        'step name error',
        'listen error'
    ]
    trace = [
        'line 1',
        'line 2',
        'line 3'
    ]
    def test_raise_error(self):
        for e,c,t in zip(self.error_name, self.error_content, self.trace):
            raise_error(e, c, t)