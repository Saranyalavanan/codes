import pandas as pd
import numpy as np


product_ids = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
product_series = pd.Series(product_ids, index=['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10'])
print("Product Series:")
print(product_series)


data = {
    'Name': ['saran', 'prakash', 'suji', 'sathya', 'lavanya', 'prem', 'gopi', 'deni', 'guna', 'jama'],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Camera', 'Smartwatch', 'Monitor', 'Keyboard', 'Mouse', 'Speaker'],
    'Quantity': [2, 3, 1, 5, 2, 4, 3, 6, 2, 1],
    'GST (%)': [18, 18, 12, 18, 18, 18, 18, 18, 18, 18],
    'Actual Price': [50000, 30000, 20000, 15000, 25000, 10000, 20000, 5000, 3000, 7000],
    'Selling Price': [59000, 35400, 22400, 17700, 29500, 11800, 23600, 5900, 3540, 8260]
}

df = pd.DataFrame(data)
print("\nShopping Mall DataFrame:")
print(df)

df.to_csv('saranya', index=False)
df_read = pd.read_csv('saranya.csv')
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
