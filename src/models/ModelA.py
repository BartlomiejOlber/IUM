from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd

class ModelA():

    def __init__(self):
        self.xGBClassifier = XGBClassifier()

    def train(self,
                xTrain, yTrain):
        self.xGBClassifier.fit(xTrain, yTrain)

    def predict(self,
                discount,
                buyingProductFrequency,
                buyingFrequency,
                userBuyingProductFrequency,
                buyingWithBiggerDiscountFrequency,
                buyingWithLowerDiscountFrequency,
                buyingWithDiscountFrequency,
                buyingWithoutDiscountFrequency,
                buyingThisProductWithBiggerDiscountFrequency,
                buyingThisProductWithLowerDiscountFrequency,
                buyingThisProductWithDiscountFrequency,
                buyingThisProductWithoutDiscountFrequency,
                userBuyingThisProductWithBiggerDiscountFrequency,
                userBuyingThisProductWithLowerDiscountFrequency,
                userBuyingThisProductWithDiscountFrequency,
                userBuyingThisProductWithoutDiscountFrequency,
                differenceBiggerLower,
                differenceDiscountWithout,
                differenceThisProductBiggerLower,
                uesrDifferenceThisProductBiggerLower):

        x = [discount,
             buyingProductFrequency,
             buyingFrequency,
             userBuyingProductFrequency,
             buyingWithBiggerDiscountFrequency,
             buyingWithLowerDiscountFrequency,
             buyingWithDiscountFrequency,
             buyingWithoutDiscountFrequency,
             buyingThisProductWithBiggerDiscountFrequency,
             buyingThisProductWithLowerDiscountFrequency,
             buyingThisProductWithDiscountFrequency,
             buyingThisProductWithoutDiscountFrequency,
             userBuyingThisProductWithBiggerDiscountFrequency,
             userBuyingThisProductWithLowerDiscountFrequency,
             userBuyingThisProductWithDiscountFrequency,
             userBuyingThisProductWithoutDiscountFrequency,
             differenceBiggerLower,
             differenceDiscountWithout,
             differenceThisProductBiggerLower,
             uesrDifferenceThisProductBiggerLower]
        return self.xGBClassifier.predict(x)
