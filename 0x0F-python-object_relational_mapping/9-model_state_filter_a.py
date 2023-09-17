#!/usr/bin/python3
"""
This script lists all State objects containing the letter a in the db
hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State).order_by(State.id):
        if "a" in states.name:
            print("{}: {}".format(states.id, states.name))
