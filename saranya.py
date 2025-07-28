import pandas as pd
from sklearn.preprocessing import *
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv("datasets\Admission_Predict.csv",encoding='ISO-8859-1')
X=data.drop(["Research","SOP","LOR "],axis=1)

scaler=StandardScaler()
Xs=scaler.fit_transform(X)

X.to_csv('Admission_Predict.csv', index=False)
data_read = pd.read_csv('Admission_Predict.csv')

kmean=KMeans(n_clusters=2,random_state=42)
data["cluster"]=kmean.fit_predict(Xs)
print(data_read)

x=data[["Serial No.","GRE Score","TOEFL Score","University Rating","CGPA","Chance of Admit "]]
y=data["cluster"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print("\nAccuracy : ",accuracy)

