import pandas as pd
from sklearn.preprocessing import *
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_csv("datasets/retail_sales_dataset.csv",encoding='ISO-8859-1')
data["Date"] = pd.to_datetime(data["Date"])
cat=["Customer ID","Gender","Product Category"]
label_encode=LabelEncoder()
for  c in cat:
    data[c]=label_encode.fit_transform(data[c])

num=["Transaction ID","Age","Quantity","Price per Unit","Total Amount"]
scaler=MinMaxScaler()
data[num]=scaler.fit_transform(data[num])

X = data.drop(["Transaction ID", "Date", "Customer ID"], axis=1)

scaler = StandardScaler()
Xs = scaler.fit_transform(X)

kmean = KMeans(n_clusters=2, random_state=42)
data["cluster"] = kmean.fit_predict(Xs)
print(data)


plt.scatter(data["Price per Unit"], data["Quantity"], c=data["cluster"], cmap="Set1", s=200, edgecolors="k")
plt.colorbar(label="Cluster")
plt.xlabel("Price per Unit")
plt.ylabel("Quantity")
plt.title("Customer Clusters")
plt.show()


x = data.drop(["cluster", "Transaction ID", "Date", "Customer ID"], axis=1)
y = data["cluster"]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)
