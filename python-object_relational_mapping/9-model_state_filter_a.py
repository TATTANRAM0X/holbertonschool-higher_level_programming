#!/usr/bin/python3
'''
This module contains the function model_state_filter_a()
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def print_state_with_a():
    '''
    Lists all State objects that contain the letter a
    from the database
    '''

    address = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])
    engine = create_engine(address, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    State.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    conn = engine.connect()
    session = Session(bind=conn)

    objs = session.query(State).order_by(State.id).all()

    for obj in objs:
        if 'a' in obj.name:
            print("{}: {}".format(obj.id, obj.name))


if __name__ == "__main__":
    print_state_with_a()
