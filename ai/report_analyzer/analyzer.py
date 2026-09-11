from pathlib import Path
import re
import joblib

BASE = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE / "models" / "report_analyzer" / "report_classifier.joblib"

RANGES = {
    "hemoglobin": (12.0, 17.5, "g/dL"),
    "wbc": (4.0, 11.0, "x10^9/L"),
    "platelets": (150.0, 450.0, "x10^9/L"),
    "creatinine": (0.6, 1.3, "mg/dL"),
    "glucose": (70.0, 140.0, "mg/dL"),
}

PATTERNS = {
    "hemoglobin": r"hemoglobin\s*[:=]?\s*(\d+(?:\.\d+)?)",
    "wbc": r"wbc\s*[:=]?\s*(\d+(?:\.\d+)?)",
    "platelets": r"platelets\s*[:=]?\s*(\d+(?:\.\d+)?)",
    "creatinine": r"creatinine\s*[:=]?\s*(\d+(?:\.\d+)?)",
    "glucose": r"glucose\s*[:=]?\s*(\d+(?:\.\d+)?)",
}

def load_model():
    return joblib.load(MODEL_PATH)

def analyze(report_text):
    model = load_model()
    label = model.predict([report_text])[0]
    confidence = max(model.predict_proba([report_text])[0])

    labs = []
    flags = []
    text = report_text.lower()

    for name, pattern in PATTERNS.items():
        match = re.search(pattern, text)
        if not match:
            continue
        value = float(match.group(1))
        low, high, unit = RANGES[name]
        status = "within_demo_range"
        if value < low:
            status = "low"
            flags.append(f"{name} below configured demo range")
        elif value > high:
            status = "high"
            flags.append(f"{name} above configured demo range")
        labs.append({
            "test": name,
            "value": value,
            "unit": unit,
            "status": status,
            "reference_range": f"{low}-{high}"
        })

    return {
        "model_label": str(label),
        "model_confidence": round(float(confidence), 3),
        "extracted_labs": labs,
        "flags": flags,
    }
