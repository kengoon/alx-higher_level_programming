#!/usr/bin/python3
"""
MySQL script that lists all states that starts with
the letter N in the table states
"""
from sys import argv

from MySQLdb import connect


def main(username, password, database):
    """
    Main function.
    :param username:
    :param password:
    :param database:
    :return:
    """
    conn = connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name "
        "LIKE BINARY 'N%' ORDER BY states.id ASC;"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    argv = argv[1:]
    main(*argv)
