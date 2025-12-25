import os
import pandas as pd
from sklearn.preprocessing import MaxAbsScaler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "Student_Performance.csv")

df = pd.read_csv(DATA_PATH)

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

scaler = MaxAbsScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("Absolute (MaxAbs) Scaling Applied")
print(df.head())
