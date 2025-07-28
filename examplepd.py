import pandas as pd
import numpy as np

data = [101,102,103,104,105,106,107,108,109,110]
series = pd.Series(data, index=['A', 'B', 'C', 'D', 'E','F','G','H','I','J'])
print("Series:")
print(series)

data_dict = {
    'Name': ['Saran', 'prakash', 'suji', 'praveena', 'Sathya', 'Sarmila', 'Varshini', 'Jeni', 'Joe','Raj'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Salary': [50000, 60000, 70000, 80000, 50000, 60000, 70000, 80000,90000, 50000]
}
df = pd.DataFrame(data_dict)
print("\nDataFrame:")
print(df)

df.to_csv('saran.csv', index=False)
df_read = pd.read_csv('saran.csv')
print("\nRead CSV:")
print(df_read)

print("\nInfo:")
print(df.info())
print("\nDescription:")
print(df.describe())
print("\nColumns:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
