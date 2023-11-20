#!/usr/bin/python3
""" 
Lists all State objects containing the letter 'a' 
from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query and display State objects containing 'a' in name
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for instance in states_with_a:
        print(instance.id, instance.name, sep=": ")
    
    session.close()
