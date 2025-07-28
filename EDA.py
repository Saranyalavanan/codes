import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("phone data.csv")

print(data.describe())
sns.countplot(x="network",hue="item",data=data,palette="PRGn")
plt.show()
sns.histplot(x="network",hue="network_type",data=data,palette="magma")
plt.show()
sns.boxplot(x="network",hue="item",data=data,palette="coolwarm")
plt.show()
