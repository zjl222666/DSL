from SerWise.setting import user_setting,save_var
from SerWise.util.error import raise_error
from SerWise.util.logger import get_user_logger, get_core_logger
from SerWise.core.database import userDatabase
from SerWise.core.interpreter import Interpreter
from SerWise.setting import user_setting
import random
import sys
import argparse
import os
from rich import print

class DslProcess:
    '''
    Overview:
        Class used to create, manage, and run a customer service dialogue process
    Parameters:
        - id <str> : id for current process
        - codes <list[str]> : script the process will run
        - file <str> : the file path of script
    Returns:
        None  
    '''
    def __init__(self, id : str, codes : list, file : str):

        self.id = id
        self.codes = codes
        self.file = file
        self.logger = get_user_logger(f"conversation_for_{id}")
        self.database = userDatabase()
        self.interpreter = Interpreter(id)
        self.logger.debug(f"service process {id} start successfully")


    def run(self):
        '''
        Overview:
            the main step of a customer service dialogue process
        '''

        user_num = self.database.get_num()
        if user_setting == 'input':
            self.logger.info(f"请输入用户id, 目前数据库中用户人数为{user_num}")
            id = input()
        elif user_setting == 'random':
            self.logger.debug(f"随机生成用户id，目前库中用户总数为{user_num}")
            id = str(random.randint(0, user_num - 1))
            self.logger.debug(f"生成用户id为{id}")
        else:
            id = ""

        # load user information
        try:
            user_information = self.database.select_with_id(id)
        except:
            user_information = {}
        if not "$id" in user_information.keys():
            self.logger.warning(f'未知用户访问')
        for key,value in user_information.items():
            self.interpreter.add_var(key, value)
        
        self.interpreter.interpret(self.codes, self.file, "")

        if save_var:
            self.database.result_save(f"result_{self.id}", self.interpreter.var_cache)
            self.logger.debug(f"已将过程变量存入数据库中，table名为result_{self.id}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, required=True)
    parser.add_argument('--file_path', type=str, required=True)
    args = parser.parse_args()
    f = open(args.file_path, encoding="utf-8")
    codes = f.readlines()
    f.close()
    process = DslProcess(args.id, codes, args.file_path)
    process.run()
    os.system("pause")

if __name__ == "__main__":
    main()