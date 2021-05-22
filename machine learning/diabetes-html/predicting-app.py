#Importing the libaries 
from flask import Flask, render_template, request, jsonify 
import requests
import pickle
import numpy as np 


#Setting up the API 
app = Flask(__name__)
loadedModel = pickle.load(open('diabetes.sav', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


#Taking the input from the form
@app.route('/predict', methods=['POST'])
def predict():
    bmi = int(request.form['bmi'])
    age = int(request.form['age'])
    glucose = int(request.form['glucose'])

    print("Age: ", age)
    print("BMI: ", bmi)
    print("Glucose: ", glucose)


#Main function
if __name__ == '__main__':
    app.run(debug=True)