'''
error type:
    syntax error
    memory error
    
'''

from DSL.util.logger import get_user_logger

def raise_error(type, content, trace):
    logger = get_user_logger("running_log")
    logger.error("{}: {}".format(type, content))
    logger.error("trace back: {}".format(trace))

def raise_warning(content, trace):
    logger = get_user_logger("running_log")
    logger.warn("{}: {}".format(trace, content))
    
