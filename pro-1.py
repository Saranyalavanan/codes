import pymysql 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

df = pd.read_csv("datasets/phone data.csv")
table_name = "phone"

columns = df.columns
create_table_sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` (\n"
for col in columns:
    create_table_sql += f"  `{col}` VARCHAR(255),\n"
create_table_sql = create_table_sql.rstrip(",\n") + "\n);\n\n"

insert_sql = ""
for _, row in df.iterrows():
    values = "', '".join([str(x).replace("'", "''") for x in row])
    insert_sql += f"INSERT INTO `{table_name}` VALUES ('{values}');\n"

with open("phone_full.sql", "w", encoding="utf-8") as f:
    f.write(create_table_sql)
    f.write(insert_sql)

print("SQL file with CREATE TABLE and INSERTs saved as 'phone_full.sql'")

conn = pymysql.connect(host='localhost', user='root', password='livewire', database='saranya')
cursor = conn.cursor()

try:
    with open('phone_full.sql', 'r') as file:
        sql_script = file.read()

    for statement in sql_script.split(';'):
        if statement.strip():
            cursor.execute(statement)

    conn.commit()
    print("SQL file executed and data inserted.")

    cursor.execute("SELECT * FROM phone")
    res = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    df = pd.DataFrame(res, columns=columns)
    df["date"] = pd.to_datetime(df["date"])

    df["month"] = pd.to_datetime(df["month"])
    df["month_year"] = df["month"].dt.year
    df["month_num"] = df["month"].dt.month
    df.drop(columns=["month"], inplace=True)

    cat = ["item", "network", "network_type"]
    for c in cat:
        le = LabelEncoder()
        df[c] = le.fit_transform(df[c])

    num = ["index", "duration"]
    scaler = MinMaxScaler()
    df[num] = scaler.fit_transform(df[num])

    
    X = df[["item", "network_type"]]
    y = df["network"]  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

    plt.figure(figsize=(10, 5))
    sns.histplot(y_pred, kde=True, color='lightblue')
    plt.title("Predicted Network Distribution")
    plt.xlabel("Predicted Network")
    plt.ylabel("Frequency")
    plt.show()



finally:
    cursor.close()
    conn.close()
