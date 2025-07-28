import pymysql as mysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
con=mysql.connect(host="localhost",user="root",password="livewire",database="saranya")
cursor=con.cursor()

cursor.execute("select * from students")
res=cursor.fetchall()

columns=[desc[0] for desc in cursor.description]


df=pd.DataFrame(res,columns=columns)

ab=df[df["assignment_score"]>50]
be=df[df["assignment_score"]<75]

grouped = df.groupby(['department', 'gender']).size().reset_index(name='count')
print(grouped)

label=["above 50","below 50"]
counts=[len(ab),len(be)]
plt.bar(label,counts,color=["grey","lightblue"])
plt.show()

sns.barplot(data=grouped, x='department', y='count', hue='gender', palette='coolwarm')
plt.title('Student Gender Distribution per Department')
plt.xlabel('Department')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



