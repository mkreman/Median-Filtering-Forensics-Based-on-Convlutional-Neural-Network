import sys
import os
import cv2
import numpy as np
from keras.models import load_model


# To hide warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

# Getting the image name
try:
    image = sys.argv[1]
except IndexError:
    print('Give a image path')

# Checking if the image exist
if not os.path.exists(image):
    print(f"'{image}' file does not exit.")
    quit()
else:
    print(f'Predicting on the image {image}')

# Reading the image
I = cv2.imread(image, 0)
image = I.copy()
np.clip(I, 0, 255, out=I)
I.astype('uint8')

# Applying the filter layer
I = cv2.medianBlur(I, 3)
I = cv2.medianBlur(I, 3) - I

# Getting a 64x64 patch from the image
shape = I.shape
I = I[shape[0]//2-32:shape[0]//2+32, shape[1]//2-32:shape[1]//2+32]
I = I.reshape(1, 64, 64, 1)

# Loading the model
print('Loading the model')
model = load_model('./data/saved_models/combined_model.h5', compile=False)

# Prediction
prediction = model.predict(I)
if prediction[0][0] < prediction[0][0]:
    print('Positive')
else:
    print('Negative')
print(prediction)