from pyftpdlib.handlers import FTPHandler
import ftpd_log
import logging

class SimpleHandler(FTPHandler):
  '''
  Simple Handler to hand the messages about login, logout , logout , file_received ....
  all user ops which can be handed
  '''
  visit_logger = logging.getLogger(ftpd_log.logsDict['visitLog']['name'])
  file_ops_logger = logging.getLogger(ftpd_log.logsDict['fileOpsLog']['name'])
  def on_login(self, username):
    SimpleHandler.visit_logger.info("%s - log in - %s", username,self.remote_ip)
  def on_logout(self, username):
    SimpleHandler.visit_logger.info("%s - log out - %s", username,self.remote_ip)
  def on_login_failed(self, username, password):
    SimpleHandler.visit_logger.info("%s - log failed - %s", username,self.remote_ip)
  def on_file_sent(self, file):
    SimpleHandler.file_ops_logger.info("%s - downloaded %s - %s", self.username,file,self.remote_ip)
  def on_file_received(self, file):
    SimpleHandler.file_ops_logger.info("%s - uploaded %s - %s", self.username,file,self.remote_ip)
  def in_incomplete_file_sent(self, file):
    SimpleHandler.file_ops_logger.info("%s - downloaded failed: %s - %s", self.username,file,self.remote_ip)
  def on_incomplete_file_received(self, file):
    import os
    os.remove(file)
    SimpleHandler.file_ops_logger.info("%s - uploaded failed: %s,already been deleted - %s", self.username,file,self.remote_ip)



