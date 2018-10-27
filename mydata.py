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
#from PyQt5 import QtCore
#from PyQt5 import QtGui
#from pyQt5 import QtSql
import sqlite3
import os
import glob

STICKERPATH = "sticker/"
ICONPATH = "icon/"

def initDB():
    # This is a method called only at the first building
    # Create a database and initialize
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    c.executescript(
        """
        DROP TABLE IF EXISTS Users;
        DROP TABLE IF EXISTS Items;
        DROP TABLE IF EXISTS Purchase;
        DROP TABLE IF EXISTS Gallery;
        
        create table Users(
            uid text,
            password text,
            money integer,
            energy integer,
            level integer
        );

        create table Items(
            iid integer,
            iname text,
            price integer,
            icon text
        );

        create table Purchase(
            time text,
            uid text,
            iid integer,
            num integer
        );

        create table Gallery(
            path text
        );
        """)
    conn.commit()
    c.close()
    c = conn.cursor()
    stickers = [] 
    cwd = os.path.dirname(os.path.abspath(__file__))
    cwdstck = cwd+'/sticker/*.gif'
    for i,f in enumerate(glob.glob(cwdstck)):
        stickers.append((f,))
    c.executemany("""
    INSERT INTO Gallery VALUES (?)
    """, stickers)
    conn.commit()
    c.close()


def check(account):
    # Check if account exist
    # Return a boolean value
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (account,)
    ex = c.execute("""
        SELECT EXISTS(
        SELECT * FROM Users
        WHERE uid = ?)
    """, t)
    success = ex.fetchone()
    success = success[0]
    c.close()
    return bool(success)

def register(account,pwd):
    # Register a new account with password
    # Return a boolean value
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (account, pwd)
    c.execute("""
    INSERT INTO Users VALUES (?,?,0,0,0)
    """, t)
    t = (account,)
    ex = c.execute("""
            SELECT EXISTS(
                SELECT * FROM Users
                WHERE uid = ?
            )
    """, t)
    conn.commit()
    success = ex.fetchone()
    success = success[0]
    c.close()
    return bool(success)

def login(account,pwd):
    # Check if account and password match
    # Return a boolean value
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (account,)
    c.execute("""
    SELECT password FROM Users
    WHERE uid = ?
    """, t)
    info = c.fetchone()
    c.close()
    if info is None:
        return False

    if info[0] == pwd:
        return True
    else:
        return False

def load(account):
    # Retrieve data from database, 
    # return a list of [uid, money, energy, level]
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (account,)
    c.execute("""
    SELECT uid, money, energy, level FROM Users
    WHERE uid = ?
    """, t)
    info = c.fetchone()
    c.close()
    result = []
    for i in info:
        result.append(i)
    return result

def save(account,money,energy,level):
    # save data to database, return whether success
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (money,energy,level,account,)
    c.execute("""
    UPDATE Users
    SET money = ?, energy = ?, level = ?
    WHERE uid = ?
    """, t)
    conn.commit()
    c.execute("""
    SELECT money, energy, level FROM Users
    WHERE uid = ?
    """, (account,))
    ck = c.fetchone()
    ckExpected = [money,energy, level]
    c.close()
    for i,j in zip(ck, ckExpected):
        if i != j:
            return False
    return True



def getApperance(level):
    # return a list of absolute paths of stickser available
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    result = []
    c.execute("SELECT * FROM Gallery LIMIT ?",(level,))
    for i in c.fetchall():
        result.append(i[0])
    c.close()
    return result


if __name__ == '__main__':
    initDB()
    print(register("yty","123456"))
    print(load("yty"))
    save("yty",100,20,2)
    print(load("yty"))
    print(check('yty'))
    print(check('yt'))  
    print(getApperance(3))
    print(login('yty','123456'))
    print(login('yty','123'))
    