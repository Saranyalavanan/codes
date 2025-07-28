import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from scipy import stats

data=pd.read_csv("datasets\hospital.csv")
print(data.describe())

numberical=["Procedure.Heart Attack.Cost","Procedure.Heart Failure.Cost","Procedure.Pneumonia.Cost","Procedure.Hip Knee.Cost"]

meanvalue=data[numberical].mean()
print(meanvalue)

medianvalue=data[numberical].median()
print(medianvalue)

numdata=data.select_dtypes(include=["number"])
skewness=numdata.apply(skew)
print(skewness)

for col,skews in skewness.items():
    if skews>0:
      print(f"{col} is a positive skewed")
    elif skews<0:
       print(f"{col} is a negative skewed")
    else:
       print(f"{col} is normally distributted")


sample=data["Procedure.Heart Failure.Cost"]
data["zscore"]=zscore(sample)
print(data)

numerical = ["Procedure.Heart Attack.Cost", "Procedure.Heart Failure.Cost", "Procedure.Pneumonia.Cost", "Procedure.Hip Knee.Cost"]
values = data[numerical]

mean = values.mean()
std = values.std()
z_scores = (values - mean) / std

print(mean,std,values,z_scores,sep="\n")


categories = ["Procedure.Heart Attack.Cost", "Procedure.Heart Failure.Cost", "Procedure.Pneumonia.Cost", "Procedure.Hip Knee.Cost"]
value = [50,40,30,20]
plt.figure(figsize = (8,5))
plt.bar(categories,value,color = ['blue','lightblue','grey','pink'])
plt.xlabel('categories')
plt.ylabel('values')
plt.show()

categories = ["Procedure.Heart Attack.Cost", "Procedure.Heart Failure.Cost", "Procedure.Pneumonia.Cost", "Procedure.Hip Knee.Cost"]
value = [50,40,30,20]
plt.figure(figsize = (8,5))
plt.bar(categories,value,color = ['green','lightgreen','orange','brown'])
plt.xlabel('categories')
plt.ylabel('z_scores')
plt.show()

sns.barplot(x=skewness.index,y=skewness.values,palette="coolwarm")
plt.show()






