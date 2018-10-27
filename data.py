#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:42:17 2018

@author: yty from TYTS

data interface for Budding Pop
"""
"""
Database Content:
    Table Users:
        uid         CHAR[10]
        password    CHAR[20]
        uname       CHAR[20]
        money       INTEGER
        energy      INTEGER
        level       INTEGER
        PrimaryKey(uid)
    
    Table Items:
        iid         INTEGE
        iname       CHAR[20]
        price       INTEGER
        icon        CHAR[20]
        PrimaryKey(iid)
    
    Table Purchase:
        uid         CHAR[10]
        iid         INTEGER
        time        DATE
        num         INTEGER
        PrimaryKey(time)
    
    Table Gallery:
        sid         INTEGER
        path        CHAR[20]
"""
from PyQt5 import QtCore
from PyQt5 import QtGui
from pyQt5 import QtSql

def initDB(path):
     db = qtsql.QSqlDatabase.addDatabase("QMYSQL");

def check(account):
    # Check if account exist
    