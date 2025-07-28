import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("D:/SARANYA DATASCIENCE/datasets/employee_supervised_dataset.csv")

print("\n Data Informations")
print(df.info())

print("\n Missing Values")
print(df.isnull().sum())

cat=["Department","Attrition"]
label_encode=LabelEncoder()
for  c in cat:
    df[c]=label_encode.fit_transform(df[c])
    print(df[c])

df_encode=df.copy()
le=LabelEncoder()
df_encode["Department"]=le.fit_transform(df_encode["Department"])
df_encode["YearsAtCompany"]=le.fit_transform(df_encode["YearsAtCompany"])


X=df_encode.drop(["Department","YearsAtCompany"],axis=1)
y=df_encode["YearsAtCompany"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print("\nAccuracy ==>",accuracy)

plt.figure(figsize=(6, 4))
sns.countplot(x='YearsAtCompany', data=df_encode, palette='coolwarm')
plt.title('Countplot (YearsAtCompany)')
plt.xlabel('Years at Company')
plt.ylabel('Count')
plt.tight_layout()
plt.show()






