import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("datasets/Baby.csv", encoding='ISO-8859-1')
df = df.head(500)

for rating in sorted(df['rating'].unique(), reverse=True):
    filtered_df = df[df['rating'] == rating][['name', 'rating', 'review']]
    filename = f"D:/SARANYA DATASCIENCE/datasets/rating_{rating}.csv"
    filtered_df.to_csv(filename, index=False)
    print(f"Saved: {filename}")

data = pd.read_csv("datasets/rating_5.csv")
cat = (data)

label_encode = LabelEncoder()
for c in cat:
    data[c] = label_encode.fit_transform(data[c])
    print(data[c])

data_encode = data.copy()
le = LabelEncoder()
data_encode["review"] = le.fit_transform(data_encode["review"])
data_encode["name"] = le.fit_transform(data_encode["name"])

X = data_encode.drop(["review", "name"], axis=1)
y = data_encode["name"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy ==>", accuracy)

df['name'] = LabelEncoder().fit_transform(df['name'])
df['review'] = LabelEncoder().fit_transform(df['review'])

X = df[['name', 'review']]
y = df["rating"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_test, y_pred)

print(mean_squared_error(y_test, y_pred))

# Scatter plot: Actual vs Predicted Ratings
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.title("Actual vs Predicted Ratings")
plt.xlabel("Actual Rating")
plt.ylabel("Predicted Rating")
plt.grid(True)
plt.tight_layout()
plt.show()

