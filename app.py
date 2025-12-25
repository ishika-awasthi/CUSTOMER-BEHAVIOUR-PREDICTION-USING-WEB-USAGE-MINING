from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/predict-page")
def predict_page():
    return render_template("index.html")



# load trained model
with open("customer_behavior_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            float(request.form["Administrative"]),
            float(request.form["Administrative_Duration"]),
            float(request.form["Informational"]),
            float(request.form["Informational_Duration"]),
            float(request.form["ProductRelated"]),
            float(request.form["ProductRelated_Duration"]),
            float(request.form["BounceRates"]),
            float(request.form["ExitRates"]),
            float(request.form["PageValues"]),
            float(request.form["SpecialDay"]),
            float(request.form["Month"]),
            float(request.form["OperatingSystems"]),
            float(request.form["Browser"]),
            float(request.form["Region"]),
            float(request.form["TrafficType"]),
            float(request.form["VisitorType"]),
            float(request.form["Weekend"]),
        ]

        features = np.array(features).reshape(1, -1)
        prediction = model.predict(features)[0]

        result = "Purchase" if prediction == 1 else "No Purchase"

        return jsonify({
    "prediction": prediction,
    "label": "Likely to Purchase" if prediction == 1 else "Not Likely to Purchase"
})

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)


