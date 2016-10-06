#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from Parse import Parse
from Provider import Provider
#import pymysql.cursor
#import sys


contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Resource Map Research Tool</title>
</head>
<body>
<h2>Workstation</h2>
</body>
</html>
'''

def main():
    sqlite_file = 'research.sqlite'     # name of the sqlite database file
    cursor = initializeDB(sqlite_file)  #cursor is pointer to db connection
    p = Provider.fromDB(cursor)         #p -> array of providers
    queryDB(cursor)
    #browseLocal(contents)              #display webpage
    cursor.close()
def initializeDB(sqlite_file):
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    return conn.cursor()


def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac
def queryDB(c):
    table_name = 'resource'
    #id_column = 'rid'
    c.execute('SELECT * FROM {tn}'.\
        format(tn=table_name))
    all_rows = c.fetchall()
    print('1):', all_rows)
    return all_rows

main()