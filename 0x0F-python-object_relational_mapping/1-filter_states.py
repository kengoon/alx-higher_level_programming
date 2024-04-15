#!/usr/bin/python3
"""
A script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
"""


import sys
import MySQLdb

if __name__ == '__main__':

    conn_db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )

    cursor = conn_db.cursor()
    query_l = "SELECT * FROM states WHERE name LIKE BINARY 'N%'"
    cursor.execute(query_l)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()
