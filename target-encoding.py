import os
import pandas as pd
import category_encoders as ce

# Resolve project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "Student_Performance.csv")

# Load dataset
df = pd.read_csv(DATA_PATH)

# -----------------------------
# Target column (CONFIRMED)
# -----------------------------
target = "overall_score"

# Select categorical columns
cat_cols = df.select_dtypes(include='object').columns

# Apply Target Encoding
encoder = ce.TargetEncoder(cols=cat_cols)
df_encoded = encoder.fit_transform(df, df[target])

print("Target Encoding Applied Successfully")
print("Target column used:", target)
print(df_encoded.head())
