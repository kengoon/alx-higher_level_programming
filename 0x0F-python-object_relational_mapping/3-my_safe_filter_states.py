#!/usr/bin/python3
"""
Write a script that takes in an argument
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':

    conn_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = conn_db.cursor()

    forth_arg = argv[4]
    query_l = "SELECT * FROM states WHERE name = %s"

    cursor.execute(query_l, (forth_arg,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn_db.close()
