from SerWise.util.logger import get_core_logger, get_user_logger
from SerWise.API.output import speak_dict
from SerWise.API.input import listen_dict
from SerWise.setting import listen_method, speak_method, analyzer_chosen
from SerWise.core.parser import Parser
from SerWise.util.error import raise_error, raise_warning
from SerWise.API.analyzer import Analyzer_dict


class Interpreter:
    '''
    overview:
        interpreter of serWise, it will interpret and execute each serwise statement that has been parsed
    '''
    core_logger = get_core_logger("interpreter_test")
    def __init__(self, id) -> None:
        self.id = id
        self.var_cache = {}
        self.step_cache = {}
        '''
        a dict to store the step
            - key: step name
            - value: command list
                - command<dict>:
                    -'command': command name
                    -'parameters': parameters for command
                    -'trace': the command running trace
        '''

        self.cur_switch = []
        '''
        a stack for labeling whether the running codes is in switch block and record the switch expr
        if not : (0,None)
        in but haven't go into any branch: (1,z)
        in and go into a branch: (2,z)        
        ''' 

        self.parser = Parser()
    
    def add_var(self, key, val):
        '''
        Prepare for user information initialization
        '''
        self.var_cache[key] = val

     
    def calculate_expr(self, expr: str, trace):
        '''
        a hyper function to calculate the expression of string
        '''
        try:
            result = ""
            expr = expr.split('+')
            expr = list(map(lambda x: x.strip(), expr))
            self.core_logger.debug(f"calculate:  {expr}")
            
            for e in expr: 
                if e[0] == '"':
                    result += e[1:-1]
                else:
                    result += str(self.var_cache[e])
            return result
        except:
            raise_error("running error: ", "expression calculate failed", trace)
            raise RuntimeError
    
    def fun_switch(self, parameters, trace):
        '''
        execute switch command
        '''
        try:
            self.cur_switch[0] = [1, parameters[0]]
            return True
        except:
            raise_error("running error: ", "switch setting failed", trace)      
            return False
    
    def fun_speak(self, parameters, trace):
        '''
        execute speak command
        '''
        try:
            speak_words = self.calculate_expr(parameters[0], trace)
            self.core_logger.debug(speak_words)
            if not speak_dict[speak_method](speak_words,parameters[1]):
                raise_error("running error: ", "speak method failed", trace)  
                return False
            logger = get_user_logger(f"conversation_for_{self.id}")
            logger.info("server: {}".format(speak_words))
            return True
        except:
            raise_error("running error: ", "speak failed", trace)
            return False
    
    def fun_branch(self, parameters, trace):
        '''
        execute branch command
        '''
        try:
            if self.cur_switch[0][0] == 0:
               raise_error("compile error: ", "brach without switch", trace)
               return False
            cur_str = self.calculate_expr(self.cur_switch[0][1], trace)
            target_str = self.calculate_expr(parameters[0], trace)
            target_step = parameters[1]
            flag = Analyzer_dict[analyzer_chosen](target_str, cur_str, parameters[2])
            if not target_step in self.step_cache:
                raise_error("running error: ", "unKown step", trace)
                return False
            
            if flag: 
                self.cur_switch[0][0] = 2
                return self.run(self.step_cache[target_step], trace)
            return True
        except:
            raise_error("running error: ", "branch command execute failed", trace)
            return False

    def fun_goto(self, parameters, trace):
        '''
        execute goto command
        '''
        try:
            target_step = parameters[0]
            if not target_step in self.step_cache:
                raise_error("running error: ", "unKown step", trace)
                return False
            return self.run(self.step_cache[target_step], trace)
        except:
            raise_error("running error: ", "goto command execute failed", trace)
            return False

    def fun_listen(self, parameters, trace):
        '''
        execute listen command
        '''
        try:
            key = parameters[0]
            words =  listen_dict[listen_method](parameters[1])
            self.var_cache[key] = words
            logger = get_user_logger(f"conversation_for_{self.id}")
            logger.info("User: {}".format(words))
            return True
        except:
            raise_error('running error: ', 'listen command failed', trace)
            return False

    def fun_set(self, parameters, trace):
        '''
        execute set command
        '''
        try:
            key =  parameters[0]
            expr = self.calculate_expr(parameters[1], trace)
            self.var_cache[key] = expr
            return True
        except:
            raise_error('running error: ', 'set command failed', trace)
            return False

    
    def fun_import(self, parameters, trace):
        '''
        execute import command
        '''
        try:
            file_path = parameters[0]
            f = open(file_path, encoding="utf-8")
            codes = f.readlines()
            f.close()
            self.interpret(codes, file_path, trace)
            return True
        except:
            raise_error('running error: ',"import file failed, please check the path", trace)
            return False

    def run(self, commands, trace):
        '''
        execute command with hyper functions 
        '''
        command_fun = {
            'speak': self.fun_speak,
            'listen': self.fun_listen,
            'import': self.fun_import,
            'branch': self.fun_branch,
            'switch': self.fun_switch,
            'set': self.fun_set,
            'goto': self.fun_goto
        }

        self.cur_switch.insert(0, [0,None])
        
        for command in commands:
            if self.cur_switch[0][0] > 1:
                break
            if not command['command'] in ['branch', 'default']:
                self.cur_switch[0][0] = 0
            if not command_fun[command['command']](command['parameters'], trace + command['trace']):
                return False
        
        self.cur_switch.pop(0)
        return True

    def interpret(self, codes : list, file: str, trace: str):
        '''
        Overview:
            the main step of interprete
        '''

        cur_step = ""
        main = []
        # scan the codes and push them into step_dict
        for line, sentence in enumerate(codes):
            tmp_trace = f'({file})line{line} :{sentence}'

            # skip the blank line
            if len(sentence.split()) < 1: continue

            parse_result = self.parser.parse(sentence)
            if isinstance(parse_result, str):
                raise_error("sytnax error: ", parse_result, trace + tmp_trace)
                return
            
            # process the 'step' command
            if parse_result[0] == 'step':
                if not cur_step == "":
                    raise_error("compile error", "Nested step declarations are not allowed",  trace + tmp_trace)
                    return
                cur_step = parse_result[1][0]
                self.step_cache[cur_step] = []
            # process the 'stepover' command
            elif parse_result[0] == 'stepover':
                if cur_step == "":
                    raise_error("compile error", "Step and Stepover do not match", trace + tmp_trace)
                    return
                cur_step = ""
            # store the other command to the Corresponding cache
            else:
                if cur_step == "":
                    main.append({'command': parse_result[0], 
                                'parameters': parse_result[1],
                                'trace': tmp_trace})
                else:
                    self.step_cache[cur_step].append({'command': parse_result[0], 
                                                    'parameters': parse_result[1],
                                                    'trace': tmp_trace})
            
        self.run(main, trace)
        

    
            