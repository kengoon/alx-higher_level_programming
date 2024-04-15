#!/usr/bin/python3
"""
Write a script that takes in an argument
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


import sys
import MySQLdb

if __name__ == '__main__':

    conn_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = conn_db.cursor()

    forth_arg = sys.argv[4]

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}%'".format(forth_arg)
        )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()
