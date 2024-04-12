import os
from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

def create_connection():
    # Get the connection parameters from environment variables

    # host = os.getenv('DB_HOST')
    # port = os.getenv('DB_PORT')
    # dbname = os.getenv('DB_NAME')
    # user = os.getenv('DB_USER')
    # password = os.getenv('DB_PASSWORD')

    # Connection parameters
    host = "localhost"
    port = "5432"
    dbname = "postgres"
    user = "postgres"
    password = "pass123"

    # Create the connection
    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    # Create the database engine
    engine = create_engine(connection_string)

    return engine

def save_to_db(data, table_name):
    # Create the connection
    engine = create_connection()

    print("CONNECTION TO ENGINE CREATED!")

    # Save the data to the database
    data.to_sql(table_name, engine, if_exists='replace', index=False)

    # Close the connection
    engine.dispose()
