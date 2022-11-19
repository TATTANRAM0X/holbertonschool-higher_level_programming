#!/usr/bin/python3
'''
This module contains the function model_state_my_get()
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def model_state_my_get():
    '''
    prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
    '''

    address = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                          sys.argv[2],
                                                          sys.argv[3])

    if ';' in argv[4]:
        return

    engine = create_engine(address, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    State.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    conn = engine.connect()
    session = Session(bind=conn)

    objs = session.query(State).order_by(State.id).all()

    for obj in objs:
        if sys.argv[4] == obj.name:
            print(obj.id)
            return
    print('Not found')


if __name__ == "__main__":
    model_state_my_get()