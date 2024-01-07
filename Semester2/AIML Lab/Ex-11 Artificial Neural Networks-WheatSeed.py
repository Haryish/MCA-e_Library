import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_curve, auc
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Load and preprocess your data (replace with your data loading code)
data = pd.read_csv('Datasets/seeds_dataset.txt',names = [1,2,3,4,5,6,7,8],sep='\s+')
data = data.sample(frac=1,random_state=123).reset_index(drop=True)
#displaying subroutines
dir(tf.keras.losses)
#dir(tf.keras.optimizers)

X = np.array(data)[:, 0:-1]
Y = np.array(data)[:, -1]
one_hot_encoder = OneHotEncoder(sparse=False)
Y = one_hot_encoder.fit_transform(np.array(Y).reshape(-1, 1))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)
# Define the neural network architecture
model = keras.Sequential([
    keras.layers.Input(shape=(X_train.shape[1],)),
    keras.layers.Dense(11, activation='relu'),
    keras.layers.Dense(7, activation='relu'),
    keras.layers.Dense(3, activation='relu'),
    keras.layers.Dense(Y_train.shape[1], activation='softmax')
])
# Compile the model
model.compile(optimizer='Adam', loss='CategoricalCrossentropy', metrics=['accuracy'])

# Train the model
epochs = 100
batch_size = 32
model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_test, Y_test))
     

# Evaluate the model
accuracy = model.evaluate(X_test, Y_test)
print("Testing Accuracy: {}".format(accuracy[1]))

# Predict and evaluate
Y_result = model.predict(X_test)
Y_result = np.argmax(Y_result, axis=1)
Y_test = np.argmax(Y_test, axis=1)

classification_rep = classification_report(Y_test, Y_result)
print("Classification Report:\n", classification_rep)

# Calculate fpr and tpr
fpr, tpr, _ = roc_curve(Y_test, Y_result)

# Plot ROC curve
def plot_roc_curve(fpr, tpr):
    plt.plot(fpr, tpr)
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.show()

plot_roc_curve(fpr, tpr)
