#!/usr/bin/python3
""" prints first State object from database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state(username, password, dbname):
    """
    Connects to the database and prints the first State object,
    sorted by states.id in ascending order.
    """
    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, dbname), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the first State object ordered by id
    state = session.query(State).order_by(State.id).first()

    # Print state. 'Nothing' if no state is found
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        fetch_first_state(username, password, dbname)
