import numpy as np
import tensorflow as tf
import librosa
import os
import warnings
warnings.filterwarnings("ignore")


def load_model():
    abs_path = os.getcwd()
    model = tf.keras.models.load_model(abs_path + "/saved_model/model_20230607_02")

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                  metrics=['accuracy'])

    return model


def sample_preparer(location):
    sample_data = []
    sample = np.zeros((128, 100, 3))
    y, sr = librosa.load(location, sr=22050)
    y, _ = librosa.effects.trim(y, top_db=50)
    y = librosa.resample(y=y, orig_sr=sr, target_sr=22050)
    melspect = librosa.feature.melspectrogram(y=y)

    for i, _ in enumerate(melspect):  # 128
        for j, _ in enumerate(melspect[i]):  # LENGTH
            sample[i][j] = melspect[i][j]

    sample_data = [sample]

    return sample_data
