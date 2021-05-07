#Importing the libraries
import pickle
from flask import Flask, request, json, jsonify
import numpy as np

#Global variables
app = Flask(__name__)
filename = 'diabetes.sav'
loadedModel = pickle.load(open(filename, 'rb'))

#User defined functions
@app.route('/', methods=['POST'])
def predict():
    #Getting the input
    features = request.json
    featuresList = [features['Glucose'], features['BMI'], features['Age']]

    #Making predictions
    prediction = loadedModel.predict([featuresList])
    confidence = loadedModel.predict_proba([featuresList])

    #Returning the predictions
    response = {}
    response['prediction'] = int(prediction[0])
    response['confidence'] = str(round(np.amax(confidence[0])*100, 2))

    return jsonify(response)

#Main function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)