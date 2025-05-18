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

# Cloud storage
# Question: How do you read data from the S3 location given below and write the data to a DuckDB database?
# Data source: https://docs.opendata.aws/noaa-ghcn-pds/readme.html station data at path "csv.gz/by_station/ASN00002022.csv.gz"
# Hint: Use boto3 client with UNSIGNED config to access the S3 bucket
# Hint: The data will be zipped you have to unzip it and decode it to utf-8

# My solution
import boto3
import gzip
import io
import csv
import duckdb

# Initialize Boto3 client
s3_client = boto3.client('s3', config=boto3.session.Config(signature_version=boto3.UNSIGNED))

# Bucket and object key
bucket_name = 'noaa-ghcn-pds'
object_key = 'csv.gz/by_station/ASN00002022.csv.gz'

# Download the gzip file from S3
obj = s3_client.get_object(Bucket=bucket_name, Key=object_key)
with io.BytesIO(obj['Body'].read()) as file_stream:0
    with gzip.open(file_stream, 'rt', encoding='utf-8') as gzip_file:
        reader = csv.reader(gzip_file)
        
        # Assuming you have a DuckDB connection established as `duckdb_conn`
        # and your table schema matches the CSV structure
        duckdb_cursor = duckdb_conn.cursor()
        
        # Iterate over the CSV rows and insert into DuckDB
        for row in reader:
            # Transform row if necessary to match DuckDB table schema
            duckdb_cursor.execute('INSERT INTO salary VALUES (?, ?, ...)', row)
        
        # Commit changes
        duckdb_conn.commit()

# Close the cursor and connection
duckdb_cursor.close()
duckdb_conn.close()


# Provide solution
import csv
import gzip
from io import StringIO

import boto3
import duckdb
from botocore import UNSIGNED
from botocore.client import Config

# AWS S3 bucket and file details
bucket_name = "noaa-ghcn-pds"
file_key = "csv.gz/by_station/ASN00002022.csv.gz"
# Create a boto3 client with anonymous access
s3_client = boto3.client("s3", config=Config(signature_version=UNSIGNED))

# Download the CSV file from S3
response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
compressed_data = response["Body"].read()

# Decompress the gzip data
csv_data = gzip.decompress(compressed_data).decode("utf-8")

# Read the CSV file using csv.reader
csv_reader = csv.reader(StringIO(csv_data))
data = list(csv_reader)
# Connect to the DuckDB database (assume WeatherData table exists)
duckdb_conn = duckdb.connect("duckdb.db")

# Insert data into the DuckDB WeatherData table
insert_query = """
INSERT INTO WeatherData (id, date, element, value, m_flag, q_flag, s_flag, obs_time)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

duckdb_conn.executemany(insert_query, data[:100000])

# Commit and close the connection
duckdb_conn.commit()
duckdb_conn.close()

# API
# Question: How do you read data from the CoinCap API given below and write the data to a DuckDB database?
# URL: "https://api.coincap.io/v2/exchanges"
# Hint: use requests library

# My solution
import requests
import duckdb

# Step 2: Fetch data from the API
response = requests.get("https://api.coincap.io/v2/exchanges")
data = response.json()['data']  # Step 3: Parse the JSON response

# Step 4: Connect to DuckDB
conn = duckdb.connect('exchanges.db')

# Step 5: Create a table (assuming data structure is known and consistent)
conn.execute("""
CREATE TABLE IF NOT EXISTS exchanges (
    id VARCHAR,
    name VARCHAR,
    rank INTEGER,
    percentTotalVolume DECIMAL,
    volumeUsd DECIMAL,
    tradingPairs INTEGER,
    socket BOOLEAN,
    exchangeUrl VARCHAR,
    updated INTEGER
)
""")

# Step 6: Insert data into the table
for exchange in data:
    conn.execute("""
    INSERT INTO exchanges (id, name, rank, percentTotalVolume, volumeUsd, tradingPairs, socket, exchangeUrl, updated)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (exchange['id'], exchange['name'], exchange['rank'], exchange['percentTotalVolume'], exchange['volumeUsd'], exchange['tradingPairs'], exchange['socket'], exchange['exchangeUrl'], exchange['updated']))

# Step 7: Commit changes and close the connection
conn.commit()
conn.close()