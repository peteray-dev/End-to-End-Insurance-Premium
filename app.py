from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.inproject.pipeline.prediction import PredictionPipeline
from math import ceil


app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/about',methods=['GET'])  # route to display the home page
def about_file():
    return render_template("about.html")

@app.route('/contact',methods=['GET'])  # route to display the home page
def contact():
    return render_template("contact.html")

@app.route('/prediction',methods=['GET'])  # route to display the home page
def prediction():
    return render_template("prediction.html")

@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            # Extract fields from the form
            fields = [
                'Age', 'Gender', 'Annual Income', 'Marital Status',
                'Number of Dependents', 'Education Level', 'Occupation',
                'Health Score', 'Location', 'Policy Type', 'Previous Claims',
                'Vehicle Age', 'Credit Score', 'Insurance Duration',
                'Policy Start Date', 'Customer Feedback', 'Smoking Status',
                'Exercise Frequency', 'Property Type'
            ]

            # Initialize data dictionary for input
            data_dict = {}

            # Process form data
            for field in fields:
                value = request.form.get(field)

                # Handle missing values
                if value in [None, '', 'NaN']:
                    data_dict[field] = None
                    continue

                # Process specific data types
                if field in ['Age', 'Annual Income', 'Number of Dependents', 'Health Score', 
                             'Previous Claims', 'Vehicle Age', 'Credit Score', 'Insurance Duration']:
                    data_dict[field] = float(value)
                # elif field == 'Policy Start Date':
                #     # Convert date to a standard format or timestamp if required
                #     data_dict[field] = pd.to_datetime(value)
                else:
                    # Assume all other fields are categorical
                    data_dict[field] = value

            # Convert data dictionary to DataFrame
            data_df = pd.DataFrame([data_dict])
            print(f'inputed data: {data_df}')
            # Prediction logic
            obj = PredictionPipeline()
            # print(obj.predict())
            prediction = ceil(obj.predict(data=data_df))
       
            print("Prediction Result:", prediction)
            return render_template('result.html', prediction=str(prediction))

        except Exception as e:
            print("The Exception message is:", e)
            return f"Error during processing: {e}"
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8080)