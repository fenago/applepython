#Step 1: Load the dataset and explore its features
import pandas as pd



df = pd.read_csv('titanic.csv')

print(df.head())

print(df.info())
#Step 2: Analyze Categorical to Categorical Columns (C2C)
Frequency Table and Crosstab
# Create frequency table

freq_table = df['Sex'].value_counts()

print(freq_table)



# Create crosstab

crosstab = pd.crosstab(index=df['Sex'], columns=df['Survived'])

print(crosstab)
Stacked Bar Chart
import matplotlib.pyplot as plt



# Create stacked bar chart

df.groupby(['Sex', 'Survived'])['PassengerId'].count().unstack().plot(kind='bar', stacked=True)

plt.show()
#Chi-Square Test
from scipy.stats import chi2_contingency



# Perform chi-square test

chi2, p, dof, expected = chi2_contingency(crosstab)

print('Chi-Square Statistic:', chi2)

print('P-Value:', p)
#Step 3: Analyze Categorical to Numeric Columns (C2N)
Box Plot
# Create box plot

df.boxplot(column='Age', by='Survived')

plt.show()
Violin Plot
import seaborn as sns



# Create violin plot

sns.violinplot(x='Survived', y='Age', data=df)

plt.show()
#T-Test
from scipy.stats import ttest_ind



# Create subsets of numeric variable based on categorical variable

subset1 = df.loc[df['Survived'] == 0]['Age'].dropna()

subset2 = df.loc[df['Survived'] == 1]['Age'].dropna()



# Perform t-test

t, p = ttest_ind(subset1, subset2)

print('T-Statistic:', t)

print('P-Value:', p)
#Step 4: Analyze Numeric to Numeric Columns (N2N)
Scatter Plot
import matplotlib.pyplot as plt



# Create scatter plot

plt.scatter(df['Age'], df['Fare'])

plt.xlabel('Age')

plt.ylabel('Fare')

plt.show()
#Correlation Coefficient
# Calculate correlation coefficient

corr = df['Age'].corr(df['Fare'])

print('Correlation Coefficient:', corr)
#Heatmap
import seaborn as sns



# Create heatmap

sns.heatmap(df.corr())

plt.show()
