#!/usr/bin/python3
"""
MySQL script that lists all states that starts with
the letter N in the table states
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute(
        """SELECT * FROM states WHERE name
        LIKE BINARY 'N%' ORDER BY states.id ASC;"""
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
