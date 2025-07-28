import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv("StudentsPerformance.csv")
confidence = 0.95
n = len(data)
tdis = stats.t.ppf((1 + confidence) / 2, df=n - 1)
x = ["math score", "reading score", "writing score"]

for score in x:
    scores = data[score]
    mean = np.mean(scores)
    sem = stats.sem(scores)
    margin = tdis * sem
    l = mean - margin
    u = mean + margin

    print(f"{score}")
    print("Mean   :", mean)
    print("SEM    :", sem)
    print("TDist  :", tdis)
    print("Lower  :", l)
    print("Upper  :", u)
    print("......................................")
