#!usr/bin/env python
#coding: utf-8

import urllib2
import gzip
import StringIO
from MySQLDatabase import MySQLDatabase

def connectDb():
    ip = 'localhost'
    user = 'root'
    password = '123456'
    database = 'baidu'
    db = MySQLDatabase(ip, user, password, database)
    db.OpenDb()
    return db