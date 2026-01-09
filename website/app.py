from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def prediction(features):
    filename = 'model/predictor.pickle'
    try:
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        pred_value = model.predict([features])
        return pred_value
    except Exception as e:
        print("Prediction Error:", e)
        return None

@app.route('/', methods=['POST', 'GET'])
def index():
    pred = None
    error_msg = None

    if request.method == 'POST':
        try:
            # Collect all form inputs
            Age = request.form['Age']
            Blood_Pressure = request.form['Blood_Pressure']
            Cholesterol_Level = request.form['Cholesterol_Level']
            BMI = request.form['BMI']
            Sleep_Hours = request.form['Sleep_Hours']
            Triglyceride_Level = request.form['Triglyceride_Level']
            Fasting_Blood_Sugar = request.form['Fasting_Blood_Sugar']
            CRP_Level = request.form['CRP_Level']
            Homocysteine_Level = request.form['Homocysteine_Level']
            Gender = request.form['Gender']
            Smoking = request.form['Smoking']
            Family_Heart_Disease = request.form['Family_Heart_Disease']
            Diabetes = request.form['Diabetes']
            High_Blood_Pressure = request.form['High_Blood_Pressure']
            Low_HDL_Cholesterol = request.form['Low_HDL_Cholesterol']
            High_LDL_Cholesterol = request.form['High_LDL_Cholesterol']
            Exercise_Habits = request.form['Exercise_Habits']
            Alcohol_Consumption = request.form['Alcohol_Consumption']
            Stress_Level = request.form['Stress_Level']
            Sugar_Consumption = request.form['Sugar_Consumption']

            # Create features list (cast to float/int)
            feature_list = [
                float(Age),
                float(Gender),
                float(Blood_Pressure),
                float(Cholesterol_Level),
                float(Exercise_Habits),
                float(Smoking),
                float(Family_Heart_Disease),
                float(Diabetes),
                float(BMI),
                float(High_Blood_Pressure),
                float(Low_HDL_Cholesterol),
                float(High_LDL_Cholesterol),
                float(Alcohol_Consumption),
                float(Stress_Level),
                float(Sleep_Hours),
                float(Sugar_Consumption),
                float(Triglyceride_Level),
                float(Fasting_Blood_Sugar),
                float(CRP_Level),
                float(Homocysteine_Level),              
                
            ]

            print("Feature list:", feature_list)  # Debug
            pred_result = prediction(feature_list)
            print("Raw prediction:", pred_result)

            if pred_result is not None:
                pred = int(pred_result[0])
            else:
                error_msg = "Prediction failed. Check console for errors."

        except Exception as e:
            print("Form Error:", e)
            error_msg = str(e)

    return render_template("index.html", pred=pred, error_msg=error_msg)

if __name__ == "__main__":
    app.run(debug=True)
