from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLite database in-memory (you can replace it with your MySQL connection details)
DATABASE_URI = 'sqlite:///:memory:'
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

class State(Base):
    """State class representing the states table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Create the table in the database
Base.metadata.create_all(engine)

# Insert multiple sample states into the states table
states_to_insert = [
    State(name='California'),
    State(name='Arizona'),
    State(name='Texas'),
    State(name='New York'),
    State(name='Nevada'),
]

session = sessionmaker(bind=engine)()
session.add_all(states_to_insert)
session.commit()

# Query and print all states from the states table
result = session.query(State).all()
for state in result:
    print(f"{state.id}: {state.name}")
