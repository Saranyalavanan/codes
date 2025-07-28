import pymysql as mysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

con=mysql.connect(host="localhost",user="root",password="livewire",database="saranya")
cursor=con.cursor()

cursor.execute("select * from students")
res=cursor.fetchall()

columns=[desc[0] for desc in cursor.description]


df=pd.DataFrame(res,columns=columns)

X=df[["midterm_score", "final_score", "assignment_score"]]
y=df["final_score"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print(y_test,y_pred)

print(mean_squared_error(y_test,y_pred))

plt.figure(figsize=(10,5))
sns.histplot(y_pred, kde=True, color='lightblue')
plt.title("student final score")
plt.xlabel("Predicted Grades")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, color='lightblue', edgecolors='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--', lw=2)  
plt.xlabel('Predicted Grades')
plt.ylabel('Frequency')
plt.title('Scatter plot of student final score')
plt.show()

