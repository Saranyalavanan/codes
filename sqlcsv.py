import sqlite3
import pandas as pd
import re

# Load the original MySQL SQL file
with open("Creation Queries.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

# Remove MySQL-specific syntax: CHARACTER SET and backticks
sql_script = re.sub(r"CHARACTER SET\s+\w+", "", sql_script)
sql_script = sql_script.replace("`", "")

# Replace NUMERIC with REAL or DECIMAL
sql_script = sql_script.replace("NUMERIC", "REAL")

# Connect to in-memory SQLite DB
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Run the cleaned script
cursor.executescript(sql_script)

# Query and export to Excel
df = pd.read_sql_query("SELECT * FROM sales", conn)
df.to_excel("sales_data.xlsx", index=False)

print("Exported to Excel successfully!")
