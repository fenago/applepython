import pandas as pd
df = pd.read_csv('abalone.csv')
print(df.dtypes)
df['Rings'] = df['Rings'].astype(float)
dtypes = {'Sex': 'category'}
df = df.astype(dtypes)
print(df.dtypes)
