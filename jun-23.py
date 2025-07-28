from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("datasets/fetal_health.csv")
X=df.drop(columns=["histogram_tendency"])
# print(X)

xs=StandardScaler().fit_transform(X)
print(xs)

pca=PCA(n_components=2)
xp=pca.fit_transform(xs)
print(xp)

plt.scatter(xp[:,0],xp[:,1])
plt.show()
