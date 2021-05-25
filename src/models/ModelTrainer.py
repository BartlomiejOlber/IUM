import pandas as pd


class ModelTrainer():

    def __init__(self, modelA, modelB, predictionService, loggingService):
        self.modelA = modelA
        self.modelB = modelB
        self.predictionService = predictionService
        self.loggingService = loggingService

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
                                       'userDifferenceThisProductBiggerLower'])

        # TODO use validation
        # sessions = sessions.iloc[0:int(0.02*(len(sessions))),:]
        # sessions = sessions[sessions['event_type'] == "BUY_PRODUCT"]
        for index, row in sessions.iterrows():
            print("Complete " + str(index/len(sessions.index)))
            specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)

            xTrain.loc[0] = [specimen.discount,
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
                                   specimen.userDifferenceThisProductBiggerLower]

            isBought = False
            yTrain = [0]
            if row.event_type == "BUY_PRODUCT":
                isBought = True
                yTrain = [1]


            self.modelA.train(xTrain, yTrain)



            self.loggingService.log(row.user_id, row.product_id, isBought, row.offered_discount)


    def trainB(self, sessionsTrainPath):
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
                                       'userDifferenceThisProductBiggerLower'])

        # sessions = sessions.iloc[0:int(0.02*(len(sessions))),:]
        # sessions = sessions[sessions['event_type'] == "BUY_PRODUCT"]
        for index, row in sessions.iterrows():
            print("Complete " + str(index/len(sessions.index)))
            specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)

            xTrain.loc[0] = [specimen.discount,
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
                                   specimen.userDifferenceThisProductBiggerLower]

            isBought = False
            yTrain = [0]
            if row.event_type == "BUY_PRODUCT":
                isBought = True
                yTrain = [1]

            self.modelB.train(xTrain, yTrain)


            self.loggingService.log(row.user_id, row.product_id, isBought, row.offered_discount)