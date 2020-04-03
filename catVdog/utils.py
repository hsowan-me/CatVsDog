from django.conf import settings
from keras.models import load_model
import os
import cv2
import numpy as np
import tensorflow as tf


ROWS = 150
COLS = 150
CHANNELS = 3


def read_image(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
    return cv2.resize(img, (ROWS, COLS), interpolation=cv2.INTER_CUBIC)


def predict():
    dir_path = os.path.join(settings.MEDIA_ROOT, 'img')
    filename = os.listdir(dir_path)[0]
    file_path = os.path.join(dir_path, filename)
    image = read_image(file_path)

    model_path = os.path.join(settings.BASE_DIR, 'model.h5')
    graph = tf.get_default_graph()
    model = load_model(model_path)

    data = np.ndarray((1, ROWS, COLS, CHANNELS), dtype=np.uint8)
    data[0] = image
    test = data

    with graph.as_default():
        predictions = model.predict(test, verbose=0)

    results = {}
    if predictions[0, 0] >= 0.5:
        print('I am {:.2%} sure this is a Dog'.format(predictions[0][0]))
        results[f'/media/img/{filename}'] = "图片预测为：Dog！"
    else:
        print('I am {:.2%} sure this is a Cat'.format(1 - predictions[0][0]))
        results[f'/media/img/{filename}'] = "图片预测为：Cat！"
    return results

