import psycopg2

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        dbname="invoicedb",
        user="myuser",
        password="password1612",
        host="localhost",
        port="5432"
    )
    
    # Create a cursor object
    cursor = connection.cursor()
    
    # Execute a test query to get the PostgreSQL server version
    cursor.execute("SELECT version();")
    
    # Fetch the result
    db_version = cursor.fetchone()
    print(f"Connected to PostgreSQL server version: {db_version[0]}")

except psycopg2.Error as e:
    print(f"Error: Connection to PostgreSQL server failed - {e}")

finally:
    # Close the cursor and connection
    try:
        if 'connection' in locals():
            if connection:
                connection.close()
                print("PostgreSQL connection is closed")
        if 'cursor' in locals():
            if cursor:
                cursor.close()
    except psycopg2.Error as e:
        print(f"Error: Failed to close connection - {e}")
