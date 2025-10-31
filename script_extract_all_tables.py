#!/usr/bin/env python3
import psycopg2
import pandas as pd

# ------------------------
# PostgreSQL connection
# ------------------------
conn_params = {
    "host": "localhost",          # Docker container port mapped to host
    "port": 5432,                 # PostgreSQL port
    "database": "testdb",         # Your database name
    "user": "postgres",           # PostgreSQL user
    "password": "mysecretpassword" # Your password
}

try:
    conn = psycopg2.connect(**conn_params)
    print("Connected to PostgreSQL successfully!")
except Exception as e:
    print("Error connecting to PostgreSQL:", e)
    exit(1)

# ------------------------
# Extract tables
# ------------------------
tables = ["users", "products", "orders"]

for table in tables:
    query = f"SELECT * FROM {table};"
    try:
        df = pd.read_sql(query, conn)
        csv_file = f"{table}.csv"
        df.to_csv(csv_file, index=False)
        print(f"Table '{table}' exported to '{csv_file}' ({len(df)} rows).")
    except Exception as e:
        print(f"Error extracting table {table}:", e)

# ------------------------
# Optional: join tables (example)
# ------------------------
try:
    join_query = """
    SELECT o.id AS order_id,
           u.name AS user_name,
           u.email AS user_email,
           p.name AS product_name,
           p.price AS product_price,
           o.quantity,
           o.order_date
    FROM orders o
    JOIN users u ON o.user_id = u.id
    JOIN products p ON o.product_id = p.id;
    """
    df_join = pd.read_sql(join_query, conn)
    df_join.to_csv("orders_joined.csv", index=False)
    print(f"Joined table exported to 'orders_joined.csv' ({len(df_join)} rows).")
except Exception as e:
    print("Error joining tables:", e)

# ------------------------
# Close connection
# ------------------------
conn.close()
print("PostgreSQL connection closed.")
