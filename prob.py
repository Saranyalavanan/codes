import random
import matplotlib.pyplot as plt

def ball():
    value = random.randint(0,4)
    if value == 0:
        return "pink ball"
    elif value == 1:
        return "grey ball"
    elif value == 2:
        return "brown ball"
    elif value == 3:
        return "skyblue ball"
    else:
        return "violet ball"

def sim():
    n = 1000  
    result = {"pink ball": 0, "grey ball": 0, "brown ball":0,"skyblue ball":0,"violet ball": 0}

    for _ in range(n):
        result[ball()] += 1
    
    print("pink ball: ", result["pink ball"])
    print("grey ball: ", result["grey ball"])
    print("brown ball:", result["brown ball"])
    print("skyblue ball:",result["skyblue ball"])
    print("violet ball: ", result["violet ball"])

    pink_ball = result["pink ball"] / n
    grey_ball = result["grey ball"] / n
    brown_ball= result["brown ball"]/ n
    skyblue_ball= result["skyblue ball"]/ n
    violet_ball = result["violet ball"] / n

    print("pink balll (probability): ", pink_ball)
    print("grey ball (probability): ", grey_ball)
    print("brown ball(probability):",brown_ball)
    print("skyblue ball(probability):",skyblue_ball)
    print("violet ball (probability):", violet_ball)

    labels = result.keys()
    counts = result.values()
    plt.bar(labels, counts, color=["pink", "grey","brown","skyblue", "violet"])
    plt.title("Ball Color Distribution")
    plt.ylabel("Count")
    plt.show()

sim()
