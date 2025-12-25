import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "Student_Performance.csv")

df = pd.read_csv(DATA_PATH)

cat_cols = df.select_dtypes(include='object').columns
df_encoded = pd.get_dummies(df, columns=cat_cols)

print("One-Hot Encoding Applied Successfully")
print(df_encoded.head())
