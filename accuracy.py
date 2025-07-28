import pandas as pd
from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


df=pd.read_csv("management.csv") 

cat=["type_school","school_accreditation","gender","interest","residence","parent_was_in_college","will_go_to_college"]
label_encode=LabelEncoder()
for  c in cat:
    df[c]=label_encode.fit_transform(df[c])
    print(df[c])

num=["parent_age","parent_salary","house_area","average_grades"]
scaler=MinMaxScaler()
df[num]=scaler.fit_transform(df[num])
print(df[num])

df_encode=df.copy()
le=LabelEncoder()
df_encode["type_school"]=le.fit_transform(df_encode["type_school"])
df_encode["will_go_to_college"]=le.fit_transform(df_encode["will_go_to_college"])


X=df_encode.drop(["type_school","will_go_to_college"],axis=1)
y=df_encode["will_go_to_college"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print("\nAccuracy ==>",accuracy)

model=GaussianNB()
model.fit(X,y)

ypred=model.predict(X)
print(ypred)
accuracy=accuracy_score(y,ypred)
print(accuracy)

