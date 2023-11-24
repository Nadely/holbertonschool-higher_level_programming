#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create a base class for declarative models
Base = declarative_base()

# Define the State class, representing the 'states' table in the database
class State(Base):
    """Represents a state in the database. Attributes:
    - id: The unique identifier for the state.
    - name: The name of the state."""
    
    __tablename__ = 'states'
    id = Column("id", Integer(11), primary_key=True, nullable=False,
                autoincrement=True)
    name = Column("name", String(128), nullable=False)
