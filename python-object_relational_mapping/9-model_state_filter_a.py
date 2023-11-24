#!/usr/bin/python3
"""script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to execute SQL commands
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    contain_a = (session.query(State).filter(State.name.like('%a%')).order_by(
        State.id))

    # Print result
    for state in contain_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
