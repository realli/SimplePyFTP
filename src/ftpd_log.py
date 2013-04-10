import logging
from logging.handlers import RotatingFileHandler

def set_visit_log():
  # set the visit log system
  logger = logging.getLogger('visit')
  logger.setLevel(logging.DEBUG)
  logger.propagate=0

  ch = RotatingFileHandler('simple_ftpd_visit.log',
                                  mode='a',
                                  maxBytes=10*1024*1024,
                                  backupCount=5
                                   )
  ch.setLevel(logging.DEBUG)

  formatter = logging.Formatter('%(asctime)s - %(message)s')
  ch.setFormatter(formatter)

  logger.addHandler(ch)
if not logging.getLogger().handlers:
  set_visit_log()
