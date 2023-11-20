#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    try:
        # Connect to MySQL server running on localhost at port 3306
        db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            host='localhost'
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the query to retrieve states starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

        # Fetch all the rows from the query result
        states_with_N = cursor.fetchall()

        # Display results
        for state in states_with_N:
            print(state)
    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
