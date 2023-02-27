import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00498/incident_event_log.zip"

df = pd.read_csv(url, compression='zip', header=0, sep=',', quotechar='"')
print(df.head())
print(df.shape)
df = df.drop(['sys_updated_at', 'sys_created_at'], axis=1)
import seaborn as sns
sns.heatmap(df.corr())
df = df.drop(['impact', 'urgency'], axis=1)
from statsmodels.stats.outliers_influence import variance_inflation_factor
X = df.select_dtypes(include=[int, float])
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns
print(vif)
df = df.drop(['sys_mod_count'], axis=1)
df.to_csv('cleaned_data.csv', index=False)
