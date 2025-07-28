import pandas as pd
from scipy.stats import skew
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 2)

data=pd.read_csv("StudentsPerformance.csv")
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
sns.barplot(x=skewness.index,y=skewness.values,palette="coolwarm",ax=axes[0, 0])
axes[0, 0].set_title('StudentsPerformance Skewness')


data = pd.read_csv("hotel.csv")
numdata = data[["lead_time", "adults", "children", "babies"]]
skewness = numdata.apply(skew)
for col,skews in skewness.items():
    if skews>0:
      print(f"{col} is a positive skewed")
    elif skews<0:
       print(f"{col} is a negative skewed")
    else:
       print(f"{col} is normally distributted")
sns.barplot(x=skewness.index,y=skewness.values,palette="coolwarm",ax=axes[0, 1])
axes[0, 1].set_title('Hotel Skewness')


data=pd.read_csv("employee.csv")
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
sns.barplot(x=skewness.index,y=skewness.values,palette="coolwarm", ax=axes[1, 0])
axes[1, 0].set_title('Employee Skewness')


data=pd.read_csv("College.csv")
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
sns.barplot(x=skewness.index,y=skewness.values,palette="coolwarm", ax=axes[1, 1])
axes[1, 1].set_title('College Skewness')
plt.show()



