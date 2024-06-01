#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import mysql.connector 
from mysql.connector import connection
from mysql.connector import Error
from mysql.connector import errorcode
import os, sys



def get_connection():
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                 database=os.environ.get('foodatabase'),
                                 user=os.environ.get('foousername'),
                                 password=os.environ.get('foopassword'),
                                 port = os.environ.get('fooport'),
                                 use_pure=True)
        if connection.is_connected():
            #cursor = connection.cursor(buffered=True)
            print("Connected to MySQL database... ")
            return connection
           #db_Info = connection.get_server_info()
    except Error as e :
            print ("Error while connecting to MySQL", e)
    return false

