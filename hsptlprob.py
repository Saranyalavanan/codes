import pandas as pd
import matplotlib.pyplot as plt
import random
d = pd.read_csv("Disease_dataset.csv")
disease_list = d['Disease'].tolist()
def Disease():
     return random.choice(disease_list)
def sim():
    n = 1000
    result = {"Influenza": 0, "Common Cold": 0, "Eczema":0, "Asthma":0, "Hyperthyroidism":0, "Allergic Rhinitis":0,}
    
    for _ in range(n):
        result[Disease()] += 1
    
    print("Influenza :", result["Influenza"])
    print("Common Cold :", result["Common Cold"])
    print("Eczema :",result["Eczema"])
    print("Asthma :",result["Asthma"])
    print("Hyperthyroidism :",result["Hyperthyroidism"])
    print("Allergic Rhinitis :",result["Allergic Rhinitis"])

    Influenza_prob = result["Influenza"] / n
    Common_Cold_prob = result["Common Cold"] / n
    Eczema_prob = result["Eczema"] / n
    Asthma_prob = result["Asthma"] / n
    Hyperthyroidism_prob = result["Hyperthyroidism"] / n
    Allergic_Rhinitis_prob = result["Allergic Rhinitis"] / n
    
    print("Influenza prob :", Influenza_prob)
    print("Common Cold prob :", Common_Cold_prob)
    print("Eczema prob :", Eczema_prob)
    print("Asthma prob :", Asthma_prob)
    print("Hyperthyroidism prob :",Hyperthyroidism_prob)
    print("Allergic Rhinitis prob :",Allergic_Rhinitis_prob)

    labels = list(result.keys())
    counts = list(result.values())
    
   

    labels = ['Influenza', 'Common Cold', 'Eczema', 'Asthma', 'Hyperthyroidism', 'Allergic Rhinitis']
    sizes = [60,50,40, 30, 20, 10]
    plt.pie(sizes,labels=labels, autopct='%1.1f%%', colors=["skyblue", "pink", "gold", "orange", "violet", "blue"])
    plt.title('Simulation of Disease Distribution')
    plt.show()


sim()
