# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:15:58 2020

@author: pRoJyot
"""

import numpy as np
from flask import Flask, request, jsonify,render_template
import pickle

from joblib import dump, load

app = Flask(__name__)
path = "D:\Machine Learning Sentex\ML Project\ML Dragon Real Estate\deployment_heroku\template\index.html"
path_model = "D:\Machine Learning Sentex\ML Project\ML Dragon Real Estate\deployment_heroku"
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
        #For rendering results on HTML GUI
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Housing Price should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)