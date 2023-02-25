#Step 1: Load the dataset and explore its features
import pandas as pd
df = pd.read_csv('bank_customers.csv')
print(df.head())
print(df.info())
#Step 2: Analyze Categorical to Categorical to Categorical Columns (CCC)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv('bank_customers.csv')
# Create heatmap
sns.heatmap(pd.crosstab(df['Gender'], [df['Education'], df['Credit_Status']]), annot=True, fmt="d", cmap="YlGnBu")
plt.show()
#Step 3: Analyze Categorical to Categorical to Numeric Columns (CCN)
import matplotlib.pyplot as plt
# Create grouped box plot

df.boxplot(column='Income', by=['Gender', 'Education'], figsize=(12,8))

plt.show()
#Step 4: Analyze Numeric to Numeric to Categorical Columns (NNC)
# Create scatter plot with color-coded markers

sns.scatterplot(x="Age", y="Income", hue="Gender", data=df)

plt.show()
#Step 5: Analyze Numeric to Numeric to Numeric Columns (NNN)
#Pairplot
# Create pairplot

sns.pairplot(df, vars=['Age', 'Income', 'Credit_Score'], hue="Gender")

plt.show()

# Create correlation matrix

corr = df.corr()

sns.heatmap(corr, annot=True, cmap="YlGnBu")

plt.show()
# Create scatter plot matrix

sns.pairplot(df, vars=['Age', 'Income', 'Credit_Score'], hue="Gender", markers=['o', 's'])

plt.show()
