#Missing Values Lab
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
columns = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status",

    "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",

    "hours-per-week", "native-country", "income"]
df = pd.read_csv(url, header=None, names=columns, na_values=[" ?"])
df.isna().sum()
import missingno as msno
msno.matrix(df)
msno.bar(df)
threshold = 0.2  # 20% threshold
df.dropna(axis=0, thresh=int(df.shape[1] * (1 - threshold)), inplace=True)
threshold = 0.2  # 20% threshold
df.dropna(axis=1, thresh=int(df.shape[0] * (1 - threshold)), inplace=True)
