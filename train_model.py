"""
Run this script ONCE to train the model and generate customer_behavior_model.pkl
Usage:  python train_model.py
"""

import zipfile
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ── Load dataset ──────────────────────────────────────────────────────────────
DATASET_ZIP = "online+shoppers+purchasing+intention+dataset.zip"

with zipfile.ZipFile(DATASET_ZIP) as z:
    with z.open("online_shoppers_intention.csv") as f:
        df = pd.read_csv(f)

print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ── Encode categorical columns ────────────────────────────────────────────────
le_month   = LabelEncoder()
le_visitor = LabelEncoder()

df["Month"]       = le_month.fit_transform(df["Month"])
df["VisitorType"] = le_visitor.fit_transform(df["VisitorType"])
df["Weekend"]     = df["Weekend"].astype(int)
df["Revenue"]     = df["Revenue"].astype(int)

print("Month classes  :", list(le_month.classes_))
print("Visitor classes:", list(le_visitor.classes_))

# ── Train / Test split ────────────────────────────────────────────────────────
X = df.drop("Revenue", axis=1)
y = df["Revenue"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── Train Random Forest ───────────────────────────────────────────────────────
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print(f"\nAccuracy: {accuracy_score(y_test, preds):.4f}")
print(classification_report(y_test, preds, target_names=["No Purchase", "Purchase"]))

# ── Save model and encoders ───────────────────────────────────────────────────
with open("customer_behavior_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("encoders.pkl", "wb") as f:
    pickle.dump({"month": le_month, "visitor": le_visitor}, f)

# Save feature column order (important for correct prediction)
with open("feature_columns.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)

print("✅  Saved: customer_behavior_model.pkl")
print("✅  Saved: encoders.pkl")
print("✅  Saved: feature_columns.pkl")
