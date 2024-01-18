#!/usr/bin/python3
"""
Module that contains the class definition of a State
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table states
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://username:password@localhost:3306/database')

    # Create all the tables in the database
    Base.metadata.create_all(engine)

    # Uncomment the following lines if you want to add an example entry to the states table
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # new_state = State(name='Example State')
    # session.add(new_state)
    # session.commit()
