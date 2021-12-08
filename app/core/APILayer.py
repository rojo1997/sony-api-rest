import pickle
import numpy as np

from schema.schema import Geometry

class APILayer:
    def __init__(self):
        with open("app/data/model.pkl", mode = "rb") as f:
            self.regr = pickle.load(f)

    def predict(self, input: Geometry):
        output = self.regr.predict(np.array([input.coordinates]))
        return output[0]