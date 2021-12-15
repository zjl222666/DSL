import logging
import os
from SerWise.setting import *

user_logger = {}
core_logger = {}

def get_user_logger(file_name) -> logging.Logger:
    '''
    Used to get the corresponding logger, this method will save the log file under user_log and print it out on the console
    '''
    global user_logger
    if not os.path.exists("log_user"):  os.makedirs("log_user")
    if not file_name  in user_logger:
        logger = logging.getLogger("user"+file_name)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)8s] %(message)s')
        
        # file print
        fh = logging.FileHandler("log_user\\{}.log".format(file_name), encoding="utf-8")
        fh.setFormatter(formatter)

        # console print
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)

        logger.setLevel(user_logging_level)
        logger.addHandler(fh)
        logger.addHandler(sh)
        user_logger[file_name] = logger
    return user_logger[file_name]



def get_core_logger(file_name) -> logging.Logger:
    '''
    Used to get the corresponding logger, this method will save the log file under "core_log" and won't print it out on the console
    '''
    global core_logger
    if not os.path.exists("log_core"):  os.makedirs("log_core")
    if not file_name in core_logger:
        logger = logging.getLogger("core"+file_name)

        formatter = logging.Formatter('[%(asctime)s][%(filename)15s][%(levelname)8s] %(message)s')
        # file print
        fh = logging.FileHandler("log_core\\{}.log".format(file_name), encoding="utf-8")
        fh.setFormatter(formatter)
        logger.setLevel(core_logging_level)
        logger.addHandler(fh)
        user_logger[file_name] = logger
    return user_logger[file_name]
