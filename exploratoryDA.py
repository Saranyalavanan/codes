import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('stationery data.csv')


mean_values = {
    'Metric': ['Unit Price', 'Units'],
    'Mean': [data['Unit Price'].mean(), data['Units'].mean()]
}


mean_df = pd.DataFrame(mean_values)


plt.figure(figsize=(8, 6))
sns.barplot(x='Metric', y='Mean', data=mean_df, palette='viridis')


plt.title('Mean Values of Unit Price and Units')
plt.xlabel('Metric')
plt.ylabel('Mean')

plt.show()
