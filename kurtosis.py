import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import kurtosis
import seaborn as sns
csvfiles = ("College.csv", "employee.csv", "hospital.csv", "hotel.csv", "StudentsPerformance.csv")

for file in csvfiles:
    df = pd.read_csv(file)
    numdata = df.select_dtypes(include=["number"])
    kurt = numdata.apply(kurtosis)      

    for col, k in kurt.items():
     if k > 3:
        print(col, "this is heavy tails")
     elif k < 3:
        print(col, "this is light tails")
     else:
        print(col, "normal tails")


labels = ['Heavy Tails', 'Light Tails', 'Normal Tails']
sizes = [50,40,30]
plt.figure(figsize=(6, 6))
colors = ['red', 'blue', 'green']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'blue','green'])
plt.title(f"Kurtosis Tail Distribution - {file}")
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(numdata[col], bins=30, color="skyblue")
plt.title("Distribution in Kurtosis")
plt.xlabel(col)
plt.ylabel("Density")
plt.tight_layout()
plt.show()
