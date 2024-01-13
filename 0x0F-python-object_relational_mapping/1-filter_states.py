#!/usr/bin/python3
"""Script that list all states with a name starting with N from database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Main execute"""
    db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port='3306')

    cursor = db.cursor()
    
    cursor.execute("SELECT FROM * WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
