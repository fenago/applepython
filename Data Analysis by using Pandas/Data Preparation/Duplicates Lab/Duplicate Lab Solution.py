import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'

df = pd.read_csv(url, header=None)
df.head()
duplicate_rows = df[df.duplicated()]

# print the duplicate rows
print("Duplicate Rows:")
print(duplicate_rows)
df = df.drop_duplicates()

# print the updated DataFrame
print("Updated DataFrame:")
print(df)
