from flask import Flask , request , render_template
import os
from src.DS_project.pipeline.prediction_pipeline import PredictionPipeline
import numpy as np
from src.DS_project import logger

app =Flask(__name__)

@app.route("/" , methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/train" , methods=["GET"])
def train():
    os.system("python main.py")
    return "Training Successfull"

@app.route("/predict" , methods=["GET" , "POST"])
def predict():
    if request.method == "GET":
        return render_template("index.html")
    
    else:
        try:
            obj = PredictionPipeline()
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])

            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))


        except Exception as e:
            logger.exception(e)
            raise e



if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000 , debug=True)