# EmotionsDatasetMLP_Classifier
A program using the MLP Classifier along with Scikit Learn to classify the test dataset of the Emotions Dataset. 
## Description
This program uses the MLP Classifer and the K Nearest Neighbors Classifier in a competition-like format to see which one can gain higher accuracies. It starts with a text-based dataset (The Emotions Dataset) before converting it using the TfidfVectorizer. The vectorized data is then fed through both the KNN and MLP algorithms, where I experimented a lot with the parameters to find the best accuracies. 
## Naming Standards
For this program, the fresh, imported, un-vectorized data was called "train_x and test_x". After being vectorized, I changed their names to the standard "X_train" and "X_test".

