import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "dataset.csv"
MODEL_PATH = BASE_DIR / "models" / "random_forest.pkl"

df = pd.read_csv(DATA_PATH)

X = df.drop("label", axis=1)
y = df["label"]

model = joblib.load(MODEL_PATH)

preds = model.predict(X)

print("Accuracy:", accuracy_score(y, preds))

print(classification_report(y, preds))

cm = confusion_matrix(y, preds)

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=["Helix","Sheet","Coil"],
    yticklabels=["Helix","Sheet","Coil"]
)

plt.title("Confusion Matrix")
plt.show()