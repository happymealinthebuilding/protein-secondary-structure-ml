import joblib
import numpy as np
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "random_forest.pkl"
DATA_PATH = BASE_DIR / "data" / "processed" / "dataset.csv"

amino_acids = "ACDEFGHIKLMNPQRSTVWY"

def one_hot_encode(aa):
    vec = [0]*20
    if aa in amino_acids:
        vec[amino_acids.index(aa)] = 1
    return vec

model = joblib.load(MODEL_PATH)

# get feature column names from training data
df = pd.read_csv(DATA_PATH)
feature_names = df.drop("label", axis=1).columns

sequence = input("Enter protein sequence: ")

X = [one_hot_encode(a) for a in sequence]

X_df = pd.DataFrame(X, columns=feature_names)

pred = model.predict(X_df)

print("Predicted structure:")
print(pred)