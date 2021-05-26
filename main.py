from flask import Flask
from flask import request

from src.models.ModelB import ModelB
from src.models.ModelTrainer import ModelTrainer
from src.services.LoggingService import LoggingService
from src.models.ModelA import ModelA
from src.services.PredictionService import PredictionService
from src.repositories.ProductDataRepository import ProductDataRepository
from src.repositories.UserDataRepository import UserDataRepository
from src.repositories.UserPerProductDataRepository import UserPerProductDataRepository

import pandas as pd
import pathlib
from optparse import OptionParser

app = Flask(__name__)

productDataBasePath = pathlib.Path('usersAndProducts.db')
userDataBasePath = productDataBasePath
userPerProductDataBasePath = productDataBasePath

sessions_cleanPath = pathlib.Path("data/sessions_clean.jsonl")
sessionsTrainPath = pathlib.Path("data/sessionsTrain.jsonl")
sessionsValidationPath = pathlib.Path("data/sessionsValidation.jsonl")
sessionsTestPath = pathlib.Path("data/sessionsTest.jsonl")

saveModelAPath = pathlib.Path("savedModels/modelA.json")
saveModelBPath = pathlib.Path("savedModels/modelB.json")

userDataRepository = UserDataRepository(userDataBasePath.__str__())
productDataRepository = ProductDataRepository(productDataBasePath.__str__())
userPerProductDataRepository = UserPerProductDataRepository(userPerProductDataBasePath.__str__())

modelA = ModelA(saveModelAPath)
modelB = ModelB(saveModelBPath)

predictionService = PredictionService(modelA, modelB, userDataRepository, productDataRepository, userPerProductDataRepository)
loggingService = LoggingService(userDataRepository, productDataRepository, userPerProductDataRepository)

modelTrainer = ModelTrainer(predictionService,loggingService)


@app.route("/")
def index():
    return "<p> IUM web app! </p>"

@app.route("/predictA", methods  = ['POST'])
def predictA():
    user_id = request.args.get('user_id')
    product_id = request.args.get('product_id')
    prediction = predictionService.getPredictionA(user_id, product_id)
    return "<p> A prediction: " + str(prediction) + "</p>"

@app.route("/predictB", methods  = ['POST'])
def predictB():
    user_id = request.args.get('user_id')
    product_id = request.args.get('product_id')
    prediction = predictionService.getPredictionB(user_id, product_id)
    return "<p> B prediction: " + str(prediction) + "</p>"

@app.route("/bought", methods = ['POST'])
def bought():
    user_id = request.args.get('user_id')
    product_id = request.args.get('product_id')
    discount = request.args.get('discount')
    if loggingService.log(user_id, product_id, True, discount):
        return "OK"
    else:
        return "ERROR"

@app.route("/viewed", methods=['POST'])
def viewed():
    user_id = request.args.get('user_id')
    product_id = request.args.get('product_id')
    if loggingService.log(user_id, product_id, False, 0):
        return "OK"
    else:
        return "ERROR"
def createTrainAndTestAndLoadToDB():
    userDataRepository.deleteUsersTable()
    userDataRepository.createUsersTable()
    productDataRepository.deleteUsersTable()
    productDataRepository.createUsersTable()
    userPerProductDataRepository.deleteUserPerProductTable()
    userPerProductDataRepository.createUserPerProductTable()
    loggingService.logAndSplitFromJsonl(sessions_cleanPath,
                                        sessionsTrainPath,
                                        sessionsValidationPath,
                                        sessionsTestPath)

def testModelA(debug):
    sessions = pd.read_json(sessionsTestPath, lines=True)

    allBuys = len(sessions[sessions['event_type'] == "BUY_PRODUCT"])
    correctPredictionsCounter = 0
    falsePredictionsCounter = 0
    for index, row in sessions.iterrows():
        # print(row)
        prediction = predictionService.getPredictionA(row.user_id, row.product_id)
        # print(prediction)
        isBought = False
        if row.event_type == "BUY_PRODUCT":
            isBought = True
            if prediction >= row.offered_discount:
                correctPredictionsCounter = correctPredictionsCounter + 1
                print(prediction)
        else:
            if prediction > 0:
                falsePredictionsCounter = falsePredictionsCounter + 1

        loggingService.log(row.user_id, row.product_id, isBought, row.offered_discount)

    print("Accuracy: " + str(correctPredictionsCounter / allBuys))
    print("Precision: " + str( correctPredictionsCounter / (correctPredictionsCounter + falsePredictionsCounter)))

def trainModelA(debug):
    modelTrainer.train(modelA, sessionsTrainPath, sessionsValidationPath)

def trainModelB(debug):
    modelTrainer.train(modelB, sessionsTrainPath, sessionsValidationPath)

def testModelB(debug):
    sessions = pd.read_json(sessionsTestPath, lines=True)

    allBuys = len(sessions[sessions['event_type'] == "BUY_PRODUCT"])
    correctPredictionsCounter = 0
    falsePredictionsCounter = 0
    for index, row in sessions.iterrows():
        prediction = predictionService.getPredictionB(row.user_id, row.product_id)

        isBought = False
        if row.event_type == "BUY_PRODUCT":
            isBought = True
            if prediction >= row.offered_discount:
                correctPredictionsCounter = correctPredictionsCounter + 1
                # print(prediction)
        else:
            if prediction > 0:
                falsePredictionsCounter = falsePredictionsCounter + 1

        loggingService.log(row.user_id, row.product_id, isBought, row.offered_discount)

    print("Accuracy: " + str(correctPredictionsCounter / allBuys))
    print("Precision: " + str( correctPredictionsCounter / (correctPredictionsCounter + falsePredictionsCounter)))

if __name__ == '__main__':
    print("Hello AI World!")

    usage = "usage: %prog [options]\n" \
            "Debug: -q\n" \
            "Params: -t -e -l\n"
    parser = OptionParser(usage=usage)

    parser.add_option("-q", "--debug", action="store_true", dest="debug", default=False,
                      help="Prints debug info")
    # parser.add_option("-l", "--load", action="store_true", dest="load", default=False,
    #                   help="Loads data from data/sessions_clean.jsonl")
    parser.add_option("-t", "--train", type="int", dest="train", default=0,
                      help="Train model A (1) or model B (2) or none (0) (default 0)")
    parser.add_option("-e", "--test", type="int", dest="test", default=0,
                      help="Test model A (1) or model B (2) or none (0) (default 0)")

    (options, args) = parser.parse_args()

    # if options.load:
    #     createTrainAndTestAndLoadToDB()

    if options.train == 1:
        createTrainAndTestAndLoadToDB()
        trainModelA(options.debug)
    else:
        if options.train == 2:
            createTrainAndTestAndLoadToDB()
            trainModelB(options.debug)

    if options.test == 1:
        testModelA(options.debug)
    else:
        if options.test == 2:
            testModelB(options.debug)
