from pathlib import Path
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "report_analyzer" / "demo_reports.csv"
OUT = BASE / "models" / "report_analyzer" / "report_classifier.joblib"

df = pd.read_csv(DATA)
X_train, X_test, y_train, y_test = train_test_split(
    df["report_text"], df["label"], test_size=0.2,
    random_state=42, stratify=df["label"]
)
model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), lowercase=True)),
    ("clf", LogisticRegression(max_iter=1000, random_state=42))
])
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print(classification_report(y_test, pred))

joblib.dump(model, OUT)
print("Saved:", OUT)
