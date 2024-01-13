#!/usr/bin/python3
"""
    A script that takes in the name of state as an argument and list all
    cities of the state using the database hbtn_0e_4_usa
    Username, password and database name and state are given as user args
"""


if __name__ == "__main__":
    """Main execution"""
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host="localhost",
            port=3306)

    cursor = db.cursor()

    query = """ SELECT cities.name FROM states
            INNER JOIN cities ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY id ASC"""

    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fethall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
