import pandas as pd
import matplotlib.pyplot as plt
import random

# Read the dataset
d = pd.read_csv("college_admission.csv")

# Function to randomly select gender
def gender():
    return random.choice(d['Gender'].tolist())

# Function to simulate the counts of male, female, courses, and admission status
def sim():
    n = 1000  # Total number of applicants (assuming 1000 records)
    
    # Initialize dictionaries to store counts for gender, courses, and admission status
    gender_count = {"Male": 0, "Female": 0}
    major_count = {}
    admission_status_count = {"Admitted": 0, "Rejected": 0, "Waitlisted": 0}
    
    # Loop through n records and count occurrences of each category
    for _ in range(n):
        # Count gender
        gender_count[gender()] += 1
        
        # Count major (course applied to)
        major = random.choice(d['Major'].tolist())
        major_count[major] = major_count.get(major, 0) + 1
        
        # Count admission status
        status = random.choice(d['Admission_Status'].tolist())
        admission_status_count[status] += 1

    # Print the results
    print("Gender Distribution:")
    print(f"Male: {gender_count['Male']}")
    print(f"Female: {gender_count['Female']}")
    
    print("\nCourse Distribution:")
    for major, count in major_count.items():
        print(f"{major}: {count}")
    
    print("\nAdmission Status Distribution:")
    for status, count in admission_status_count.items():
        print(f"{status}: {count}")
    
    # Visualize the data with bar plots
    # Gender distribution plot
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.bar(gender_count.keys(), gender_count.values(), color=['blue', 'pink'])
    plt.title("Gender Distribution")
    plt.ylabel("Count")
    
    # Admission status plot
    plt.subplot(1, 2, 2)
    plt.bar(admission_status_count.keys(), admission_status_count.values(), color=['green', 'red', 'yellow'])
    plt.title("Admission Status Distribution")
    plt.ylabel("Count")

    plt.tight_layout()
