import pandas as pd
import numpy as np

data = pd.read_csv("datasets\plane_crash_info.csv")
print(data.head())
grouped = data.groupby("Carrier").size()
print(grouped)
