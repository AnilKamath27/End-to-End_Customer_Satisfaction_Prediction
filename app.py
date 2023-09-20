import pickle #type: ignore
from flask import Flask, request, render_template,jsonify
import pandas as pd
import numpy as np
import warnings #type: ignore

app = Flask(__name__)

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Load the model
XGBoost_Model = pickle.load(open('XGBoost_Model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json['data'] # Get data as a dictionary
        input_data = np.array(list(data.values())).reshape(1, -1)
        prediction = int(XGBoost_Model.predict(input_data)[0])
        if prediction ==1:
            prediction = "Satisfied Customer"
        else:
            prediction = "Unsatisfied Customer"

        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()  # Get data as a dictionary

        # Create a DataFrame from the input data
        input_data = pd.DataFrame([data])

        # Make a prediction
        prediction = int(XGBoost_Model.predict(input_data)[0])
        if prediction == 1:
            prediction = "Satisfied Customer"
        else:
            prediction = "Unsatisfied Customer"

        return render_template('home.html', prediction_text='The prediction is {}'.format(prediction))

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)