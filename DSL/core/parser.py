from DSL.util.error import raise_error
import re
from DSL.core.rules import *

class Parser:
    '''
    overview:
        提供语句预处理功能，包括
            - 词法分析
            - 语法分析
            - 错误处理
            - 语句规范化输出
    '''
    def parse(self, sentence: str):
        # pretreatment
        if comment_char in sentence:
            sentence = sentence[:sentence.find('#')]        

        if change_to_lower:
            sentence = sentence.lower()

        for c in need_to_replace:
            sentence = sentence.replace(c, '')
        
        





        




