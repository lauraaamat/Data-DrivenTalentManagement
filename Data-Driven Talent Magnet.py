# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:59:03 2024

@author: Anca
"""

#Import libraries
import numpy as np
import pandas as pd

# Load the dataset 
employee_data = pd.read_csv(r"C:\Users\Anca\Python work\HR_data_set.csv")



#Mosaic Plot to analyze employee demographics,  gender & department, 
# compare recruitment sources and hiring outcomes

#Import libraries
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

# Load the dataset 
employee_data = pd.read_csv("C:\\Users\\Anca\\Python work\\HR_data_set.csv")


# Create the mosaic plot
plt.figure(figsize=(10, 6))
mosaic(employee_data, ['Gender', 'Department'], title='Mosaic Plot: Gender vs. Department')
plt.show()
# Creating a treemap using Python
#Import libraries
import pandas as pd
import squarify
import matplotlib.pyplot as plt

# Load the dataset 
employee_data = pd.read_csv("C:\\Users\\Anca\\Python work\\HR_data_set.csv")

# Calculate the department sizes
department_sizes = employee_data['Department'].value_counts()

# Create labels for each department
labels = department_sizes.index
# Create treemap
plt.figure(figsize=(10, 6))
ax= squarify.plot(sizes=department_sizes, label=labels, alpha=0.7)
# Annotate each square with the number of employees
for i, label in enumerate(labels):
    x, y, dx, dy = ax.patches[i].get_bbox().bounds
    plt.text(x+dx/2, y+dy/3 , f'{department_sizes[i]}', va='center', ha='center', fontsize=12, fontweight='bold')

plt.axis('off')
plt.title('Employee Breakdown by Department (Treemap)')
plt.show()
# Creating a heatmap using Python
#Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset 
employee_data = pd.read_csv("C:\\Users\\Anca\\Python work\\HR_data_set.csv")

# Select the columns for analysis
columns_to_analyze = ['Satisfaction Rate (%)','Tenure','EngagementScore','Productivity (%)','Salary']

# Create a correlation matrix
correlation_data = employee_data[columns_to_analyze].corr()

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_data, annot=True, cmap='YlGnBu', fmt='.2f', cbar=True)
plt.title('Correlation Heatmap of Employee Metrics')
plt.show()





# Creating a box plot using Python
#Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset 
employee_data = pd.read_csv("C:\\Users\\Anca\\Python work\\HR_data_set.csv")

# Create a box plot of employee performance ratings by department
plt.figure(figsize=(12, 6))
sns.boxplot(data=employee_data, x='Department', y='EngagementScore', palette='Set2')
plt.xlabel('Department')
plt.ylabel('Engagement Score')
plt.title('Engagement Score by Department (Box Plot)')
plt.xticks(rotation=45)
plt.show()








# Creating a stacked bar chart using Python
#Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset 
employee_data = pd.read_csv("C:\\Users\\Anca\\Python work\\HR_data_set.csv")

# Create a stacked bar chart to visualize recruitment source distribution by department
recruitment_data = employee_data.groupby(['Department', 'Recruitment Source']).size().unstack(fill_value=0)
recruitment_data.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Paired')
plt.xlabel('Department')
plt.ylabel('Count')
plt.title('Recruitment Source Distribution by Department (Stacked Bar Chart)')
plt.xticks(rotation=45)
plt.legend(title='Recruitment Source', loc='upper right')
plt.show()








import pandas as pd

# Load the dataset
employee_data = pd.read_csv("C:\\Users\\Anca\\Python work\\HR_data_set.csv")

# Filter data
high_salary = employee_data[employee_data["Salary"] > 100000]

# Create a DataFrame for high-salary employees and their departments
high_salary_df = high_salary[["Department", "Salary"]]

# Visualize the distribution of high-salary employees across departments
plt.figure(figsize=(12, 6))
plt.title('High-Salaried vs. Departments')
sns.barplot(x=high_salary_df["Department"], y=high_salary_df["Salary"])
plt.show()









#Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset 
employee_data = pd.read_csv("C:\\Users\\Anca\\Python work\\HR_data_set.csv")

# Calculate average salary function
def calculate_average_salary(data, gender):
    filtered_data = [entry['Salary'] for index, entry in data.iterrows() if entry['Gender'] == gender]
    if filtered_data:
        return sum(filtered_data) / len(filtered_data)
    else:
        return 0

# Create pie chart function
def create_pie_chart(average_salary_male, average_salary_female):
    labels = ['Male', 'Female']
    average_salaries = [average_salary_male, average_salary_female]

    plt.pie(average_salaries, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Average Salary Comparison (Male vs Female)')
    plt.show()

average_salary_male = calculate_average_salary(employee_data, 'Male')
average_salary_female = calculate_average_salary(employee_data, 'Female')
create_pie_chart(average_salary_male, average_salary_female)

