import numpy as np
import pandas as pd

amino_acids = "ACDEFGHIKLMNPQRSTVWY"

def one_hot_encode(aa):
    vec = [0]*20
    if aa in amino_acids:
        vec[amino_acids.index(aa)] = 1
    return vec


def create_dataset(sequence, structure):

    X = []
    y = []

    for aa, ss in zip(sequence, structure):

        X.append(one_hot_encode(aa))

        if ss in ["H", "G", "I"]:
            y.append("Helix")
        elif ss in ["E", "B"]:
            y.append("Sheet")
        else:
            y.append("Coil")

    return np.array(X), np.array(y)


sequence = "ACDEFGHIKLMNPQRSTVWYACDEFGHIK"
structure = "HHHHCCCCEEECCCCCHHHHHCCCCEEE"

X, y = create_dataset(sequence, structure)

df = pd.DataFrame(X)
df["label"] = y

df.to_csv("data/processed/dataset.csv", index=False)

print("Dataset saved")