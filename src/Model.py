import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

class Model:
    def __init__(self, train_inputs, train_output, real_inputs, real_output):
        self.train_inputs = train_inputs
        self.train_output = train_output
        self.real_inputs = real_inputs
        self.real_output = real_output
    def train(self):
        pass
    def predict(self):
        self.predicted_output = self.model.predict(self.real_inputs)
        return self.predicted_output