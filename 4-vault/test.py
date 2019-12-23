#! /usr/bin/env python3
import mysql.connector
from mysql.connector import errorcode
import os

release_name = os.environ['RELEASE_NAME']
mysql_host = release_name+"-mysql"


config = {
  'user': 'root',
  'password': 'password',
  'host': mysql_host,
  'database': 'test',
  'raise_on_warnings': True
}

try:
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  print(cnx.connection_id)
  cursor.execute("SHOW TABLES")
  print(cursor.fetchall())
  cursor.execute("SHOW DATABASES")
  print(cursor.fetchall())
  cursor.execute("SELECT DATABASE()")
  print(cursor.fetchall())
  #cursor.execute("CREATE TABLE testTable (testID int)")
  #print(cursor.fetchall())
  cursor.execute("SHOW TABLES")
  print(cursor.fetchall())


  cursor.execute("INSERT INTO testTable (testID) VALUES (1)")
  cursor.execute("SELECT * FROM testTable")
  print(cursor.fetchall())
  print(cursor.fetchall())
  cursor.close()
  cnx.close()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
