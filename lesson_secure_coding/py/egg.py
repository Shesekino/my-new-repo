from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, text
from sqlalchemy.exc import SQLAlchemyError

def setup_database():
    engine = create_engine('sqlite:///example.db')
    metadata = MetaData()
    
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String)
                 )
    
    metadata.create_all(engine)
    
    try:
        with engine.connect() as connection:
            # Insert data
            result = connection.execute(users.insert(), [{'name': 'Alice'}, {'name': 'Bob'}])
            print(f"Rows inserted: {result.rowcount}")
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")

def check_data():
    engine = create_engine('sqlite:///example.db')
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    users = metadata.tables['users']
    
    with engine.connect() as connection:
        result = connection.execute(users.select())
        rows = result.fetchall()
        print("Data in table:", rows)

# Run setup and check functions
setup_database()
check_data()
