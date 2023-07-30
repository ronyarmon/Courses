import pandas as pd
from sqlalchemy import create_engine
db_name, db_user, db_password, db_host = 'testdb', 'postgres', 'postgres', 'localhost'
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}',\
                       pool_pre_ping=True)
# Create table
engine.execute('DROP TABLE IF EXISTS users')
engine.execute("""
             CREATE TABLE IF NOT EXISTS users(
             id SERIAL PRIMARY KEY,
             name VARCHAR (50) NOT NULL,
             email VARCHAR (50) UNIQUE NOT NULL) 
             """)
engine.execute("""INSERT INTO users
                       (name, email)
                       VALUES ('jack', 'jack@gogo.com')""")
print(list(engine.execute("""SELECT * FROM users""")))
names_emails = {'name':['john', 'jean'], 'email':['john@gogo.com','jean@gogo.com']}
users_df = pd.DataFrame.from_dict(names_emails)
print(users_df)
users_df.to_sql('users', con=engine, index=False, if_exists='append')
print ('engine connection test')
users_df = pd.read_sql(f'SELECT * FROM users', con=engine)
print(users_df)
engine.execute('DROP TABLE IF EXISTS users')
