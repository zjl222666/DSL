from DSL.util.logger import get_core_logger, get_user_logger
from DSL.API.output import speak_dict
from DSL.API.input import listen_dict
from DSL.setting import listen_method, speak_method
from DSL.core.parser import Parser
from DSL.util.error import raise_error
from DSL.API.analyzer import Analyzer_dict


class runnerDFA:
    pass

class Interpreter:
    '''
    overview:
        解释器
    '''
    core_logger = get_core_logger("interpreter_test")
    def __init__(self) -> None:
        self.var_cache = {}
        self.step_cache = {"":[]}
        self.cur_switch = []

        self.is_switch = 0 
        '''
        note whether the running codes is in switch block
        if not : 0
        in but haven't go into any branch: 1
        in and go into a branch: 2        
        ''' 
        
        self.parser = Parser()
    
    # a hyper function to calculate the expression of string
    def calculate_expr(self, expr: str, trace):
        try:
            result = ""
            expr = expr.split('+')
            expr = list(map(lambda x: x.strip(), expr))
            self.core_logger.info(f"{expr}")
            
            for e in expr: 
                if e[0] == '"':
                    result += e[1:-1]
                else:
                    result += self.var_cache[e]
            return result
        except:
            raise_error("running error: ", "expression calculate failed", trace)
            raise RuntimeError
    
    def fun_switch(self, parameters, trace):
        try:
            self.swicth_var = parameters[0]
            return True
        except:
            raise_error("running error: ", "switch setting failed", trace)      
            return False
    
    def fun_speak(self, parameters, trace):
        try:
            speak_words = self.calculate_expr(parameters[0])
            if not speak_dict[speak_method](speak_words):
                raise_error("running error: ", "switch setting failed", trace)  
                return False
            logger = get_user_logger("conversation")
            logger.info("server: {}".format(speak_words))
            return True
        except:
            raise_error("running error: ", "speak failed", trace)
            return False
    
    def fun_branch(self, parameters, trace):
        try:
            if self.cur_switch == None:
               raise_error("running error: ", "expression calculate failed", trace)
               return False
            cur_str = self.var_cache[self.cur_switch]
            target_str = self.calculate_expr(parameters[0], trace)
            target_step = parameters[1]
            if target_str in Analyzer_dict:
                flag = Analyzer_dict[target_str](cur_str)
            else:
                flag = target_str == cur_str
            if not target_step in self.step_cache:
                raise_error("running error: ", "expression calculate failed", trace)
                return False
            
            if flag: 
                self.run(self.step_cache[target_step], trace)
            return True
        except:
            raise_error("running error: ", "branch command execute failed", trace)
            return False

    def fun_listen(self, parameters, trace):
        try:
            key = parameters[0]
            words =  listen_dict[listen_method]
            self.var_cache[key] = words
            logger = get_user_logger("conversation")
            logger.info("User: {}".format(words))
            return True
        except:
            raise_error('running error: ', 'listen command failed', trace)
            return False

    def fun_set(self, parameters, trace):
        try:
            key =  parameters[0]
            expr = self.calculate_expr(parameters[1], trace)
            self.var_cache[key] = expr
            return True
        except:
            raise_error('running error: ', 'set command failed', trace)
            return False

    
    def fun_import(self, parameters, trace):
        try:
            file_path = parameters[0]
            f = open(file_path)
            codes = f.readlines()
            self.interpret(codes, file_path, trace)
            f.close()
            return True
        except:
            raise_error('running error: ',"import file failed, please check the path", trace)
            return False

    def run(self, commands, trace):
        command_fun = {
            'speak': self.fun_speak,
            'listen': self.fun_listen,
            'import': self.fun_import,
            'branch': self.fun_branch,
            'switch': self.fun_switch,
            'set': self.fun_set,
        }

        if not trace == "": trace += '\n'
        for command in commands:
            if not command_fun[command['command']](command['parameters'], trace + command['trace']):
                return

    def interpret(self, codes : list, file: str, trace: str):
        
        cur_step = ""
        # scan the codes and push them into step_dict
        for line, sentence in enumerate(codes):
            if not trace == "": trace = trace + '\n'
            trace = trace + f'({file})line{line} :{sentence}'

            # skip the blank line
            if len(sentence.split()) < 1: continue

            parse_result = self.parser.parse(sentence)
            if isinstance(parse_result, str):
                raise_error("sytnax error: ", parse_result, trace)
                return
            
            # process the 'step' command
            if parse_result[0] == 'step':
                if not cur_step == "":
                    raise_error("compile error", "Nested step declarations are not allowed",  trace)
                    return
                cur_step = parse_result[1][0]
                self.step_cache[cur_step] = []
            # process the 'stepover' command
            elif parse_result[0] == 'stepover':
                if cur_step == "":
                    raise_error("compile error", "Step and Stepover do not match", trace)
                    return
                cur_step = ""
            # store the other command to the Corresponding cache
            else:
                self.step_cache[cur_step].append({'command': parse_result[0], 
                                                'parameters': parse_result[1],
                                                'trace': trace})
        

    
            