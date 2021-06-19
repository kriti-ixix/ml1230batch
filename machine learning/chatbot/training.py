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

trainingSentences = [] #Possible user inputs 
trainingLabels = [] #All the tags 
labels = [] #Only unique tags
responses = [] #Bot responses

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

'''
[hello, goodbye, help, complaint, account] -> [0, 2, 1, 4, 3]
'''

#Tokenization & Pad Sequences
vocabSize = 1000
oovToken = "<OOV>"
maxLength = 20
embeddingDim = 16

tokenizer = Tokenizer(num_words=vocabSize, oov_token=oovToken)
tokenizer.fit_on_texts(trainingSentences)
wordIndex = tokenizer.word_index

'''
wordIndex: {'hi':230, 'help':555}
'''

sequences = tokenizer.texts_to_sequences(trainingSentences)
paddedSequences = pad_sequences(sequences, maxlen = maxLength)

'''
[[1, 2, 3], 
[0, 0, 4], 
[0, 5, 6]]
'''

#Creating a Neural Network
model = Sequential()
model.add(Embedding(vocabSize, embeddingDim, input_length=maxLength)) #Input layer 
model.add(GlobalAveragePooling1D())
model.add(Dense(16, activation='relu')) #Hidden layer
model.add(Dense(16, activation='relu')) #Hidden layer
model.add(Dense(len(labels), activation='softmax')) #Final hidden layer 

#Compiling the network
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
history = model.fit(paddedSequences, np.array(trainingLabels), epochs = 500)

#Saving the network
model.save("chatbot model")

#Saving the algorithms
import pickle 

pickle.dump(tokenizer, open('tokenizer.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
pickle.dump(lblEncoder, open('label encoder.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
