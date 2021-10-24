import logging


def logconf(file):
    logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler(file)
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    return logger
