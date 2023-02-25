#This analysis is an example of univariate analysis, which involves examining the distribution of each feature separately. It is used to gain insight into the characteristics of a dataset and inform further analysis and modeling.

#Step 1: Import the necessary libraries
import pandas as pd

import matplotlib.pyplot as plt
#Step 2: Load the dataset
df = pd.read_csv('titanic.csv')
#Step 3: Examine the distribution of continuous features using histograms
plt.hist(df['Age'], bins=20)

plt.xlabel('Age')

plt.ylabel('Count')

plt.show()



plt.hist(df['Fare'], bins=20)

plt.xlabel('Fare')

plt.ylabel('Count')

plt.show()
#Step 4: Examine the distribution of continuous features using box plots
plt.boxplot(df['Age'])

plt.ylabel('Age')

plt.show()



plt.boxplot(df['Fare'])

plt.ylabel('Fare')

plt.show()
#Step 5: Examine the distribution of categorical features using a bar chart
counts = df['Sex'].value_counts()

counts.plot(kind='bar')

plt.xlabel('Sex')

plt.ylabel('Count')

plt.show()
#Step 6: Examine the distribution of categorical features using a pie chart
counts = df['Embarked'].value_counts()

counts.plot(kind='pie', autopct='%1.1f%%')

plt.ylabel('')

plt.show()
#Step 7: Examine the distribution of categorical features using a frequency table
freq_table = pd.crosstab(index=df['Embarked'], columns='count')

freq_table['percentage'] = freq_table['count'] / len(df) * 100

print(freq_table)
#Step 8: Examine the distribution of categorical features using a density plot
df['Embarked'].value_counts().plot(kind='density')

plt.xlabel('Embarked')

plt.show()
#Step 9: Summarize the findings
#You can see the graph below and can use them for your analysis
