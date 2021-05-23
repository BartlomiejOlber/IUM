import pandas as pd


class ModelTrainer():

    def __init__(self, modelA, modelB, predictionService):
        self.modelA = modelA
        self.modelB = modelB
        self.predictionService = predictionService

    def trainA(self, sessionsTrainPath):
        sessions = pd.read_json(sessionsTrainPath, lines=True)

        xTrain = pd.DataFrame(columns=['discount',
                                       'buyingProductFrequency',
                                       'buyingFrequency',
                                       'userBuyingProductFrequency',
                                       'buyingWithBiggerDiscountFrequency',
                                       'buyingWithLowerDiscountFrequency',
                                       'buyingWithDiscountFrequency',
                                       'buyingWithoutDiscountFrequency',
                                       'buyingThisProductWithBiggerDiscountFrequency',
                                       'buyingThisProductWithLowerDiscountFrequency',
                                       'buyingThisProductWithDiscountFrequency',
                                       'buyingThisProductWithoutDiscountFrequency',
                                       'userBuyingThisProductWithBiggerDiscountFrequency',
                                       'userBuyingThisProductWithLowerDiscountFrequency',
                                       'userBuyingThisProductWithDiscountFrequency',
                                       'userBuyingThisProductWithoutDiscountFrequency',
                                       'differenceBiggerLower',
                                       'differenceDiscountWithout',
                                       'differenceThisProductBiggerLower',
                                       'uesrDifferenceThisProductBiggerLower'])
        for index, row in sessions.iterrows():
            specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)
            # maybe needed to create df
            xTrain = xTrain.append([specimen.discount,
                                   specimen.buyingProductFrequency,
                                   specimen.buyingFrequency,
                                   specimen.userBuyingProductFrequency,
                                   specimen.buyingWithBiggerDiscountFrequency,
                                   specimen.buyingWithLowerDiscountFrequency,
                                   specimen.buyingWithDiscountFrequency,
                                   specimen.buyingWithoutDiscountFrequency,
                                   specimen.buyingThisProductWithBiggerDiscountFrequency,
                                   specimen.buyingThisProductWithLowerDiscountFrequency,
                                   specimen.buyingThisProductWithDiscountFrequency,
                                   specimen.buyingThisProductWithoutDiscountFrequency,
                                   specimen.userBuyingThisProductWithBiggerDiscountFrequency,
                                   specimen.userBuyingThisProductWithLowerDiscountFrequency,
                                   specimen.userBuyingThisProductWithDiscountFrequency,
                                   specimen.userBuyingThisProductWithoutDiscountFrequency,
                                   specimen.differenceBiggerLower,
                                   specimen.differenceDiscountWithout,
                                   specimen.differenceThisProductBiggerLower,
                                   specimen.userDifferenceThisProductBiggerLower])

        yTrain = sessions.event_type.str.get_dummies().drop(columns='VIEW_PRODUCT')

        self.modelA.train(xTrain, yTrain)
