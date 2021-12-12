import pytest
from DSL.API.input import listen_dict

@pytest.mark.listen
def test_listen():
    for listen in listen_dict.values():
        print(listen(['5']))
    print(listen_dict['clock'](['4']))


if __name__ == '__main__':
    test_listen()