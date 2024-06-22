#!/usr/bin/python3
""" list all states with name matching the argument
from database"""

import MySQLdb
import sys


def filter_states_by_name(username, password, dbname, state_name):
    """ Connects to  database and prints states with a name
    matching the argument"""
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
    query = ("SELECT id, name FROM states WHERE BINARY name = %s "
             "ORDER BY id ASC".format(state_name))

    cursor.execute(query, (state_name,))

    # Fetch all the results
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(f"({state[0]}, '{state[1]}')")

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        filter_states_by_name(username, password, dbname, state_name)
