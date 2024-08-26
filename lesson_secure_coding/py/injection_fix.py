import os
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, text
from sqlalchemy.exc import SQLAlchemyError

filename = 'example.fix.py.db'
conn_string = f'sqlite:///{filename}'

def reset_database():
    try:
        os.remove(filename)
    except OSError:
        pass

def setup_database():
    engine = create_engine(conn_string)
    metadata = MetaData()
    
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String)
                 )
    
    metadata.create_all(engine)
    
    try:
        with engine.connect() as connection:
            # Check if data is already present
            result = connection.execute(users.select())
            if result.fetchall():
                print("Data already exists.")
            else:
                connection.execute(users.insert(), [{'name': 'Alice'}, {'name': 'Bob'}])
                print("Data inserted.")
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")

def get_user(user_id):
    engine = create_engine(conn_string)
    with engine.connect() as connection:
        # result = connection.execute(text("SELECT * FROM users WHERE id = :id"), {'id': user_id})
        result = connection.execute(text("SELECT * FROM users"))
        user = result.fetchall()
    return user

# reset_database()
setup_database()
# user = get_user("1 OR 1=1")
user = get_user(1)

print(user)



from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///example.fix.py.db')
metadata = MetaData()
metadata.reflect(bind=engine)

for table in metadata.sorted_tables:
    print(f"Table: {table.name}")
    with engine.connect() as connection:
        result = connection.execute(table.select())
        print("Rows:", result.fetchall())
