from flask import Flask, request, jsonify, render_template
from flasgger import Swagger
import pandas as pd

app = Flask(__name__)
Swagger(app)


@app.route('/')
def home():
    return "Welcome"


@app.route('/metrics',methods=['GET'])
def post_metrics():
    """
    This function prints the evaluation metrics for the models: 
    Linear Regression, Random Forest Regression and Gradiant Boost Regression
    ---
    responses:
        200:
            description: The evaluation metrics of the models
            - name: RMSE - Root Mean Squared Error
            - name: MAE - Mean Absolute Error
            - name: R-squared
    """
    df1 = pd.read_csv("Train_data_metrics.csv").to_html(index=False)
    return "TRAIN DATASET: Metrics: \n{}".format(df1)


@app.route('/results',methods=['GET'])
def post_results():
    """
    This function prints the Sale Price of the data set using Random Forest Regression model.
    ---
    responses:
        200:
            description: This function prints the prediction values of the Random Forest 
            Regression model as that model has the highest accuracy.
    """
    df2 = pd.read_csv("final_submission.csv").to_html(index=False)
    return "TEST DATASET: \n Sale Price Prediction Results: \n{}".format(df2)


if __name__ == "__main__":
    app.run(debug=True)