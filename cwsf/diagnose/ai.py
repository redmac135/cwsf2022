from tensorflow import keras
import numpy as np

# Loading the Model
model = keras.models.load_model(r'diagnose\aiassets\ForeSight.h5')

# Load scaling features
mean = np.load(r'diagnose\aiassets\mean.npy')
std = np.load(r'diagnose\aiassets\std.npy')

# Scaling
def scale(x, mean, std):
    return (x - mean) / std

labels = [
    'bladder',
    'breast',
    'colorectal',
    'esophageal',
    'gastric',
    'glioma',
    'liver',
    'lung',
    'non-cancer',
    'ovarian',
    'pancreatic',
    'prostate'
]

def predict(rawinput):
    # scaling the AI
    X = np.array(rawinput).astype(np.float64)
    scaled_inp = np.array([scale(X, mean, std)])

    # Getting AI's predictions
    predictions = model.predict(scaled_inp)[0]

    output = []

    # DIAGNOSIS
    for i in range(len(labels)):
        seq = [labels[i], '{0:.4f}'.format(predictions[i])]
        output.append(seq)
    
    return output