import numpy as np
import pandas as pd


class ModelTrainer():

    def __init__(self, predictionService, loggingService):
        # self.modelA = modelA
        # self.modelB = modelB
        self.predictionService = predictionService
        self.loggingService = loggingService

    def train(self, model, sessionsTrainPath, sessionsValidationPath):
        sessions = pd.read_json(sessionsTrainPath, lines=True)
        sessionsValidation = pd.read_json(sessionsValidationPath, lines=True)


        # sessions = sessions.iloc[0:int(0.02*(len(sessions))),:]
        # sessions = sessions[sessions['event_type'] == "BUY_PRODUCT"]
        sessionsChunked = np.array_split(sessions, 10)
        sessionsValidationChunked = np.array_split(sessionsValidation, 10)
        yTrain = []
        yTrainValidation = []
        for i, chunk in enumerate(sessionsChunked):
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
            yTrain.clear()
            yTrainValidation.clear()

            numberOfBought=0
            numberOf0Bought=0
            numberOf5Bought=0
            numberOf10Bought=0
            numberOf15Bought=0
            numberOf20Bought=0
            numberOfViewed=0

            for index, row in chunk.iterrows():
                print("Complete " + str(index/len(chunk.index)))
                specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)
                if row.event_type == "BUY_PRODUCT":
                    append = False
                    if row.offered_discount == 0:
                        if numberOf5Bought >= numberOf0Bought and \
                            numberOf10Bought >= numberOf0Bought and \
                            numberOf15Bought >= numberOf0Bought and \
                            numberOf20Bought >= numberOf0Bought:
                            numberOf0Bought = numberOf0Bought +1
                            append = True
                    if row.offered_discount == 5:
                        if numberOf0Bought >= numberOf5Bought and \
                            numberOf10Bought >= numberOf5Bought and \
                            numberOf15Bought >= numberOf5Bought and \
                            numberOf20Bought >= numberOf5Bought:
                            numberOf5Bought = numberOf5Bought +1
                            append = True

                    if row.offered_discount == 10:
                        if numberOf5Bought >= numberOf10Bought and \
                            numberOf0Bought >= numberOf10Bought and \
                            numberOf15Bought >= numberOf10Bought and \
                            numberOf20Bought >= numberOf10Bought:
                            numberOf10Bought = numberOf10Bought +1
                            append = True

                    if row.offered_discount == 15:
                        if numberOf5Bought >= numberOf15Bought and \
                            numberOf10Bought >= numberOf15Bought and \
                            numberOf0Bought >= numberOf15Bought and \
                            numberOf20Bought >= numberOf15Bought:
                            numberOf15Bought = numberOf15Bought +1
                            append = True

                    if row.offered_discount == 20:
                        if numberOf5Bought >= numberOf20Bought and \
                            numberOf0Bought >= numberOf20Bought and \
                            numberOf15Bought >= numberOf20Bought and \
                            numberOf0Bought >= numberOf20Bought:
                            numberOf20Bought = numberOf20Bought +1
                            append = True

                    if append:
                        yTrain.append(1)
                        xTrain = xTrain.append(specimen, ignore_index=True)
                        numberOfBought = numberOfBought +1
                else:
                    if numberOfViewed <= numberOfBought:
                        yTrain.append(0)
                        xTrain = xTrain.append(specimen, ignore_index=True)
                        numberOfViewed = numberOfViewed +1

            xTrainValidation = pd.DataFrame(columns=['discount',
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

            numberOfBought=0
            numberOf0Bought=0
            numberOf5Bought=0
            numberOf10Bought=0
            numberOf15Bought=0
            numberOf20Bought=0
            numberOfViewed=0

            for j, row in sessionsValidationChunked[i].iterrows():
                print("Validation Complete " + str(j/len(sessionsValidationChunked[i].index)))
                specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)
                if row.event_type == "BUY_PRODUCT":
                    append = False
                    if row.offered_discount == 0:
                        if numberOf5Bought >= numberOf0Bought and \
                                numberOf10Bought >= numberOf0Bought and \
                                numberOf15Bought >= numberOf0Bought and \
                                numberOf20Bought >= numberOf0Bought:
                            numberOf0Bought = numberOf0Bought + 1
                            append = True
                    if row.offered_discount == 5:
                        if numberOf0Bought >= numberOf5Bought and \
                                numberOf10Bought >= numberOf5Bought and \
                                numberOf15Bought >= numberOf5Bought and \
                                numberOf20Bought >= numberOf5Bought:
                            numberOf5Bought = numberOf5Bought + 1
                            append = True

                    if row.offered_discount == 10:
                        if numberOf5Bought >= numberOf10Bought and \
                                numberOf0Bought >= numberOf10Bought and \
                                numberOf15Bought >= numberOf10Bought and \
                                numberOf20Bought >= numberOf10Bought:
                            numberOf10Bought = numberOf10Bought + 1
                            append = True

                    if row.offered_discount == 15:
                        if numberOf5Bought >= numberOf15Bought and \
                                numberOf10Bought >= numberOf15Bought and \
                                numberOf0Bought >= numberOf15Bought and \
                                numberOf20Bought >= numberOf15Bought:
                            numberOf15Bought = numberOf15Bought + 1
                            append = True

                    if row.offered_discount == 20:
                        if numberOf5Bought >= numberOf20Bought and \
                                numberOf0Bought >= numberOf20Bought and \
                                numberOf15Bought >= numberOf20Bought and \
                                numberOf0Bought >= numberOf20Bought:
                            numberOf20Bought = numberOf20Bought + 1
                            append = True

                    if append:
                        yTrainValidation.append(1)
                        xTrainValidation = xTrainValidation.append(specimen, ignore_index=True)
                        numberOfBought = numberOfBought + 1
                else:
                    if numberOfViewed <= numberOfBought:
                        yTrainValidation.append(0)
                        xTrainValidation = xTrainValidation.append(specimen, ignore_index=True)
                        numberOfViewed = numberOfViewed +1

            xTrain = xTrain.fillna(0)
            xTrainValidation = xTrainValidation.fillna(0)
            model.train(xTrain, yTrain, xTrainValidation, yTrainValidation)

            for index, row in chunk.iterrows():
                isBought = False
                if row.event_type == "BUY_PRODUCT":
                    isBought = True
                self.loggingService.log(row.user_id, row.product_id, isBought, row.offered_discount)


    # def trainB(self, sessionsTrainPath):
    #     sessions = pd.read_json(sessionsTrainPath, lines=True)
    #
    #     xTrain = pd.DataFrame(columns=['discount',
    #                                    'buyingProductFrequency',
    #                                    'buyingFrequency',
    #                                    'userBuyingProductFrequency',
    #                                    'buyingWithBiggerDiscountFrequency',
    #                                    'buyingWithLowerDiscountFrequency',
    #                                    'buyingWithDiscountFrequency',
    #                                    'buyingWithoutDiscountFrequency',
    #                                    'buyingThisProductWithBiggerDiscountFrequency',
    #                                    'buyingThisProductWithLowerDiscountFrequency',
    #                                    'buyingThisProductWithDiscountFrequency',
    #                                    'buyingThisProductWithoutDiscountFrequency',
    #                                    'userBuyingThisProductWithBiggerDiscountFrequency',
    #                                    'userBuyingThisProductWithLowerDiscountFrequency',
    #                                    'userBuyingThisProductWithDiscountFrequency',
    #                                    'userBuyingThisProductWithoutDiscountFrequency',
    #                                    'differenceBiggerLower',
    #                                    'differenceDiscountWithout',
    #                                    'differenceThisProductBiggerLower',
    #                                    'userDifferenceThisProductBiggerLower'])
    #
    #     # sessions = sessions.iloc[0:int(0.02*(len(sessions))),:]
    #     # sessions = sessions[sessions['event_type'] == "BUY_PRODUCT"]
    #     for index, row in sessions.iterrows():
    #         print("Complete " + str(index/len(sessions.index)))
    #         specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)
    #
    #         xTrain.loc[0] = [specimen.discount,
    #                                specimen.buyingProductFrequency,
    #                                specimen.buyingFrequency,
    #                                specimen.userBuyingProductFrequency,
    #                                specimen.buyingWithBiggerDiscountFrequency,
    #                                specimen.buyingWithLowerDiscountFrequency,
    #                                specimen.buyingWithDiscountFrequency,
    #                                specimen.buyingWithoutDiscountFrequency,
    #                                specimen.buyingThisProductWithBiggerDiscountFrequency,
    #                                specimen.buyingThisProductWithLowerDiscountFrequency,
    #                                specimen.buyingThisProductWithDiscountFrequency,
    #                                specimen.buyingThisProductWithoutDiscountFrequency,
    #                                specimen.userBuyingThisProductWithBiggerDiscountFrequency,
    #                                specimen.userBuyingThisProductWithLowerDiscountFrequency,
    #                                specimen.userBuyingThisProductWithDiscountFrequency,
    #                                specimen.userBuyingThisProductWithoutDiscountFrequency,
    #                                specimen.differenceBiggerLower,
    #                                specimen.differenceDiscountWithout,
    #                                specimen.differenceThisProductBiggerLower,
    #                                specimen.userDifferenceThisProductBiggerLower]
    #
    #         isBought = False
    #         yTrain = [0]
    #         if row.event_type == "BUY_PRODUCT":
    #             isBought = True
    #             yTrain = [1]
    #
    #         self.modelB.train(xTrain, yTrain)
    #
    #
    #         self.loggingService.log(row.user_id, row.product_id, isBought, row.offered_discount)