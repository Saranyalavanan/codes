import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv("datasets/management.csv") 

cat=["type_school","school_accreditation","gender","interest","residence","parent_was_in_college","will_go_to_college"]
label_encode=LabelEncoder()
for  c in cat:
    df[c]=label_encode.fit_transform(df[c])
    print(df[c])

df_encode=df.copy()
le=LabelEncoder()
df_encode["type_school"]=le.fit_transform(df_encode["type_school"])
df_encode["will_go_to_college"]=le.fit_transform(df_encode["will_go_to_college"])


X=df_encode.drop(["type_school","will_go_to_college"],axis=1)
y=df_encode["will_go_to_college"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print("\nAccuracy ==>",accuracy)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df=pd.read_csv("datasets/management.csv")

x=df[['parent_age','parent_salary','house_area','average_grades']]
y=df["average_grades"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print(y_test,y_pred)

print(mean_squared_error(y_test,y_pred))



