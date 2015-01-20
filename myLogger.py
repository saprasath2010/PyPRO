#!/usr/bin/python
import logging, logging.handlers
#Open the log file in the required path mentioned.
def open_log_file(log_file):
    try:
        logger = logging.getLogger(log_file)
        logger.setLevel(logging.DEBUG)
        handler = logging.handlers.RotatingFileHandler(log_file,
                                               maxBytes=204800,
                                               backupCount=5,
                                               )
        formatter = logging.Formatter('%(asctime)s %(filename)s: '    
                       '%(lineno)d:\t'
                       '%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
    except Exception as e:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print message

