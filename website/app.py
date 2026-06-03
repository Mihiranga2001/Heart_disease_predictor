from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

MODEL_PATH = os.path.join("model", "predictor.pickle")


def prediction(features):
    try:
        with open(MODEL_PATH, "rb") as file:
            model = pickle.load(file)

        pred_value = model.predict([features])
        return int(np.array(pred_value).flatten()[0])

    except Exception as e:
        print("Prediction Error:", e)
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    pred = None
    error_msg = None

    if request.method == "POST":
        try:
            feature_list = [
                float(request.form["Age"]),
                float(request.form["Gender"]),
                float(request.form["Blood_Pressure"]),
                float(request.form["Cholesterol_Level"]),
                float(request.form["Exercise_Habits"]),
                float(request.form["Smoking"]),
                float(request.form["Family_Heart_Disease"]),
                float(request.form["Diabetes"]),
                float(request.form["BMI"]),
                float(request.form["High_Blood_Pressure"]),
                float(request.form["Low_HDL_Cholesterol"]),
                float(request.form["High_LDL_Cholesterol"]),
                float(request.form["Alcohol_Consumption"]),
                float(request.form["Stress_Level"]),
                float(request.form["Sleep_Hours"]),
                float(request.form["Sugar_Consumption"]),
                float(request.form["Triglyceride_Level"]),
                float(request.form["Fasting_Blood_Sugar"]),
                float(request.form["CRP_Level"]),
                float(request.form["Homocysteine_Level"])
            ]

            print("Feature list:", feature_list)

            pred = prediction(feature_list)

            print("Final prediction:", pred)

            if pred is None:
                error_msg = "Prediction failed. Please check the model file or input values."

        except Exception as e:
            print("Form Error:", e)
            error_msg = "Invalid input. Please fill all fields correctly."

    return render_template("index.html", pred=pred, error_msg=error_msg)


if __name__ == "__main__":
    app.run(debug=True)