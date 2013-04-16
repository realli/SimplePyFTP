# --encoding:utf-8--
import sqlite3 as lite
from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from hashlib import md5
from pyftpdlib._compat import b

def insertTestUserInfo():
  try :
    con = lite.connect('simplepyftp.db') 
    cur = con.cursor()
    hash = md5(b('12345')).hexdigest()
    cur.execute("INSERT INTO UserInfo(name,pwd,home,perm,msg_login) VALUES('user', :hash, '/home/leo/FTPRoot', 'elradfmwM','hello')", {"hash": hash})

    con.commit()
  except lite.Error, e:
    print "test info: %s" % e.args[0]
  finally:
    if con:
      con.close()


def initialUserInfo():
  '''
  create a database table store users' info,included:

  name TEXT PRIMARY KEY , --which is user's name or account
  pwd TEXT , -- the password which digested by md5
  perm TEXT, -- the perm
  msg_login TEXT,
  msg_logout TEXT
  '''
  with lite.connect('simplepyftp.db') as con:
    cur = con.cursor()
    cur.execute("select count(*) FROM sqlite_master WHERE type='table' and name = 'UserInfo' ")

    row = cur.fetchone()
    # create database if not exist
    if not row[0]: 
      cur.execute("create TABLE UserInfo(name TEXT PRIMARY KEY, pwd TEXT,home TEXT, perm TEXT, msg_login TEXT, msg_logout TEXT)")
    con.commit()

def addUsers(auth):
  '''
  accept a DummyAuthorizer object, add users using the function add_user provided by DummyAuthorizer
  '''

  if not isinstance(auth,DummyAuthorizer):
    return
  with lite.connect('simplepyftp.db') as con:
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("select * FROM UserInfo")

    while True:
      row = cur.fetchone()
      if not row:
        break
      
      auth.add_user(row['name'], row['pwd'], row['home'],row['perm'], row['msg_login'], row['msg_logout'])



initialUserInfo()
insertTestUserInfo()

