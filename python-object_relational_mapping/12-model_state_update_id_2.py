#!/usr/bin/python3
"""script that changes the name of a State object from the database
hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session to execute SQL commands
    session = Session(engine)

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the State object with id = 2 exists
    if state_to_update:
        # Update the name of the State to "New Mexico"
        state_to_update.name = "New Mexico"

        # Commit the session to persist the changes to the database
        session.commit()

        # Print result
        print("{}".format(state_to_update.id))
    else:
        print("Not found")

    # Close the session
    session.close()
