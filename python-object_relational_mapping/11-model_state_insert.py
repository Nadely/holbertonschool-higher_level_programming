#!/usr/bin/python3
"""script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

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
    state_new = State(name="Louisiana")
    session.add(state_new)

# Commit the session to persist the changes to the database
    session.commit()

    # Print result
    print("{}: {}".format(state_new.id, state_new.name))

    # Close the session
    session.close()
