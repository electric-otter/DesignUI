import sqlite3

# Function to create a new database
def create_database(db_name):
    conn = sqlite3.connect(f'{db_name}.db')
    return conn

# Function to create a new table
def create_table(conn, table_name, columns):
    cursor = conn.cursor()
    column_defs = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})")
    conn.commit()

# Example usage
db_name = 'user_apps'
conn = create_database(db_name)

table_name = 'user_data'
columns = {
    'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
    'name': 'TEXT NOT NULL',
    'value': 'TEXT'
}
create_table(conn, table_name, columns)

# Function to insert data into a table
def insert_data(conn, table_name, data):
    cursor = conn.cursor()
    placeholders = ', '.join(['?' for _ in data])
    cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", tuple(data))
    conn.commit()

# Example usage
data = [None, 'example_name', 'example_value']
insert_data(conn, table_name, data)

# Close the connection
conn.close()
