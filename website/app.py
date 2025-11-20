from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

def prediction(list):
     filename = 'model/predictor.pickle'
     with open(filename,'rb') as file:
          model = pickle.load(file)
     pred_value = model.predict([list])
     return pred_value
     
@app.route('/',methods=['POST','GET'])
def index():
     pred = 0
     if request.method == 'POST':
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
          
          feature_list = []
          feature_list.append(float(Age))
          feature_list.append(float(Blood_Pressure))
          feature_list.append(float(Cholesterol_Level))
          feature_list.append(float(BMI))
          feature_list.append(float(Sleep_Hours))
          feature_list.append(float(Triglyceride_Level))
          feature_list.append(float(Fasting_Blood_Sugar))
          feature_list.append(float(CRP_Level))
          feature_list.append(float(Homocysteine_Level))
          feature_list.append(int(Gender))
          feature_list.append(int(Smoking))
          feature_list.append(int(Family_Heart_Disease))
          feature_list.append(int(Diabetes))
          feature_list.append(int(High_Blood_Pressure))
          feature_list.append(int(Low_HDL_Cholesterol))
          feature_list.append(int(High_LDL_Cholesterol))
          feature_list.append(int(Exercise_Habits))
          feature_list.append(int(Alcohol_Consumption))
          feature_list.append(int(Stress_Level))
          feature_list.append(int(Sugar_Consumption))
          
          pred = prediction(feature_list)     
          
     return render_template("index.html", pred=pred)

if __name__ == "__main__":
    app.run(debug=True) 