import zipfile
import pandas as pd


# extract data from compressed archive
with zipfile.ZipFile("customer_data.zip", "r") as archive:
    archive.extractall()


# load data into a pandas dataframe
df = pd.read_csv("customer_data.csv")


# perform data analysis and manipulation
df["total_spent"] = df["quantity"] * df["price"]


# group data by customer and calculate the average total spent
df_grouped = df.groupby("customer_id").mean()


# save the data in a structured format (e.g. a csv file)
df_grouped.to_csv("customer_data_analyzed.csv")


# present the data to management (e.g. using a bar chart)
df_grouped.plot(kind='bar')
