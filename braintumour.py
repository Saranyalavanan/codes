import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("datasets/brain_tumor_dataset.csv")

print("\n Data Informations")
print(df.info())

print("\n Missing Values")
print(df.isnull().sum())

columns = ["Tumor Type","Location","Size (cm)","Grade","Patient Age","Gender"]
for col in columns:
    print(f"\n Grouped by {col}")
    print(df.groupby(col).size())

plt.figure(figsize=(10, 6)) 
sns.countplot(x='Tumor Type', hue='Gender', data=df, palette='coolwarm')
plt.title('count Plot ')
plt.xlabel('Tumor Type')
plt.ylabel('Gender')
plt.show()

cat=["Tumor Type","Location","Grade","Gender"]
label_encode=LabelEncoder()
for  c in cat:
    df[c]=label_encode.fit_transform(df[c])
   
df_encode=df.copy()
le=LabelEncoder()
df_encode["Gender"]=le.fit_transform(df_encode["Gender"])
df_encode["Tumor Type"]=le.fit_transform(df_encode["Tumor Type"])

X=df_encode.drop(["Gender","Tumor Type"],axis=1)
y=df_encode["Tumor Type"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print("\nAccuracy ==>",accuracy)
