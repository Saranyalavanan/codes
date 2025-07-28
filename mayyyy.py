import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import *

data = pd.read_csv("datasets/supermarket.csv", encoding='ISO-8859-1')
data = data.head(100)
cat=["Invoice ID","Branch","City","Customer type","Gender","Product line","Date","Time","Payment","Unit price","Quantity","Tax 5%","Total","Date","Time","cogs","gross margin percentage","gross income","Rating"]
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])


X=data.drop(["gross margin percentage","Rating","City"],axis=1)
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

kmean=KMeans(n_clusters=2,random_state=42)
data["cluster"]=kmean.fit_predict(X)
print(data)

plt.scatter(data["City"],data["Total"],c=data["cluster"],cmap="Set1",s=200,edgecolors="k")
plt.colorbar(label="Cluster")
plt.show()
