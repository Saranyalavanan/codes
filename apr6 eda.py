import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('stationery data.csv')


print(data.describe())


numerical = ["Unit Price", "Units"]


meanvalue=data[numerical].mean()
print(meanvalue)

medianvalue=data[numerical].median()
print(medianvalue)


plt.figure(figsize=(10, 6)) 
sns.lineplot(x='Units',y='Unit Price', data=data,color='brown')

plt.title('Line Plot of Unit Price vs Units')
plt.xlabel('Units')
plt.ylabel('Unit Price')

plt.show()
