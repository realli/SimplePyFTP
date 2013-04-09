# --encoding:utf-8--
# test ftp server demo

# md5 hash setting
import os
import logging
from hashlib import md5

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib._compat import b

class DummyMD5Authorizer(DummyAuthorizer):
  def validate_authentication(self, username, password, handler):
    hash = md5(b(password)).hexdigest()
    try:
      if self.user_table[username]['pwd'] != hash:
        raise KeyError 
    except KeyError:
        raise AuthenticationFailed

def main():
  # auth to managing users
  authorizer = DummyMD5Authorizer()

  # add users
  hash = md5(b('12345')).hexdigest()
  authorizer.add_user('user', hash, '/home/leo/FTPRoot', perm='elradfmwM')

  handler = FTPHandler
  handler.authorizer = authorizer

  # loggin setting
  #logging.basicConfig(filename='/home/leo/ftpd.log', level=logging.DEBUG)
  logging.basicConfig(level=logging.DEBUG)

  handler.banner = "Hello , my friend"
  address = ('', 2200)
  server = FTPServer(address, handler)
  server.max_cons = 256
  server.max_cons_pre_ip = 5
  server.serve_forever()

if __name__ == '__main__':
  print "开始"
  main()
