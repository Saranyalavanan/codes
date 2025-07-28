import pandas as pd
import matplotlib.pyplot as plt
import random
d = pd.read_csv("datasets\Adults.csv")
gender_list = d['sex'].tolist()
def sex():
     return random.choice(gender_list)
def sim():
    n = 1000
    result = {"Male": 0, "Female": 0}
    
    for _ in range(n):
        result[sex()] += 1
    
    print("Male :", result["Male"])
    print("Female :", result["Female"])

    Male_prob = result["Male"] / n
    Female_prob = result["Female"] / n
    
    print("Male prob :", Male_prob)
    print("Female prob :", Female_prob)

    labels = list(result.keys())
    counts = list(result.values())
    
    plt.bar(labels, counts, color=["skyblue", "pink"])
    plt.title("Simulated Gender Distribution")
    plt.ylabel("Count")
    plt.show()

sim()
