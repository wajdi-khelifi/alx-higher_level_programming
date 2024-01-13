#!/usr/bin/python3
"""
    A script that list all states objects from datbase hbtn_0e_6_usa
    Username, password and database will be passed as arguments to the script
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == ""__main__"":
    """Main execution"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                                sys.argv[1], sys.argv[2], sys.argv[3]),
                                pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    states = session.query(State).order_by(state.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
