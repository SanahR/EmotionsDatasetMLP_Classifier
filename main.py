from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

#Step One: Creating the Data
emotion = load_dataset("dair-ai/emotion")

train_x = emotion['train']['text']
y_train = emotion['train']['label']
test_x = emotion['test']['text']
y_test = emotion['test']['label']

#Step Two: Creating the Vectorizer Algorithm
vectorizer = TfidfVectorizer()
6
#Step Three: Training the Algorithm
vectorizer.fit(train_x)

#Step Four: Doing the Actual Transformation
#Note: You can tell if the variable being used is the vectorized version if the name starts with "ve"
X_train = vectorizer.transform(train_x)
X_test = vectorizer.transform(test_x)

##########################################
## MACHINE LEARNING PORTION <3 <3 <3 <3 ##
##########################################

##################################
### Algorithm 1: MLP Classifier ##
##################################

#Creating the Algorithm #1
#First One: Hidden Layers = (3,3), accuracy = 64. Second One: Hidden Layers = (5,5), accuracy = 72 Third One: Hidden Layers = (7,5), accuracy = 76
#More Accuracy Tracking: 4th Try: Hidden Layers = (9,7), accuracy = 79.9, 5th Try: Hidden Layers = (11,9), accuracy = 81.6
#6th Try: Hidden Layers = (15,13), accuracy = 83.65,7th Try: Hidden Layers = (17,15), accuracy = 84.3
algo = MLPClassifier(max_iter = 6000,activation = 'relu',hidden_layer_sizes = (17,15),verbose = 2)

#Training the Algorithm
algo.fit(X_train,y_train)

#Prediction
index = np.random.randint(0,len(test_x))
y_pred = algo.predict(X_test)
print("Your tweet was: ",test_x[index])
emotions = {0: "sadness",1:"joy",2:"love",3:"anger",4:"fear",5:"surprise"}
answer = y_pred[index]
print("The MLP algorithm classified your tweet as: ",emotions[answer])

score = (accuracy_score(y_test,y_pred))*100
print("The accuracy percentage of our MLP algorithm is: ",score)

#Creating Algorithm #2:
#First Try: Neighbors = 10, accuracy = 73.95, Second Try: Neighbors = 20, accuracy = 76.75
algo2 = KNN(n_neighbors = 25)
algo2.fit(X_train,y_train)
index2 = np.random.randint(0,len(test_x))
y_pred2 = algo2.predict(X_test)
answer2 = y_pred2[index2]
print("Your second tweet was: ",test_x[index2])
print("The KNN algorithm classified your tweet as: ",emotions[answer2])

score2 = (accuracy_score(y_test,y_pred2))*100
print("The accuracy percentage of our KNN algorithm is: ",score2)
