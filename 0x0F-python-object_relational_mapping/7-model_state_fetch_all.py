#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database)

    try:
        engine = create_engine(conn_str)
        Session = sessionmaker(bind=engine)
        session = Session()

        Base.metadata.create_all(engine)

        states = session.query(State).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("Error:", e)
        sys.exit(1)

    finally:
        if session:
            session.close()
