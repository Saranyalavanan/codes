import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import HistGradientBoostingClassifier
from scipy.stats import skew

data = pd.read_csv("datasets/Banking.csv",encoding='ISO-8859-1') 


cols = {
    1: 'age', 2: 'job', 3: 'marital', 4: 'education', 5: 'default',
    6: 'balance', 7: 'housing', 8: 'loan', 9: 'contact', 10: 'day',
    11: 'month', 12: 'duration', 13: 'campaign', 14: 'pdays',
    15: 'previous', 16: 'poutcome', 17: 'deposit'
}

x = int(input("Enter your choice (1-17): "))
if x in cols:
    col = cols[x]
    grouped = data.groupby(col).size()
    print(grouped)
    grouped.plot(kind='bar', figsize=(8,4), title=f'Count by {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.show()
else:
    print("Invalid choice")

cat=['job','marital','education','default', 'housing','loan','contact','month','poutcome','deposit']
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])
    print(data[c])

num=["age","balance","day","duration","campaign","pdays","previous"]
scaler=MinMaxScaler()
data[num]=scaler.fit_transform(data[num])
print(data[num])


data_encode=data.copy()
le=LabelEncoder()
data_encode["education"]=le.fit_transform(data_encode["education"])
data_encode["housing"]=le.fit_transform(data_encode["housing"])


X=data_encode.drop(["education","housing"],axis=1)
y=data_encode["housing"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model = HistGradientBoostingClassifier()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print("\nAccuracy ==>",accuracy)

model=HistGradientBoostingClassifier()
model.fit(X,y)

ypred=model.predict(X)
print(ypred)
accuracy=accuracy_score(y,ypred)
print(accuracy)
    
    

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



