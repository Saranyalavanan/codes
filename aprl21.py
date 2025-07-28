import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

d = pd.read_csv("datasets\Adm.csv")

x = input("Do you want to check  admission status? (yes/no): ")
if x == "yes":
   course = input("Enter course name: ")

user_data = d[d['Name'] == course]
if not user_data.empty:
 for index, row in user_data.iterrows():
                print("\n Admission Details:")
                print(f"Course: {row['Course']}")
                print(f"Waitlisted: {row['Admission Status']}")
                print(f"Pending: {row['Admission Status']}")
                print(f"Enrolled:{row['Admission Status']}")
else:
 print("Sorry, no record found with that name.")



