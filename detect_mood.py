import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("emotion_model.h5")

emotion_labels = [
    "Angry",
    "Disgust",
    "Fear",
    "Happy",
    "Sad",
    "Surprise",
    "Neutral"
]

def detect():

    img = cv2.imread("captured_face.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = cv2.resize(gray,(48,48))

    face = face/255
    face = np.reshape(face,(1,48,48,1))

    prediction = model.predict(face)

    mood = emotion_labels[np.argmax(prediction)]

    return mood