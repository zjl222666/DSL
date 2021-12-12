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
        sentence = sentence.split(command_split)
        sentence = list(map(lambda x: x.strip(), sentence))

        # match with command
        cur_command = None
        for pattern in command.keys():
            if sentence[0] == pattern:
                cur_command = pattern
                break
        if cur_command == None:
            return "unkown_command"
        
        # extract the parameters and match it with command
        if len(sentence) > 1:
            cur_parameter = sentence[1].split(Parameter_split)
        else:
            cur_parameter = []

        cur_parameter = list(map(lambda x: x.strip(), cur_parameter))
        paramter_pattern = command[cur_command]
        if not len(cur_parameter) == len(paramter_pattern):
            return "parameters number error"

        for p, pattern in zip(cur_parameter,paramter_pattern):
            if not re.match(Parameters_patern[pattern], p):
                return "parameters type error" 
        
        return cur_command, cur_parameter




                


                


        


        
        
        





        




