#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and prints all cities
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

        with db_connect.cursor() as db_cursor:
            # Execute SQL query to list cities of the given state sorted by id in ascending order
            db_cursor.execute(
                "SELECT cities.id, cities.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name LIKE BINARY %(state_name)s "
                "ORDER BY cities.id ASC",
                {'state_name': argv[4]}
            )
            rows_selected = db_cursor.fetchall()

        # Display the results
        if rows_selected:
            for row in rows_selected:
                print(row[1])

    except db.Error as e:
        print("Error:", e)

    finally:
        # Close the database connection
        if db_connect:
            db_connect.close()
