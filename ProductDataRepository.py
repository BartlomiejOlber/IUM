import sqlite3

class ProductDataRepository():

    def __init__(self, productDataBasePath):
        self.conToDataBase = sqlite3.connect(productDataBasePath)

    def getBuyProductFrequency(self,product_id):

        return 1

    def getBuyBiggerFrequency(self,product_id):

        return 1

    def getBuyLowerFrequency(self,product_id):

        return 1