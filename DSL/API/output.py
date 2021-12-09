
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
from DSL.util.logger import get_user_logger

def console(s):
    return s

speak_dict = {
    "default":  console
}

def speak(s):
    words = console(s)
    logger = get_user_logger("conversation")
    logger.info("server: {}".format(words))
