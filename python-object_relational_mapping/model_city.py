#!/usr/bin/python3
"""Start link class to table in database """


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


# Create a base class for declarative models
Base = declarative_base()


# Define the City class, representing the 'cities' table in the database
class City(Base):
    """Represents a cities in the database. Attributes:
    - id: The unique identifier for the cities.
    - name: The name of the cities.
    - state_id: The foreign key to the states table."""

    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey('states.id'),
                      nullable=False)
