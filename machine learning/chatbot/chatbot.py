import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import random
import pickle
import colorama
from colorama import Fore, Style, Back

#Initialising
colorama.init()
with open('intents.json') as file:
    data = json.load(file)

#Loading the model and the algorithms
model = keras.models.load_model('chatbot model')
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
lblEncoder = pickle.load(open('label encoder.pkl', 'rb'))

print(Fore.YELLOW + "Start talking to the bot and enter quit to stop" + Style.RESET_ALL)

while True:
    print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
    userInput = input()

    if userInput == 'quit':
        break

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences
    ([userInput]), truncating='post', maxlen=20))

    '''
    [hello, goodbye, help, complaint, account] -> [0, 2, 1, 4, 3]
    array([0.3, 0.6, 0.56, 0.78])
    '''

    tag = lblEncoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            print(Fore.GREEN + "Bot: " + Style.RESET_ALL, np.random.choice(i['responses']))


'''
User: <message>
Bot: <bot response>
'''