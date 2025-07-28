import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datasets\TrafficVolumeData.csv")
print("\n Info :",df.info())
print("Description :",df.describe())
print("\n Columns :",df.columns)
print("\n Data Types :",df.dtypes)
print("\n Missing Values")
print(df.isnull().sum())
print(df.nunique())
df['date_time'] = pd.to_datetime(df['date_time'])
df['day_of_week'] = df['date_time'].dt.dayofweek

traffic_by_day = df.groupby('day_of_week')['traffic_volume'].mean().reset_index()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
traffic_by_day['day_of_week'] = traffic_by_day['day_of_week'].apply(lambda x: days[x])

plt.figure(figsize=(10, 6))
sns.barplot(data=traffic_by_day, x='day_of_week', y='traffic_volume', palette='coolwarm')
plt.title('Average Traffic Volume by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Traffic Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['date'] = pd.to_datetime(df['date_time']).dt.date
daily_traffic = df.groupby('date')['traffic_volume'].mean().reset_index()

plt.figure(figsize=(14, 6))
plt.plot(daily_traffic['date'], daily_traffic['traffic_volume'], color='blue')
plt.title('Daily Average Traffic Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Average Traffic Volume')
plt.grid(True)
plt.tight_layout()
plt.show()

df['month'] = pd.to_datetime(df['date_time']).dt.month

monthly_traffic = df.groupby('month')['traffic_volume'].mean().reset_index()

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_traffic['month_name'] = monthly_traffic['month'].apply(lambda x: month_labels[x-1])

plt.figure(figsize=(10, 6))
sns.barplot(data=monthly_traffic, x='month_name', y='traffic_volume', palette='coolwarm')
plt.title('Average Traffic Volume by Month')
plt.xlabel('Month')
plt.ylabel('Average Traffic Volume')
plt.tight_layout()
plt.show()
