
'''
overview:
    you can define other input method here and setting in `setting.py`

rules:
    input: None
    output: achieved object 
    note: 
        1. if the output isn't string, you need to make sure there isn't any compare between string and input content in your code
        2. you need to make the input_method correspond to a string one by one in dict `listen_dict`
setting:
    you can choose your input method in `setting.py`

'''
from DSL.util import logger
from DSL.util.logger import get_user_logger


def keyboard():
    # keyboard input
    words = input() 
    return words


listen_dict = {
    "default": keyboard
}




