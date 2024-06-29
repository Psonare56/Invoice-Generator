import psycopg2

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        dbname="invoiceDB",
        user="myuser",
        password="password1612",
        host="localhost",
        port=5432
    )
    
    # Create a cursor object
    cursor = connection.cursor()
    
    # Execute a test query
    cursor.execute("SELECT version(16.3);")
    
    # Fetch the result
    db_version = cursor.fetchone()
    print(f"Connected to - {16.3}")

except Exception as error:
    print(f"Error: {error}")

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
