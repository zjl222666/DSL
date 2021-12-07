import logging
import re

class Standardization:
    '''
    overview:
        提供语句预处理功能，包括
            - 词法分析
            - 语法分析
            - 错误处理
            - 语句规范化输出
    '''
    key_word = ['step', 'stepover', 'goto', 'speak', 'set', 'listen', 'execute']


    def __init__(self) -> None:
        pass
        
        
    def parse(self, sentence):
        pass


class Interpreter:
    '''
    overview:
        解释器
    '''
    RE = {
        r'step\b[^0-9][a-z]+': 'creat_branch'
    }

    def __init__(self) -> None:
        pass

    def parse_one_sentence(self, s):
        for pattern, action in self.RE.items():
            if re.match(pattern, s):
                return action
        




