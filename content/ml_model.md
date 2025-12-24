# Exploratory Machine Learning Analysis

## Motivation and Scope

In addition to physics-based modeling (docking and molecular dynamics),
a small exploratory machine learning (ML) analysis was performed to gain
methodological exposure to peptide–protein interaction modeling.
Given the extremely limited dataset size, this analysis is **not intended
for prediction, validation, or hypothesis testing**, but purely as a
qualitative exploration of baseline ML behavior.

This chapter presents that exploratory machine learning (ML) exercise,
required dataset, feature preparation, training stratezy and limitation
of models.


## Dataset and Feature Preparation

The dataset consists of a very small number of peptides investigated
in the protein–peptide molecular mimicry study. Each peptide was described
using simple, interpretable features:

- **Peptide length**
- **Peptide sequence**
- **Binding energy**
- **H-bond details**
- **saltbridges** (analysed during analysis in gromacs by gmx_mpi)
- **Average hydrophobicity**, computed using the Kyte–Doolittle scale

Hydrophobicity values were calculated as the mean residue hydropathy
across each peptide sequence and used as a physicochemical descriptor.


## Machine Learning Models

Several standard supervised classification models were explored:

- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- XGBoost

The goal was to observe how different model families behave under
extreme data sparsity rather than to optimize performance.

---

## Training Strategy

The dataset was split into training and test subsets using a simple
train–test split. Models were trained using default hyperparameters
to avoid overfitting through manual tuning.

Model performance was assessed using accuracy and confusion matrix
visualization.

---

## Results and Observations

Due to the very small dataset size:

- Model accuracies varied widely and were unstable

- Strong class imbalance effects were observed

- Some models failed to correctly identify one of the classes

Confusion matrix visualizations illustrate this unstable classification
behavior, which is expected under such data constraints.

Trained model objects were saved using the `joblib` format for transparency
and reproducibility, rather than reuse.

---

## Limitations

The machine learning results presented here **cannot be considered
statistically meaningful or generalizable**. The analysis is limited by:

- Extremely small sample size
- Simplistic feature representation
- Absence of independent validation data

As a result, ML outputs are interpreted **qualitatively only** and are
not used to support or refute conclusions drawn from docking or MD
simulations.

---

## Summary

This exploratory ML analysis serves as a methodological complement to the
physics-based workflow, demonstrating familiarity with basic machine
learning pipelines while respecting the limitations imposed by the data.
