#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        cur = db.cursor()
        cur.execute("SELECT * FROM cities ORDER BY id ASC")
        [print(row) for row in cur.fetchall()]

    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()
