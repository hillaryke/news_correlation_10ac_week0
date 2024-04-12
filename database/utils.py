import psycopg2
from psycopg2 import OperationalError

def create_connection():
    connection = None

    # Database connection parameters
    dbname = 'postgres'
    user = 'news_admin'
    password = 'pass123'
    host = 'localhost'

    try:
        # Establishing the connection
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def fetch_query_results(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")