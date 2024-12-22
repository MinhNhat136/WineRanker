from flask import Flask, render_template, request
import os
import numpy as np
from src.data_science.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful!"

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # Fetching form data
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                    free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            prediction_rounded = round(predict[0], 2)  
            if prediction_rounded < 2:
                conclusion = "Whoever gave you this wine literally trys to poison you!!!"
            elif 2 <= prediction_rounded < 6:
                conclusion = "Might as well just use it for cooking"
            elif 6 <= prediction_rounded < 8:
                conclusion = "Your wine is not bad, but can be better"
            else:
                conclusion = "You have a great wine in your hands!"

            return render_template('results.html', prediction=prediction_rounded, conclusion=conclusion)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something went wrong. Please try again.'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
