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
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY name ASC;")
    rows = cur.fetchall()
    for id_, name in rows:
        print(f"({id_}, '{name}')")


if __name__ == "__main__":
    argv = argv[1:]
    if len(argv) != 3:
        print(f"Usage: {argv[0]} username password database")
        exit(1)
    main(*argv)
