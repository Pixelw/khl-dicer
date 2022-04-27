import logging
import sys
from logging.handlers import TimedRotatingFileHandler

from util.osfile import check_dir, concat_path

LOG_PATTERN = '%(asctime)s\t(%(filename)s:%(lineno)d)-%(levelname)s:\t%(message)s'


def set_logger(log_name, log_to_file=True, log_path='logs/', log_pattern=LOG_PATTERN, log_level='INFO',
               timed_rotate=None):
    logger = logging.getLogger(log_name)
    if not logger.hasHandlers():
        formatter = logging.Formatter(log_pattern)
        # if log to file enabled
        if log_to_file is True:
            check_dir(log_path)
            log_file_path = concat_path(log_path, log_name)
            if timed_rotate is not None:
                file_handler = TimedRotatingFileHandler(log_file_path, when=timed_rotate, interval=1, encoding='utf-8')
            else:
                file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
            file_handler.suffix = '%Y%m%d.log'
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(formatter)
        console.setLevel(log_level)
        logger.addHandler(console)
        logger.setLevel(level=log_level)
    return logger
