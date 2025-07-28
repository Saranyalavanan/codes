import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random


d = pd.read_csv("college_admission.csv")
gender_list = d['Gender'].tolist()
course_list = d['Course'].tolist()
admissionstatus_list = d['Admission Status'].tolist()


def random_gender():
    return random.choice(gender_list)

def random_course():
    return random.choice(course_list)

def random_admissionstatus():
    return random.choice(admissionstatus_list)


def sim(n=1000):
    gender = {"Male": 0, "Female": 0}
    course = {}
    admissionstatus = { "Waitlisted": 0, "Enrolled": 0, "Pending": 0}

    for _ in range(n):
        g = random_gender()
        c = random_course()
        a = random_admissionstatus()

        
        if g in gender:
            gender[g] += 1
        else:
            gender[g] = 1  

        
        if c in course:
            course[c] += 1
        else:
            course[c] = 1

        
        if a in admissionstatus:
            admissionstatus[a] += 1
        else:
            admissionstatus[a] = 1

    print("~~~~ Gender ~~~~")
    print("Male:", gender["Male"])
    print("Female:", gender["Female"])

    print("~~~~ Course ~~~~",)
    for key, value in course.items():
        print(f"{key}: {value}")

    print("~~~~ Admission Status ~~~~")
    print("Waitlisted:", admissionstatus["Waitlisted"])
    print("Enrolled:", admissionstatus["Enrolled"])
    print("Pending:", admissionstatus["Pending"])

   
labels = ['Waitlisted','Enrolled','Pending']
sizes = [50,40,30]
plt.figure(figsize = (8,5))
plt.pie(sizes,labels=labels,autopct='%1.1f%%',colors=['lightblue','blue','brown'])
plt.title('pie chart')
plt.show()

sim(1000)
