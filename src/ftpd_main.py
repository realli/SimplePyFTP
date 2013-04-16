#!/usr/bin/env python
# --encoding:utf-8--
# test ftp server demo

# md5 hash setting
import os
import logging
import logging.config
from hashlib import md5

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
#from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib._compat import b

from ftpd_handlers import SimpleHandler
import ftpd_users

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
  ftpd_users.addUsers(authorizer)

  handler = SimpleHandler 
  handler.authorizer = authorizer

  # loggin setting
  
  handler.banner = "Hello , my friend"
  address = ('', 2200)
  server = FTPServer(address, handler)
  server.max_cons = 256
  server.max_cons_pre_ip = 5
  server.serve_forever()

if __name__ == '__main__':
  print "开始"
  main()
