import logging
from logging.handlers import RotatingFileHandler

# logsDict stores the loggers' info , simplly as name , file to log and the format strings
logsDict = {
    'visitLog': {'name':'visit', 'fileName':'simple_ftpd_visit.log','fmt':" %(levelname)s:%(asctime)s - %(message)s"},
    'fileOpsLog': {'name':'fileOps', 'fileName':'simple_ftpd_fileops.log','fmt':"%(levelname)s:%(asctime)s - %(message)s"}
    }


# used to set the logging system
def set_log(name='visit',fileName='ftpd_log_unknow.log',fmt="%(levelname)s:%(asctime)s - %(message)s"):
  '''
  set the logger 'name' to log into file 'filename' and use the format 'fmt'
  the logger all use Rotating File to dispatch messages which will send messages 
  to disk file and rotating the file based the maximum log file size.
  '''
  logger = logging.getLogger(name)
  logger.setLevel(logging.DEBUG)
  logger.propagate=0

  ch = RotatingFileHandler(fileName,
                                  mode='a',
                                  maxBytes=10*1024*1024,
                                  backupCount=5
                                   )
  ch.setLevel(logging.DEBUG)

  formatter = logging.Formatter(fmt)
  ch.setFormatter(formatter)

  logger.addHandler(ch)


# used to set the logger when imported
for __, logDict in logsDict.items():
  if not logging.getLogger(logDict['name']).handlers:
    set_log(logDict['name'], logDict['fileName'])
