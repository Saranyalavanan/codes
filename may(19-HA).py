import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster
from sklearn.preprocessing import *

data = pd.read_csv("datasets/supermarket.csv", encoding='ISO-8859-1')

data_duplicate = pd.DataFrame([data.iloc[0], data.iloc[99]])
print("\nDataFrame with Duplicates:")
print(data_duplicate.duplicated())
print("\nAfter Dropping Duplicates:")
print(data_duplicate.drop_duplicates())

data = data.head(100)
cat=(data)
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])
    print(data[c])

X=data.drop(["Invoice ID","Date","Time","Branch","Tax 5%"],axis=1)
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

linked=linkage(X_scaled,method="ward")

kmean=KMeans(n_clusters=2,random_state=42)
data["cluster"]=kmean.fit_predict(X)
print(data)

dendrogram(linked,orientation="top",distance_sort="descending")
plt.show()

plt.scatter(data["Branch"],data["Rating"],c=data["cluster"],cmap="Set1",s=200,edgecolors="k")
plt.colorbar(label="Cluster")
plt.show()
