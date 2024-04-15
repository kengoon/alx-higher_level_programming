#!/usr/bin/python3
"""
MySQL script that lists all states that starts with
the letter N in the table states
"""
import sys

from MySQLdb import connect


def main():
    """
    Main function.
    :param username:
    :param password:
    :param database:
    :return:
    """
    conn = connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
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
    main(argv[1], argv[2], argv[3])
