import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import joblib

# === Load dataset ===
df = pd.read_csv("pep_details.csv")
df.dropna(subset=["sequence", "mimics_human"], inplace=True)

# === Feature Engineering Function ===
def extract_features(seq):
    seq = str(seq).upper()
    analysis = ProteinAnalysis(seq)
    
    # Amino acid % composition
    aa_counts = analysis.get_amino_acids_percent()
    aa_features = {f"perc_{aa}": aa_counts.get(aa, 0) for aa in 'ACDEFGHIKLMNPQRSTVWY'}
    
    # Extra features
    features = {
        "mol_weight": analysis.molecular_weight(),
        "aromaticity": analysis.aromaticity(),
        "instability_index": analysis.instability_index(),
        "isoelectric_point": analysis.isoelectric_point(),
        "gravy": analysis.gravy(),
        "charge": analysis.charge_at_pH(7.0)
    }
    
    return {**aa_features, **features}

# === Apply Feature Engineering to all rows ===
seq_features = df["sequence"].apply(extract_features)
seq_df = pd.DataFrame(seq_features.tolist())
df = pd.concat([df.reset_index(drop=True), seq_df], axis=1)

# === Select features ===
base_features = ["Binding_Energy", "HBonds", "SaltBridges", "Hydrophobicity", "Length"]
X = df[base_features + list(seq_df.columns)]
y = df["mimics_human"]

# === Train-Test split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# === Define models ===
models = {
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss"),
    "SVM": SVC(kernel='rbf', probability=True)
}

# === Train and evaluate each model ===
for name, model in models.items():
    print(f"\n======= {name} =======")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    joblib.dump(model, f"{name}_mimicry_model.joblib")




