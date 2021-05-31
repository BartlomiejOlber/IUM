import numpy as np
import xgboost
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd

class ModelA():

    def __init__(self, modelSavePath):
        params = {
            "learning_rate": 0.001,
            "max_depth": 7,
            "objective": "binary:logistic"
        }
        self.xGBClassifier = XGBClassifier(**params)
        self.modelSavePath = modelSavePath

        if modelSavePath.is_file():
            self.xGBClassifier.load_model(modelSavePath)

    def train(self, xTrain, yTrain, xTrainValidation, yTrainValidation):
        xTrain = xTrain.astype('float')
        yTrain = pd.DataFrame(yTrain,columns=['Bought'])
        yTrain = yTrain.astype('float')

        xTrainValidation = xTrainValidation.astype('float')
        yTrainValidation = pd.DataFrame(yTrainValidation,columns=['Bought'])
        yTrainValidation = yTrainValidation.astype('float')

        eval_set = [(xTrainValidation, yTrainValidation)]
        # print(xTrain.iloc[0])
        # print(yTrain.iloc[0])

        # yTrain = xgboost.DMatrix(np.array(yTrain))
        self.xGBClassifier.fit(xTrain, yTrain, early_stopping_rounds=10, eval_metric=["auc","error","logloss"], eval_set=eval_set)
        # print(cross_val_score(self.xGBClassifier, X=xTrain, y=yTrain))
        # print(self.xGBClassifier.predict())
        self.xGBClassifier.save_model(self.modelSavePath)


    def predict(self,specimen):
        specimen = specimen.astype('float')

        return self.xGBClassifier.predict(specimen)
