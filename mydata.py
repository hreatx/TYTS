#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:42:17 2018

@author: yty from TYTS

database interface for Budding Pop
"""

import sqlite3
import glob
import datetime

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
        DROP TABLE IF EXISTS Records;
        DROP TABLE IF EXISTS Items;
        DROP TABLE IF EXISTS Purchase;
        DROP TABLE IF EXISTS Gallery;
        DROP TABLE IF EXISTS Smiles;

        create table Users(
            uid text,
            password text,
            money integer,
            energy integer,
            level integer
        );

        create table Records(
            uid text,
            start integer,
            end integer
        );

        create table Items(
            iname text,
            price integer,
            energy integer
        );

        create table Purchase(
            time text,
            uid text,
            iname text,
            num integer
        );

        create table Gallery(
            path text,
            tag integer
        );

        create table Smiles(
            uid text,
            time integer
        )
        """)
    admin = ('admin','admin',500,0,1,)
    c.execute(
        """
        INSERT INTO Users VALUES (?,?,?,?,?)
        """,admin)
    conn.commit()
    c.close()
    c = conn.cursor()
    stickers = [] 
    cwdsad = '../TYTS/sticker/sad/*.gif'
    cwdnat = '../TYTS/sticker/natural/*.gif'
    cwdhap = '../TYTS/sticker/happy/*.gif'
    for i,f in enumerate(glob.glob(cwdsad)):
        stickers.append((f,1,))
    for i,f in enumerate(glob.glob(cwdnat)):
        stickers.append((f,2,))
    for i,f in enumerate(glob.glob(cwdhap)):
        stickers.append((f,3,))
    c.executemany("""
    INSERT INTO Gallery VALUES (?,?)
    """, stickers)
    conn.commit()
    t = [('Macaron',4,7,),
    ('Ice Cream',5,10,),
    ('Panini',15,40,),
    ('Pizza',18,48,),
    ('Hamburger',20,50)]
    c.executemany("""
    INSERT INTO Items VALUES (?,?,?)
    """,t)
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
    INSERT INTO Users VALUES (?,?,38,0,1)
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
    # return a list of [uid, money, energy, level] (list)
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
    # save data to database, return whether success (boolean)
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
    # return a list of absolute paths of stickser available (list)
    if level>3:
        tag = 3
        limit = 2*level
    else:
        tag = level
        limit = 4
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    result = []
    c.execute("""
    SELECT path FROM Gallery 
    WHERE tag = ?
    LIMIT ?
    """,(tag,limit))
    for i in c.fetchall():
        result.append(i[0])
    c.close()
    return result

def getItems():
    # return a list of dictionary {name: ,price: ,energy: } (dictionary)
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    c.execute("""
    SELECT * FROM items
    """)
    result = []
    for i in c.fetchall():
        result.append({'name':i[0],'price':i[1],'energy':i[2]})
    return result


def record(account,start,end):
    # record the login and logout time, in form of long integer (boolean)
    # add a new line to table records
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (account,start,end)
    c.execute("""
    INSERT INTO records VALUES (?,?,?)
    """,t)
    conn.commit()
    t = (account,end,)
    ex = c.execute("""
            SELECT EXISTS(
                SELECT * FROM Records
                WHERE uid = ? AND end = ?
            )
    """, t)
    conn.commit()
    success = ex.fetchone()
    success = success[0]
    c.close()
    return bool(success)


def lastLogout(account):
    # return the time of last logout (long int)
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (account,)
    c.execute("""
    SELECT MAX(end) FROM Records
    WHERE uid = ?
    """,t)
    result = c.fetchone()[0]
    c.close()
    return result

def totalTime(account):
    # return the total online time of a user (int)
    # in form of second
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (account,)
    c.execute("""
    SELECT start, end FROM Records
    WHERE uid = ?
    """,t)
    sumtime = 0
    for f in c.fetchall():
        sumtime = sumtime + f[1] - f[0]
    return sumtime

def addSmile(account,time):
    # record the time of smiles (boolean)
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (account,time,)
    c.execute("""
    INSERT INTO Smiles VALUES (?,?)
    """,t)
    conn.commit()
    ex = c.execute("""
            SELECT EXISTS(
                SELECT * FROM Smiles
                WHERE uid = ? AND  time = ?
            )
    """, t)
    conn.commit()
    success = ex.fetchone()
    success = success[0]
    c.close()
    return bool(success)
 
def getSmiles(account):
    # return the number of records of smiles (int)
    conn = sqlite3.connect('mydata.db')
    c = conn.cursor()
    t = (account,)
    c.execute("""
    SELECT COUNT(*) FROM Smiles
    WHERE uid = ?
    """,t)
    count = c.fetchone()[0]
    return count


if __name__ == '__main__':
    initDB()
    print(register("yty","123"))
    print(load("yty"))
    save("yty",100,20,2)
    print(load("yty"))
    print(check('yty'))
    print(check('yt'))  
    print(getApperance(3))
    print(login('yty','123456'))
    print(login('yty','123'))
    print(getItems())
    time = datetime.datetime.now()
    print(addSmile('yty',int(time.timestamp())))
    print(getSmiles('yty'))
    print(totalTime('yty'))