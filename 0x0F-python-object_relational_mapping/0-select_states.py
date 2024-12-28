#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Arguments: mysql username, mysql password, database name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # No need for host and port as they are set by default
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
