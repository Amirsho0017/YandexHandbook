import psycopg2
from db import conn as connection

create_users_query = '''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    chat_id Varchar(255) NOT NULL,
    joined_at timestamp default current_timestamp
);
'''

create_reports_query = '''
CREATE TABLE IF NOT EXISTS reports (
    id SERIAL PRIMARY KEY,
    date date default current_date,
    user_id VARCHAR(255) NOT NULL
);
'''

try:
    cursor = connection.cursor()

    cursor.execute(create_users_query)
    cursor.execute(create_reports_query)

    connection.commit()

except psycopg2.Error as e:
    print(f"Error: {e}")

finally:
    cursor.close()
    connection.close()
