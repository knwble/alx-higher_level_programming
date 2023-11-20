#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    try:
        # Connect to MySQL server running on localhost at port 3306
        db_connect = db.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )

        # Create a cursor object to interact with the database
        db_cursor = db_connect.cursor()

        # Execute a parameterized query to fetch data securely
        query = (
            "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]}
        )
        db_cursor.execute(query, {'name': argv[4]})

        # Fetch all the rows from the query result
        rows_selected = db_cursor.fetchall()

        # Display results
        for row in rows_selected:
            print(row)

    except db.Error as e:
        print("Error:", e)

    finally:
        # Close the cursor and database connection
        db_cursor.close()
        db_connect.close()
