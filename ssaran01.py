import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df= pd.read_csv('ss.csv')
df.to_csv('ss.csv', index=False)
print("\nRead CSV:")
print(df)

plt.figure(figsize=(16, 8))
plt.bar(df['EMPLOYEE_ID'], df['SALARY'], color=['blue', 'green', 'red', 'purple', 'orange', 'pink', 'violet', 'yellow', 'brown', 'grey'], label='salary')
plt.ylabel('salary')
plt.title('Bar Chart of salary by Employee Id')
plt.show()


plt.scatter(df['EMPLOYEE_ID'], df['SALARY'], color='green')
plt.xlabel('Employee Id')
plt.ylabel('Salary')
plt.title('Salary vs. Employee Id')
plt.show()


df_sorted = df.sort_values(by='EXPERIENCE')

                             
plt.plot(df_sorted['EMPLOYEE_ID'], df_sorted['SALARY'], marker='o', color='red')
plt.xlabel('Employee Id')
plt.ylabel('Salary')
plt.title('Salary Trend across Employees')
plt.show()
