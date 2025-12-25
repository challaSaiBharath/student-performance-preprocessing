import os
import pandas as pd
from sklearn.preprocessing import Normalizer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "Student_Performance.csv")

df = pd.read_csv(DATA_PATH)

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

normalizer = Normalizer()
df[num_cols] = normalizer.fit_transform(df[num_cols])

print("Vector Normalization Applied")
print(df.head())
