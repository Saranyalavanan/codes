import pandas as pd
def data():
   data = {
        'Name': [],
        'Product name': [],
        'GST (%)': [],
        'Selling Price': [],
        'Quantity': [],
        'Actual Price': []
    }

   entries = int(input("Enter the number of shopping entries you want to add: "))

for i in range(entries):
        print(f"\nEnter details for entry {i+1}:")
        
        name = input("Name: ")
        product = input("Product name: ")
        quantity = int(input("Quantity: "))     
        gst = float(input("GST (%): "))
        actual_price = float(input("Actual Price: "))   
        selling_price = float(input("Selling Price: "))
   return pd.DataFrame(data)
df = data()
print("\nShopping Mall DataFrame:")
print(df)
print("\nInfo:")
print(df.info())
print("\nDescription:")
print(df.describe())
print("\nColumns:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
