import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="testdb",
    user="postgres",
    password="mysecretpassword"
)

df_users = pd.read_sql("SELECT * FROM users LIMIT 10;", conn)
print(df_users)

conn.close()
