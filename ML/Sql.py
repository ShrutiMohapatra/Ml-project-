import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="employees"
)

query = "SELECT * FROM emp_table"
df = pd.read_sql(query, conn)
print(df.head())