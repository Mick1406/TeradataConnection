
"""
Teradata Connection using ODBC DSN - establish connection to Teradata
author: mcarraz
"""

import pyodbc
import os

#userid and password are stored into another script for security reason - load those into session
os.system('pw.py')
from pw import init_username, init_password
username=str(init_username())
password=str(init_password())

#The following create conexion to MCARRAZ 
TDCONN = pyodbc.connect('DSN=MCARRAZ;UID=' + username +';PWD=' + password +';QUIETMODE=YES;',ansi=True, autocommit=True)
cursor=TDCONN.cursor()
print("Connected to MCARRAZ")
