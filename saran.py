import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("crime_data.csv")


print(df['States/UTs'])
print(df[df['District'] == 'Visakha Rural'])
print(df.iloc[0,91])

categories = ['Murder','Rape','Kidnapping & Abduction_Total','Dacoity with Murder','Robbery','Theft']
values = [60,50,40,30,20,10]
plt.figure(figsize = (8,5))
plt.bar(categories,values,color = ['blue','lightblue','purple','brown','green','lightgreen'])
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Barchart')
plt.show()
