
'''
overview:
    you can define other out method here

rules:
    input: object will be output
    output: None
    note: 
        1. you need to make the output_method correspond to a string one by one in dict `speak_dict`
setting:
    you can choose your output method in `setting.py`

'''
from SerWise.util.logger import get_core_logger

logger = get_core_logger('speak_test')
def console(s, kwarg):
    logger.debug(s)
    return True

speak_dict = {
    "default":  console
}



