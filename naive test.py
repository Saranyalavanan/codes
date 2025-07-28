import pandas as pd
from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import HistGradientBoostingClassifier

df=pd.read_csv("MICE Loan Dataset.csv",encoding='ISO-8859-1') 

cat=["Loan_ID","Married","Education","Self_Employed","Property_Area","Loan_Status"]
label_encode=LabelEncoder()
for  c in cat:
    df[c]=label_encode.fit_transform(df[c])
    print(df[c])

num=["Dependents","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History"]
scaler=MinMaxScaler()
df[num]=scaler.fit_transform(df[num])
print(df[num])

df_encode=df.copy()
le=LabelEncoder()
df_encode["Gender"]=le.fit_transform(df_encode["Gender"])
df_encode["Loan_Status"]=le.fit_transform(df_encode["Loan_Status"])


X=df_encode.drop(["Gender","Loan_Status"],axis=1)
y=df_encode["Loan_Status"]

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

