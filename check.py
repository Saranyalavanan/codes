import pandas as pd
import numpy as np

d = pd.read_csv("college_admission.csv")
check = input("Do you want to check your admission status? (yes/no): ")
if check == "yes":
   user_name = input("Enter your full name: ")

       
if 'Name' not in d.columns:
     print("The dataset does not contain a 'Name' column.")


user_data = d[d['Name'] == user_name]
if not user_data.empty:
 for index, row in user_data.iterrows():
                print("\n Admission Details:")
                print(f"Name: {row['Name']}")
                print(f"Course: {row['Course']}")
                print(f"Gender: {row['Gender']}")
                print(f"Admission Status: {row['Admission Status']}")
else:
 print("Sorry, no record found with that name.")
