#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa"""

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

    # Create a new State object for Louisiana
    state_new = State(name="Louisiana")

    # Add the new State object to the session
    session.add(state_new)

    # Commit the session to persist the changes to the database
    session.commit()

    # Print result
    print("{}".format(state_new.id))

    # Close the session
    session.close()
