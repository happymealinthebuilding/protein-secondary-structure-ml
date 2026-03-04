# Protein Secondary Structure Prediction using Machine Learning

## Overview

Proteins are chains of amino acids that fold into complex three-dimensional structures.
A key intermediate representation of this folding is **secondary structure**, which describes local structural patterns such as:

* **α-Helix (H)**
* **β-Sheet (E)**
* **Coil (C)**

Predicting secondary structure from the **primary amino acid sequence** is a classic problem in **bioinformatics and computational biology**.

This project implements a **machine learning pipeline** that predicts the secondary structure of each amino acid in a protein sequence.

The project demonstrates the full workflow:

1. Preparing biological data
2. Converting sequences into machine-learning features
3. Training a classification model
4. Evaluating prediction accuracy
5. Predicting structures for new protein sequences

The model is implemented using **Python and scikit-learn**.

---

# Project Motivation

Predicting protein structure directly from sequence is a fundamental challenge in computational biology.
Modern tools such as AlphaFold rely on deep learning and massive datasets.

However, before deep learning approaches, classical machine learning models such as **Random Forests, SVMs, and Neural Networks** were widely used for secondary structure prediction.

This project replicates the **classical ML pipeline** used in early protein structure prediction research.

---

# Why the Local Model Uses Only 30 Amino Acids

The dataset used in this repository contains only **~30 residues**.

This was intentionally done for the **initial prototype stage** of the project.

Reasons:

1. **Local hardware limitations**

The project was initially developed on a **MacBook without GPU acceleration**.
Training on large protein datasets can require significant computational resources.

2. **Concept validation**

The goal of the first stage was to verify that the full pipeline works:

* feature extraction
* dataset generation
* model training
* prediction
* evaluation

Using a small synthetic dataset allowed rapid debugging and iteration.

3. **Pipeline verification**

The small dataset ensures that the ML pipeline works end-to-end before scaling to larger biological datasets.

---

# Planned Scaling Phase (Google Colab)

After validating the pipeline locally, the next stage will involve scaling the dataset using **Google Colab GPU resources**.

The plan is to:

* download protein sequences with known structures from **Protein Data Bank (PDB)**
* extract secondary structure annotations using **DSSP**
* build a dataset of approximately **50,000+ residues**

Training on larger datasets significantly improves prediction accuracy and produces more biologically meaningful results.

---

# Machine Learning Approach

## Feature Representation

Machine learning algorithms cannot process amino acids directly as letters.

Each amino acid is converted into a **one-hot encoded vector**.

Example:

| Amino Acid | Encoding      |
| ---------- | ------------- |
| A          | [1,0,0,0,...] |
| C          | [0,1,0,0,...] |
| D          | [0,0,1,0,...] |

There are **20 standard amino acids**, so each residue becomes a **20-dimensional feature vector**.

---

## Label Mapping

Secondary structure annotations are simplified into three categories:

| DSSP Label | Category |
| ---------- | -------- |
| H, G, I    | Helix    |
| E, B       | Sheet    |
| Other      | Coil     |

This creates a **3-class classification problem**.

---

# Model

The model used in this project is a **Random Forest classifier**.

Random Forest is an ensemble learning algorithm that:

* builds many decision trees
* aggregates their predictions
* reduces overfitting

Model parameters:

```
n_estimators = 200
max_depth = 10
```

Random Forest was chosen because it:

* performs well on structured datasets
* requires minimal tuning
* works well with categorical features

---

# Project Pipeline

The workflow consists of four main steps.

---

## 1. Feature Engineering

Script:

```
src/feature_engineering.py
```

This script:

* encodes amino acids using one-hot encoding
* generates the dataset
* saves the processed data

Output:

```
data/processed/dataset.csv
```

---

## 2. Model Training

Script:

```
src/train_model.py
```

Steps:

1. Load dataset
2. Split into training and test sets
3. Train Random Forest classifier
4. Save trained model

Output:

```
models/random_forest.pkl
```

---

## 3. Model Evaluation

Script:

```
src/evaluate_model.py
```

Metrics computed:

* Accuracy
* Precision
* Recall
* F1 score
* Confusion matrix

The confusion matrix visualizes where the model predicts correctly or incorrectly.

---

## 4. Structure Prediction

Script:

```
src/predict.py
```

This script allows users to input a protein sequence and obtain predicted secondary structure.

Example:

```
Enter protein sequence:
ACDEFGHIKLMNP
```

Output:

```
Helix Helix Coil Coil Coil Coil Coil Coil Coil Coil Sheet Coil Coil
```

Each prediction corresponds to one amino acid in the sequence.

---

# Project Structure

```
protein-ss-predictor
│
├── data
│   ├── raw
│   └── processed
│
├── models
│
├── src
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict.py
│
├── venv
└── README.md
```

---

# Installation

Clone the repository and install dependencies.

```
pip install -r requirements.txt
```

Or manually install:

```
pip install numpy pandas scikit-learn matplotlib seaborn biopython joblib
```

---

# Running the Pipeline

Run the scripts in order:

```
python src/feature_engineering.py
python src/train_model.py
python src/evaluate_model.py
python src/predict.py
```

---

# Future Improvements

Several improvements can significantly increase model performance.

### 1. Sliding Window Features

Instead of predicting from a single residue, use neighboring amino acids.

Example:

```
[-2, -1, current, +1, +2]
```

This technique is used in classical secondary structure predictors.

---

### 2. Larger Dataset

Train on **50k+ residues from PDB**.

More training data improves generalization and prediction accuracy.

---

### 3. Neural Networks

Implement models such as:

* Multi-layer perceptrons
* Convolutional neural networks
* Recurrent neural networks

---

### 4. Visualization

Add prediction confidence plots along the sequence.

---

# Technologies Used

* Python
* scikit-learn
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Biopython

---

# Educational Purpose

This project is intended as a **learning exercise in machine learning applied to bioinformatics**.

It demonstrates how biological sequence data can be converted into machine-learning features and used to train predictive models.

---

# Author

Azra Tuncay

