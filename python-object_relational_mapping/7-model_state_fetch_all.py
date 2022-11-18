#!/usr/bin/python3
'''
Function model_state_fetch_all() which lists all the
states of a database
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def model_state_fetch_all():
    ''' lists all State objects from the database '''

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    State.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    conn = engine.connect()
    session = Session(bind=conn)

    objs = session.query(State).order_by(State.id).all()

    for obj in objs:
        print('{}: {}'.format(obj.id, obj.name))


if __name__ == "__main__":
    model_state_fetch_all()
