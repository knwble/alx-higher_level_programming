#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
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

        # Create the SQL query with the argument and execute it
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
        db_cursor.execute(query, (argv[4],))

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
