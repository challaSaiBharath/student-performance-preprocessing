import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "Student_Performance.csv")

df = pd.read_csv(DATA_PATH)

df.fillna(df.median(numeric_only=True), inplace=True)
df.fillna("Unknown", inplace=True)

df.drop_duplicates(inplace=True)

num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("Data Cleaning Completed")
print(df.head())
