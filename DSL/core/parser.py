import re
from DSL.core.rules import Parameters_patern, Parameter_split, command_split, command, comment_char, change_to_lower
from DSL.util.logger import get_core_logger


class Parser:
    '''
    overview:
       Provides parsing functions, including
        - Lexical analysis
        - Statement normalized return
    '''
    
    def parse(self, sentence: str):
        # pretreatment
        if comment_char in sentence:
            sentence = sentence[:sentence.find(comment_char)]        
        if change_to_lower:
            sentence = sentence.lower()

        # splite the command and parameters
        cur_parameter = []
        if command_split in sentence:  
            cur_command = sentence[:sentence.find(command_split)].strip()
            tmp = ""
            state = 0
            for c in sentence[sentence.find(command_split)+1:]:
                if state == 1:
                    tmp += c
                    if c == '"':
                        state = 0
                else:
                    if c == Parameter_split:
                        cur_parameter.append(tmp)
                        tmp = ""
                    else:
                        tmp += c
                        if c == '"':
                            state = 1
            cur_parameter.append(tmp)
        else:
            cur_command = sentence.strip()
            
        
        # match with command
        if not cur_command in command.keys():
            return "unkown_command"
        
        # extract the parameters and match it with command
        cur_parameter = list(map(lambda x: x.strip(), cur_parameter))
        paramter_pattern = command[cur_command]
        if len(paramter_pattern) > 0 and paramter_pattern[-1] == 'kwarg':
            if len(cur_parameter) >= len(paramter_pattern):
                kwarg = cur_parameter[len(paramter_pattern) - 1:]
                cur_parameter = cur_parameter[:len(paramter_pattern) - 1]
            else:
                kwarg = []
            cur_parameter.append(kwarg)
        
        if not len(cur_parameter) == len(paramter_pattern):
            return "parameters number error"

        for p, pattern in zip(cur_parameter,paramter_pattern):
            if pattern == 'kwarg': continue
            if not re.match(Parameters_patern[pattern], p):
                return "parameters type error" 
        
        return cur_command, cur_parameter




                
