import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('datasets\Banking.csv')

print("\n Data Informations")
print(data.info())

print("\n Missing Values")
print(data.isnull().sum())

columns = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','deposit']
for col in columns:
    print(f"\n Grouped by {col}")
    print(data.groupby(col).size())

plt.figure(figsize=(10, 6)) 
sns.barplot(x='age',y='job', data=data,palette='coolwarm')
plt.title('Bar Plot ')
plt.xlabel('age')
plt.ylabel('job')
plt.show()

plt.figure(figsize=(10, 6)) 
sns.lineplot(x='age',y='duration', data=data,color='lightblue')
plt.title('line Plot ')
plt.xlabel('age')
plt.ylabel('duration')

plt.show()
