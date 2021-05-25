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
                                       'userDifferenceThisProductBiggerLower'])

        # sessions = sessions.iloc[0:int(0.02*(len(sessions))),:]
        for index, row in sessions.iterrows():
            print("Complete " + str(index/len(sessions.index)))
            specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)

            df = pd.DataFrame(columns=['discount',
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
            df.loc[0] = [specimen.discount,
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
            # print(df)
            xTrain = xTrain.append(df)

        yTrain = sessions.event_type.str.get_dummies().drop(columns='VIEW_PRODUCT')

        self.modelA.train(xTrain, yTrain)


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
        for index, row in sessions.iterrows():
            print("Complete " + str(index/len(sessions.index)))
            specimen = self.predictionService.getSpecimen(row.user_id, row.product_id, row.offered_discount)

            df = pd.DataFrame(columns=['discount',
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
            df.loc[0] = [specimen.discount,
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
            # print(df)
            xTrain = xTrain.append(df)

        yTrain = sessions.event_type.str.get_dummies().drop(columns='VIEW_PRODUCT')

        self.modelB.train(xTrain, yTrain)