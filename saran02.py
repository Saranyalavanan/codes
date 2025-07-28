import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('hospital.csv')
print("\nRead CSV:")
print(df)
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='sin Wave', color='brown', linestyle='-', linewidth=2)
plt.xlabel('Facility Type')  
plt.ylabel('Pneumonia Procedure Cost')  
plt.title('Line Plot')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df['Facility.Type'], df['Procedure.Heart Failure.Cost'],color=['blue', 'green', 'red', 'purple','pink']) 
plt.xlabel('Facility Type')
plt.ylabel('Heart Failure Procedure Cost')
plt.title('Bar Chart')
plt.show()

labels = ['Government', 'Proprietary', 'Private', 'Church','Unknown']
sizes = [50,40, 30, 20, 10]
plt.figure(figsize=(8, 5))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'blue', 'red', 'green','pink'])
plt.title('Pie Chart')
plt.show()

plt.figure(figsize=(8, 5))
plt.stem(df['Facility.Type'], df['Procedure.Pneumonia.Cost'], linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Stem Plot ')
plt.xlabel('Facility Type')
plt.ylabel('Pneumonia Procedure Cost')
plt.show()

plt.figure(figsize=(12, 10))
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Line Plot')
plt.subplot(2, 2, 2)
plt.bar(df['Facility.Type'], df['Procedure.Heart Failure.Cost']); plt.title('Bar Chart')
plt.subplot(2, 2, 3)
plt.pie([50, 40, 30, 20, 10], labels=['Gov', 'Prop', 'Priv', 'Church', 'Unknown'])
plt.title('Pie Chart')
plt.subplot(2, 2, 4); plt.stem(df['Facility.Type'], df['Procedure.Pneumonia.Cost'])
plt.title('Stem Plot')
plt.tight_layout()
plt.show()

