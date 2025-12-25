import os
import pandas as pd
import numpy as np
from scipy.stats import skew

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "Student_Performance.csv")

df = pd.read_csv(DATA_PATH)

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    if abs(skew(df[col])) > 1:
        df[col] = np.log1p(df[col])

print("Skewness Transformation Applied")
print(df.head())
