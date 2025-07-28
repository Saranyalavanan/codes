import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("datasets/supermarket.csv", encoding='ISO-8859-1')

data = data.drop(columns=["Invoice ID", "Date", "Time"])  

cat = ["Branch", "City", "Customer type", "Gender", "Product line", "Payment"]
le = LabelEncoder()
for col in cat:
    data[col] = le.fit_transform(data[col])

num = ["Unit price", "Quantity", "Tax 5%", "Total", "cogs", 
       "gross margin percentage", "gross income", "Rating"]
scaler = MinMaxScaler()
data[num] = scaler.fit_transform(data[num])

X = data.drop(["City", "Customer type"], axis=1) 
y = data["Customer type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
 
