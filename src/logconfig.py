# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

# configuration logging files and console logging
def setup_logging():
    """
    define logging
    :return:
    """
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    file_handler = RotatingFileHandler(
        "shoooter.log", # log file
        maxBytes=10 * 1024 * 1024, # log size 10M
        backupCount=5, # log retain 5
        encoding="utf-8", # log encode
    )

    # initialization logging information
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(log_format))

    # create logging controller handler'
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(log_format))

    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, console_handler],
    )


