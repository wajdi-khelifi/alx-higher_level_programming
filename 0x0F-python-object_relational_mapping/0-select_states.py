#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main':
  data_base = MySQLdb.connect(user = sys.argv[1],
                              password = sys.argv[2],
                              data_base = sys.argv[3],
                              host = 'localhost',
                              port = 3306)
  cursor = data_base.cursor()
  cursor.excute("SETECT * FROM states ORDER BY id ASC")
  data = cursor.fetchall()

  for row in data:
    print(row)
  cursor.close()
  data_base.close()