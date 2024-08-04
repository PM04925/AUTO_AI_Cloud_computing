import pickle
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

# Load the trained machine learning model

# NOTE: pickle file is not uploaded as its size is greater than 1 GB

model_file_path = 'randomforestmodel'
with open(model_file_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form data
        data = {
            "Name": request.form.get('Name'),
            "Age": request.form.get('Age'),
            "Marital Status": request.form.get('Marital Status'),
            "Education Level": request.form.get('Education Level'),
            "Number of Children": request.form.get('Number of Children'),
            "Smoking Status": request.form.get('Smoking Status'),
            "Physical Activity Level": request.form.get('Physical Activity Level'),
            "Employment Status": request.form.get('Employment Status'),
            "Income": request.form.get('Income'),
            "Alcohol Consumption": request.form.get('Alcohol Consumption'),
            "Dietary Habits": request.form.get('Dietary Habits'),
            "Sleep Patterns": request.form.get('Sleep Patterns'),
            "History of Mental Illness": request.form.get('History of Mental Illness'),
            "History of Substance Abuse": request.form.get('History of Substance Abuse'),
            "Family History of Depression": request.form.get('Family History of Depression'),
            "Chronic Medical Conditions": request.form.get('Chronic Medical Conditions'),
        }
        input_data = np.array([[
            data["Age"],
            data["Marital Status"],
            data["Education Level"],
            data["Number of Children"],
            data["Smoking Status"],
            data["Physical Activity Level"],
            data["Employment Status"],
            data["Income"],
            data["Alcohol Consumption"],
            data["Dietary Habits"],
            data["Sleep Patterns"],
            data["History of Mental Illness"],
            data["History of Substance Abuse"],
            data["Family History of Depression"],
            data["Chronic Medical Conditions"]
        ]], dtype=float)  

        prediction = model.predict(input_data)[0]

        return render_template('result.html', data=data, prediction=prediction)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
