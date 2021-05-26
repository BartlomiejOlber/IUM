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

            for index, row in chunk.iterrows():
                print("Complete " + str(index/len(chunk.index)))
                specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)
                xTrain = xTrain.append(specimen, ignore_index=True)

                if row.event_type == "BUY_PRODUCT":
                    yTrain.append(1)
                else:
                    yTrain.append(0)


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

            for j, row in sessionsValidationChunked[i].iterrows():
                print("Validation Complete " + str(j/len(sessionsValidationChunked[i].index)))
                specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)

                xTrainValidation = xTrainValidation.append(specimen, ignore_index=True)

                if row.event_type == "BUY_PRODUCT":
                    yTrainValidation.append(1)
                else:
                    yTrainValidation.append(0)

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