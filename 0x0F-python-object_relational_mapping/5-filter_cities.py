#!/usr/bin/python3

'''
This script takes in the name of a state as an argument and prints all cities
'''

import MySQLdb
import sys

if __name__ == '__main__':
    data_base = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost'
    )

    cursor = data_base.cursor()
    cursor.execute(
        'SELECT cities.name FROM cities '
        'INNER JOIN states ON cities.state_id = states.id '
        'WHERE states.name = %s '
        'ORDER BY cities.id ASC', (sys.argv[4], )
    )

    cities = cursor.fetchall()

    index = 0
    for city in cities:
        if index != 0:
            print(", ", end="")
        print("%s" % city, end="")
        index += 1
    print("")

    cursor.close()
    data_base.close()
