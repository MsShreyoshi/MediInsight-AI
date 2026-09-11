from pathlib import Path
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "test_recommender" / "demo_train.csv"
OUT = BASE / "models" / "test_recommender" / "test_recommender.joblib"

df = pd.read_csv(DATA)
features = [c for c in df.columns if c != "label"]
X, y = df[features], df["label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = RandomForestClassifier(
    n_estimators=250, random_state=42, class_weight="balanced_subsample"
)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print(classification_report(y_test, pred))

test_map = {
    "Respiratory Infection": ["CBC", "CRP", "Chest X-ray (if clinically indicated)"],
    "Urinary Tract Infection": ["Urinalysis", "Urine culture", "CBC (if systemic symptoms)"],
    "Gastroenteritis": ["CBC", "Electrolytes", "Stool testing (if indicated)"],
    "Migraine": ["Neurological assessment", "Brain imaging only if red flags/clinically indicated"],
    "Anemia": ["CBC", "Peripheral smear", "Iron studies"],
    "Diabetes": ["Fasting plasma glucose", "HbA1c", "Urine glucose/ketones if indicated"],
    "Hypertension": ["Blood pressure measurement", "Kidney function panel", "ECG"],
    "Thyroid Disorder": ["TSH", "Free T4", "Thyroid antibodies if indicated"],
}

joblib.dump(
    {"model": model, "symptoms": features, "test_map": test_map},
    OUT
)
print("Saved:", OUT)
