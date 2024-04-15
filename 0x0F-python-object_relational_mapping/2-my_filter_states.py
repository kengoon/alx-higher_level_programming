#!/usr/bin/python3
"""
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
from MySQLdb import connect
from sys import argv


def main(user, password, db_name, state_name):
    """
    main function
    :param user:
    :param password:
    :param db_name:
    :param state_name:
    :return:
    """
    db = connect(host="localhost", user=user, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name = '{state_name}'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    argv = argv[1:]
    main(*argv)