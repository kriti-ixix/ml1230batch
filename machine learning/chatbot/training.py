#Importing the libraries
import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder 


#Data preparation
with open('intents.json') as file:
    data = json.load(file)

trainingSentences = []
trainingLabels = []
labels = []
responses = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        trainingSentences.append(pattern)
        trainingLabels.append(intent['tag'])
    responses.append(intent['responses'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])

    
#Label Encoder
lblEncoder = LabelEncoder()
lblEncoder.fit(trainingLabels)
trainingLabels = lblEncoder.transform(trainingLabels)


#Tokenization & Pad Sequences
vocabSize = 1000
oovToken = "<OOV>"
maxLength = 20

tokenizer = Tokenizer(num_words=vocabSize, oov_token=oovToken)
tokenizer.fit_on_texts(trainingSentences)
wordIndex = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(trainingSentences)
paddedSequences = pad_sequences(sequences, maxlen = maxLength)
