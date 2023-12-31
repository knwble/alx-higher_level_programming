#!/usr/bin/python3
"""
Displays all values in the states where
`name` matches the argument from the database `hbtn_0e_0_usa`.
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

        # Create the SQL query with the argument using format and execute it
        query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4])
        db_cursor.execute(query)

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
