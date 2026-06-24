from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import os

app = Flask(__name__)

# ── Lazy-load model artifacts ─────────────────────────────────────────────────
_model    = None
_encoders = None
_columns  = None

def get_artifacts():
    global _model, _encoders, _columns
    if _model is None:
        base = os.path.dirname(__file__)
        with open(os.path.join(base, "customer_behavior_model.pkl"), "rb") as f:
            _model = pickle.load(f)
        with open(os.path.join(base, "encoders.pkl"), "rb") as f:
            _encoders = pickle.load(f)
        with open(os.path.join(base, "feature_columns.pkl"), "rb") as f:
            _columns = pickle.load(f)
    return _model, _encoders, _columns


@app.route("/")
def home():
    return render_template("landing.html")


@app.route("/predict-page")
def predict_page():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        model, encoders, columns = get_artifacts()

        # Encode categorical fields using the same LabelEncoders from training
        month_enc   = int(encoders["month"].transform([str(data["Month"])])[0])
        visitor_enc = int(encoders["visitor"].transform([str(data["VisitorType"])])[0])

        # Build a DataFrame with the exact column order the model was trained on
        row = {
            "Administrative":          float(data["Administrative"]),
            "Administrative_Duration":  float(data["Administrative_Duration"]),
            "Informational":            float(data["Informational"]),
            "Informational_Duration":   float(data["Informational_Duration"]),
            "ProductRelated":           float(data["ProductRelated"]),
            "ProductRelated_Duration":  float(data["ProductRelated_Duration"]),
            "BounceRates":              float(data["BounceRates"]),
            "ExitRates":                float(data["ExitRates"]),
            "PageValues":               float(data["PageValues"]),
            "SpecialDay":               float(data["SpecialDay"]),
            "Month":                    month_enc,
            "OperatingSystems":         int(data["OperatingSystems"]),
            "Browser":                  int(data["Browser"]),
            "Region":                   int(data["Region"]),
            "TrafficType":              int(data["TrafficType"]),
            "VisitorType":              visitor_enc,
            "Weekend":                  int(data["Weekend"]),
        }

        X = pd.DataFrame([row], columns=columns)

        prediction = int(model.predict(X)[0])
        proba      = model.predict_proba(X)[0].tolist()

        return jsonify({
            "prediction":            prediction,
            "label":                 "Likely to Purchase" if prediction == 1 else "Not Likely to Purchase",
            "probability_purchase":    round(proba[1] * 100, 1),
            "probability_no_purchase": round(proba[0] * 100, 1),
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
