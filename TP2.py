import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Student': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E8', 'E9'],
    'Revision Hours': [2, 4, 6, 3, 5, np.nan , 4, 4, 4, 20],
    'Attendance': [80, 90, 95, 70, 85, 90, 105, 90, 90, 95],
    'Grade': [55, 70, 85, 60, 75, 78, 68, 70, 70, 98],
}

df = pd.DataFrame(data)

# display the first rows
print(df.head(), "\n")

# display the dimensions of the dataset
print(f"Shape tuple: {df.shape}\n")

# display the data types of the variables
print(df.dtypes)

# mean median min max standard deviation of the dataset
print("\nMean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nMin:\n", df.min(numeric_only=True))
print("\nMax:\n", df.max(numeric_only=True))
print("\nStandard Deviation:\n", df.std(numeric_only=True))

# histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Grade'], bins=10, color='blue', edgecolor='black')
plt.xlabel('Grade')
plt.ylabel('Frequency')
plt.title('Grades')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Revision Hours'], df['Grade'], color='blue', alpha=0.7)
plt.xlabel('Revision Hours')
plt.ylabel('Grade')
plt.title('Revision Hours vs Grade')
plt.show()

# handle missing values in Revision Hours
temp = df['Revision Hours'].median()
df['Revision Hours'] = df['Revision Hours'].fillna(temp)

# remove duplicates
df = df.drop_duplicates()

# fix for invalid values
df.loc[df['Attendance'] > 100, 'Attendance'] = 100

# boxplot of grades
plt.figure(figsize=(10, 6))
plt.boxplot(df['Grade'], vert=False)
plt.xlabel('Grade')
plt.title('Boxplot of Grades')
plt.show()

# min,max normalization
grades = df['Grade']
min = grades.min()
max = grades.max()

df['Normalized'] = (grades - min) / (max - min)
print(df[['Student', 'Grade', 'Normalized']])
