import pandas as pd
from scipy.stats import kurtosis
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("college.csv")
numdata=data.select_dtypes(include=["number"])

kurt=numdata.apply(kurtosis)

for col,k in kurt.items():
    if k>3:
        print(col,"this is heavy tails")
    elif k<3:
        print(col,"this is light tails")
    else:
        print(col,"noraml tails") 

categories = ['Top10perc','P.Undergrad','PhD','Grad.Rate','Books','perc.alumni']
values = [10, 20,30,15, 25,35]
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['blue', 'green', 'red', 'purple','skyblue','orange'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()
