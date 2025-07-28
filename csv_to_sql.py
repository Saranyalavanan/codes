import pandas as pd

df = pd.read_csv("datasets\management.csv")

table_name = "management"

with open("management.sql", "w") as f:
    for i, row in df.iterrows():
        values = "', '".join([str(x).replace("'", "''") for x in row])
        sql = f"INSERT INTO {table_name} VALUES ('{values}');\n"
        f.write(sql)

print("CSV converted to SQL!")
