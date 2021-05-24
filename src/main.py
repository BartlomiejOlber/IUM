from flask import Flask
from flask import request

from src.models.ModelTrainer import ModelTrainer
from src.services.LoggingService import LoggingService
from src.models.ModelA import ModelA
from src.services.PredictionService import PredictionService
from src.repositories.ProductDataRepository import ProductDataRepository
from src.repositories.UserDataRepository import UserDataRepository
from src.repositories.UserPerProductDataRepository import UserPerProductDataRepository

import pandas as pd
import pathlib

app = Flask(__name__)

productDataBasePath = pathlib.Path('usersAndProducts.db')
userDataBasePath = productDataBasePath
userPerProductDataBasePath = productDataBasePath

sessions_cleanPath = pathlib.Path("data/sessions_clean.jsonl")
sessionsTrainPath = pathlib.Path("data/sessionsTrain.jsonl")
sessionsTestPath = pathlib.Path("data/sessionsTest.jsonl")

saveModelAPath = pathlib.Path("savedModels/modelA.json")

userDataRepository = UserDataRepository(userDataBasePath.__str__())
productDataRepository = ProductDataRepository(productDataBasePath.__str__())
userPerProductDataRepository = UserPerProductDataRepository(userPerProductDataBasePath.__str__())

modelA = ModelA(saveModelAPath)

predictionService = PredictionService(modelA, modelA, userDataRepository, productDataRepository, userPerProductDataRepository)
loggingService = LoggingService(userDataRepository, productDataRepository, userPerProductDataRepository)

modelTrainer = ModelTrainer(modelA,modelA,predictionService)


# @app.route("/")
# def index():
#     return "<p> IUM web app! </p>"
#
# @app.route("/predictA", methods  = ['POST'])
# def predict():
#     user_id = request.args.get('user_id')
#     product_id = request.args.get('product_id')
#     prediction = predictionService.getPredictionA(user_id, product_id)
#     return "<p> A prediction: " + prediction + "</p>"
# 
# @app.route("/predictB", methods  = ['POST'])
# def predict():
#     user_id = request.args.get('user_id')
#     product_id = request.args.get('product_id')
#     prediction = predictionService.getPredictionB(user_id, product_id)
#     return "<p> B prediction: " + prediction + "</p>"
#
# @app.route("/bought", methods = ['POST'])
# def bought():
#     user_id = request.args.get('user_id')
#     product_id = request.args.get('product_id')
#     discount = request.args.get('discount')
#     if loggingService.log(user_id, product_id, True, discount):
#         return "OK"
#     else:
#         return "ERROR"
#
# @app.route("/viewed", methods=['POST'])
# def bought():
#     user_id = request.args.get('user_id')
#     product_id = request.args.get('product_id')
#     if loggingService.log(user_id, product_id, False, 0):
#         return "OK"
#     else:
#         return "ERROR"

if __name__ == '__main__':
    print("Hello World!")

    # loggingService.logAndSplitFromJsonl(sessions_cleanPath,
    #                                     sessionsTrainPath,
    #                                     sessionsTestPath)
    modelTrainer.trainA(sessionsTrainPath)

    sessions = pd.read_json(sessionsTestPath, lines=True)

    allBuys = len(sessions[sessions['event_type'] == "BUY_PRODUCT"])
    correctPredictionsCounter = 0
    for index, row in sessions.iterrows():
        prediction = predictionService.getPredictionA(row.user_id, row.product_id)

        if row.event_type == "BUY_PRODUCT":
            if prediction == row.offered_discount:
                correctPredictionsCounter = correctPredictionsCounter + 1

    print("Accuracy" + correctPredictionsCounter / allBuys)
