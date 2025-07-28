import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets\social_media_engagement1.csv")

col = ({"platform","post_type","likes","comments","shares","post_day","sentiment_score"})
for columns in col:
    print(f"\n Grouped by {columns}")
    print(df.groupby(columns).size())

print("\n Data Informations")
print(df.info())

print("\n Missing Values")
print(df.isnull().sum()


 
