import psycopg2

try:
    connection = psycopg2.connect(
        dbname="test2",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")