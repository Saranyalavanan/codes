import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

data=pd.read_csv("saran.csv")
sample=data["Salary"]

data["zscore"]=zscore(sample)
print(data) 
