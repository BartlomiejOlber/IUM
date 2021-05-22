from flask import Flask
from flask import request

from LoggingService import LoggingService
from Model import Model
from PredictionService import PredictionService
from ProductDataRepository import ProductDataRepository
from UserDataRepository import UserDataRepository

app = Flask(__name__)

productDataBasePath = 'products.db'
userDataBasePath = 'users.db'
userDataRepository = UserDataRepository(userDataBasePath)
productDataRepository = ProductDataRepository(productDataBasePath)
model = Model()

predictionService = PredictionService(model, userDataRepository, productDataRepository)
loggingService = LoggingService(userDataRepository, productDataRepository)

@app.route("/")
def index():
    return "<p> IUM web app! </p>"

@app.route("/predict", methods  = ['POST'])
def predict():
    user_id = request.args.get('user_id')
    product_id = request.args.get('product_id')
    prediction = predictionService.getPrediction(user_id, product_id)
    return "<p>" + prediction + "</p>"

@app.route("/bought", methods = ['POST'])
def bought():
    user_id = request.args.get('user_id')
    product_id = request.args.get('product_id')
    if loggingService.log(user_id, product_id):
        return "OK"
    else:
        return "ERROR"

if __name__ == '__main__':
    print("Hello World!")

