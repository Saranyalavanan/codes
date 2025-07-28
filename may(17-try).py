import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("datasets\OfficeSupplies.csv")

print(data.head())

Reg=data["Region"].unique()
print(Reg)

Itemvalue=data["Item"].value_counts()
print(Itemvalue)

Itemvalue.plot()
plt.show() 

data['OrderDate'] = pd.to_datetime(data['OrderDate'])

daily_Units = data.groupby('OrderDate')['Units'].sum()
print(daily_Units)
plt.figure(figsize=(10, 4))
daily_Units.plot(kind='line', marker='o',color='brown')
plt.title("Daily Total Units")
plt.xlabel("bdate")
plt.ylabel("Units")
plt.grid(True)
plt.tight_layout()
plt.show()

data['Month'] = data['OrderDate'].dt.to_period('M')
monthly_Units = data.groupby('Month')['Units'].sum()
print(monthly_Units)
plt.figure(figsize=(8, 4))
monthly_Units.plot(kind='pie',color='salmon')
plt.title("Monthly Total Units")
plt.xlabel("Month")
plt.ylabel("Units")
plt.tight_layout()
plt.show()

data['Yearly'] = data['OrderDate'].dt.to_period('Y')
yearly_UnitPrice = data.groupby('Yearly')['Unit Price'].sum()
print(yearly_UnitPrice)
plt.figure(figsize=(8, 4))
yearly_UnitPrice.plot(kind='bar',color=['steelblue', 'skyblue'])
plt.title("Yearly Total Unit Price")
plt.xlabel("Year")
plt.ylabel("Unit Price")
plt.tight_layout()
plt.show()
