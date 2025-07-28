import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("datasets/Employee data.csv", encoding='ISO-8859-1', parse_dates=["bdate"])
df = df.head(50)
# Set date as index
df.set_index("bdate", inplace=True)

# Keep only numeric columns
df = df.select_dtypes(include=[np.number])


if "jobtime" not in df.columns:
    raise ValueError("The dataset must contain a 'jobtime' column.")


for lag in range(1, 13):
    df[f"lag_{lag}"] = df["jobtime"].shift(lag)

# Drop rows with NaN (from lagging)
df.dropna(inplace=True)

# Use only lag features for prediction
lag_features = [f"lag_{i}" for i in range(1, 13)]
x = df[lag_features]
y = df["jobtime"]

# Train XGBoost Regressor
model = XGBRegressor(n_estimators=100)
model.fit(x, y)

# Forecast next 12 months
future_preds = []
last_known = df.copy()

for _ in range(12):
    input_data = last_known.iloc[-1:][lag_features].copy()

    
    for j in range(12, 1, -1):
        input_data[f"lag_{j}"] = input_data[f"lag_{j-1}"]
    input_data["lag_1"] = last_known.iloc[-1]["jobtime"]

   
    next_pred = model.predict(input_data)[0]
    future_preds.append(next_pred)

   
    new_row = pd.DataFrame({
        "jobtime": [next_pred],
        **{f"lag_{j}": input_data.iloc[0][f"lag_{j}"] for j in range(1, 13)}
    }, index=[last_known.index[-1] + pd.DateOffset(months=1)])

    last_known = pd.concat([last_known, new_row])


future_dates = pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=12, freq="M")


plt.figure(figsize=(10, 5))
plt.plot(df.index, df["jobtime"], label="Historical Sales")
plt.plot(future_dates, future_preds, label="Forecasted Sales", linestyle="--", color="red")
plt.title("12-Month Sales Forecast Using XGBoost")
plt.xlabel("bdate")
plt.ylabel("jobtime")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

