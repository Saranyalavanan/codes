import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('provisional.csv')

data['Period'] = pd.to_datetime(data['Period'])  
sales_trend = data.groupby('Period')['Subject'].sum()  


plt.plot(sales_trend, marker='o', linestyle='-', color='b')
plt.title('Period by Subject')
plt.xlabel('Subject')
plt.ylabel('Period')
plt.xticks(rotation=45)
plt.grid()
plt.show()

