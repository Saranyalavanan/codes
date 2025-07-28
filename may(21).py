import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('datasets\marketing_campaign_dataset.csv')

print("\n Data Informations")
print(data.info())

print("\n Missing Values")
print(data.isnull().sum())

grouped = data.groupby('Company').size()
print("\n",grouped)
plt.figure(figsize=(8,5))

grouped = data.groupby('Campaign_Type').size()
print("\n",grouped)

grouped = data.groupby('Target_Audience').size()
print("\n",grouped)

grouped = data.groupby('Duration').size()
print("\n",grouped)

grouped = data.groupby('Channel_Used').size()
print("\n",grouped)

grouped = data.groupby('Location').size()
print("\n",grouped)

grouped = data.groupby('Language').size()
print("\n",grouped)

grouped = data.groupby('Engagement_Score').size()
print("\n",grouped)

grouped = data.groupby('Customer_Segment').size()
print("\n",grouped)
