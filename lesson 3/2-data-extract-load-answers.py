# Question: How do you read data from a sqlite3 database and write to a DuckDB database?

# Extract: Read data from a sqlite3 database
# Load: Write data to a DuckDB database

import sqlite3
import duckdb

# Connect to the sqlite3 database
sqlite_conn = sqlite3.connect('path/to/sqlite.db')
sqlite_cursor = sqlite_conn.cursor()

# Connect to the DuckDB database
duckdb_conn = duckdb.connect(database='path/to/duckdb.db')
duckdb_cursor = duckdb_conn.cursor()

# Read data from the sqlite3 database
sqlite_cursor.execute('SELECT * FROM employees')
data = sqlite_cursor.fetchall()

# Write data to the DuckDB database
duckdb_cursor.executemany('INSERT INTO cutomers VALUES (?, ?, ...)', data)
duckdb_conn.commit()

# Close the connections
sqlite_cursor.close()
sqlite_conn.close()
duckdb_cursor.close()
duckdb_conn.close()