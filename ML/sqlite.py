import sqlite3
import pandas as pd

conn = sqlite3.connect("example.db")
df = pd.read_sql("SELECT * FROM students", conn)
print(df.head())
