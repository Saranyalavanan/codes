import pandas as pd
import matplotlib.pyplot as plt
import random
d = pd.read_csv("StudentsPerformance.csv")
gender_list = d['gender'].tolist()
def gender():
     return random.choice(gender_list)
def sim():
    n = 1000
    result = {"male": 0, "female": 0}
    
    for _ in range(n):
        result[gender()] += 1
    
    print("male :", result["male"])
    print("female :", result["female"])

    male_prob = result["male"] / n
    female_prob = result["female"] / n
    
    print("male prob :", male_prob)
    print("female prob :", female_prob)

    labels = list(result.keys())
    counts = list(result.values())
    
    plt.bar(labels, counts, color=["skyblue", "pink"])
    plt.title("Simulated Gender Distribution")
    plt.ylabel("Count")
    plt.show()

sim()
