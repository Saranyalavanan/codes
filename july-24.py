import pymysql as mysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import *
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster

con=mysql.connect(host="localhost",user="root",password="livewire",database="saranya")
cursor=con.cursor()

cursor.execute("select * from students")
res=cursor.fetchall()

columns=[desc[0] for desc in cursor.description]


df=pd.DataFrame(res,columns=columns)

cat=["name","gender","department","semester"]
label_encode=LabelEncoder()
for  c in cat:
    df[c]=label_encode.fit_transform(df[c])
    print(df[c])

num=["id","midterm_score", "final_score", "assignment_score"]
scaler=MinMaxScaler()
df[num]=scaler.fit_transform(df[num])
print(df[num])

X = df.drop(["name","gender","department"],axis=1)

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

linked=linkage(X_scaled,method="ward")

ab=df[df["assignment_score"]>70]
be=df[df["assignment_score"]<70]

grouped = df.groupby(['department', 'gender']).size().reset_index(name='count')
print(grouped)

dendrogram(linked,orientation="top",distance_sort="descending")
plt.show()


label=["above 70","below 70"]
counts=[len(ab),len(be)]
plt.bar(label,counts,color=["grey","lightblue"])
plt.show()

sns.barplot(data=grouped, x='department', y='count', hue='gender', palette='coolwarm')
plt.title('Student Gender Distribution per Department')
plt.xlabel('Department')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



