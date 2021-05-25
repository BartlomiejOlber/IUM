import numpy as np
import xgboost
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd

class ModelA():

    def __init__(self, modelSavePath):
        params = {
            "learning_rate": 0.01,
            "max_depth": 15
        }
        self.xGBClassifier = XGBClassifier(**params)
        self.modelSavePath = modelSavePath

        if modelSavePath.is_file():
            self.xGBClassifier.load_model(modelSavePath)

    def train(self, xTrain, yTrain):
        xTrain = xTrain.astype('float')
        yTrain = yTrain.astype('float')
        self.xGBClassifier.fit(xTrain, yTrain)
        print(cross_val_score(self.xGBClassifier, X=xTrain, y=yTrain))
        # print(self.xGBClassifier.predict())
        self.xGBClassifier.save_model(self.modelSavePath)

    def predict(self,specimen):
        specimen = specimen.astype('float')

        return self.xGBClassifier.predict(specimen)
