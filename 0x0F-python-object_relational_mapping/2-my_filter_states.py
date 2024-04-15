#!/usr/bin/python3
"""
a script that takes in an argument
"""

from MySQLdb import connect
from sys import argv


def main(user, password, db_name, state_name):
    """
    main function
    """
    db = connect(host="localhost", user=user, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name = '{state_name}'")

    for row in cur.fetchall():
        print(row)
