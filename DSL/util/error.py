from DSL.util.logger import get_user_logger

def raise_error(type, content, trace):
    logger = get_user_logger("error_record")
    logger.error("{}: {}".format(type, content))
    logger.error("trace back: {}", trace)
