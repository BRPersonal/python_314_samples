import dask.dataframe as dd

url = "https://raw.githubusercontent.com/gakudo-ai/open-datasets/refs/heads/main/housing.csv"
df = dd.read_csv(url)

df.head()

#dask is lazy.It is mean for large dataset processing. So 
#you must call compute() to trigger the action
num_rows = df.shape[0].compute()
num_cols = df.shape[1]
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

#cleanup missing values
df = df.dropna()

num_rows = df.shape[0].compute()
num_cols = df.shape[1]
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

from sklearn.preprocessing import StandardScaler

numeric_df = df.select_dtypes(include=["number"])
X_pd = numeric_df.drop("median_house_value", axis=1).compute()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_pd)

y = df["median_house_value"]
y_pd = y.compute()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Use the scaled feature matrix produced earlier
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_pd, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.2f}")
 
