import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram,linkage,fcluster

data=pd.read_csv("datasets/114_congress.csv")
X=data.drop(["name","party","state"],axis=1)

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

linked=linkage(X_scaled,method="ward")
dendrogram(linked,orientation="top",distance_sort="descending")
plt.show()
