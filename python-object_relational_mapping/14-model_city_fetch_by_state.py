#!/usr/bin/python3
"""Script to fetch and display City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Query the database and print City objects
    cities = session.query(City).order_by(City.id).all()

    # Print result
    for city in cities:
        state_name = session.query(State.name).filter(State.id ==
                                                      city.state_id).scalar()
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    # Close the session
    session.close()
