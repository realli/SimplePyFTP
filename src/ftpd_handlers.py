from pyftpdlib.handlers import FTPHandler
import ftpd_log
import logging

class SimpleHandler(FTPHandler):
  logger = logging.getLogger('visit')
  def on_login(self, username):
    self.logger.info("%s - log in - %s", username,self.remote_ip)
  def on_logout(self, username):
    self.logger.info("%s - log out - %s", username,self.remote_ip)
  def on_login_failed(self, username, password):
    self.logger.info("%s - log in failed - %s", username,self.remote_ip)

