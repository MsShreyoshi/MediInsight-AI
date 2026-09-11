from pathlib import Path
import joblib
import pandas as pd

BASE = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE / "models" / "test_recommender" / "test_recommender.joblib"

def load():
    return joblib.load(MODEL_PATH)

def recommend(symptoms):
    bundle = load()
    model = bundle["model"]
    features = bundle["symptoms"]
    x = pd.DataFrame([{s: int(s in symptoms) for s in features}])
    probs = model.predict_proba(x)[0]
    classes = model.classes_
    order = probs.argsort()[::-1][:3]

    predictions = [
        {"condition": str(classes[i]), "confidence": round(float(probs[i]), 3)}
        for i in order
    ]
    top = predictions[0]["condition"]
    return {
        "top_prediction": top,
        "predictions": predictions,
        "recommended_tests": bundle["test_map"].get(top, [])
    }
