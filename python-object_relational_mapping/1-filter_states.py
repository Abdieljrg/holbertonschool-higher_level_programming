#!/usr/bin/python3
""" list all states with a name with "N" """

import MySQLdb
import sys


def filter_states(username, password, dbname):
    """ Connects the database and prints name
    starting with 'N'"""
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    cursor = db.cursor()

    # Execute the SQL query
    query = ("SELECT id, name FROM states WHERE name LIKE BINARY 'N%' "
             "ORDER BY id ASC")
    cursor.execute(query)

    # Fetch all the results
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(f"({state[0]}, '{state[1]}')")

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        filter_states(username, password, dbname)
