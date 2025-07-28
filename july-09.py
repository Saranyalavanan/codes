import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

data = pd.read_csv("random.csv", encoding='ISO-8859-1')


cat = ["product", "branch"]
label_encode = LabelEncoder()
for c in cat:
    data[c] = label_encode.fit_transform(data[c])


num = ["randomnumbers"]
scaler = MinMaxScaler()
data[num] = scaler.fit_transform(data[num])


X = data.drop(["randomnumbers"], axis=1)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


linked = linkage(X_scaled, method="ward")
dendrogram(linked, orientation="top", distance_sort="descending")
plt.title("Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()
