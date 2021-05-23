import pandas as pd


class PredictionService():
    def __init__(self, modelA, modelB, userDataRepository, productDataRepository, userPerProductDataRepository):
        self.modelA = modelA
        self.modelB = modelB
        self.discounts = [0, 5, 10, 15, 20]
        self.userDataRepository = userDataRepository
        self.productDataRepository = productDataRepository
        self.userPerProductDataRepository = userPerProductDataRepository

    def getSpecimen(self, user_id, product_id, discount):
        specimen = pd.DataFrame(columns=['discount',
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

        buyingFrequency = self.userDataRepository.getBuyFrequency(user_id)
        buyingWith5DiscountFrequency = self.userDataRepository.get5DiscountFrequency(user_id)
        buyingWith10DiscountFrequency = self.userDataRepository.get10DiscountFrequency(user_id)
        buyingWith15DiscountFrequency = self.userDataRepository.get15DiscountFrequency(user_id)
        buyingWith20DiscountFrequency = self.userDataRepository.get20DiscountFrequency(user_id)
        buyingWithDiscountFrequency = self.userDataRepository.getBuyDiscountFrequency(user_id)
        buyingWithoutDiscountFrequency = self.userDataRepository.getBuyWithoutFrequency(user_id)

        buyingProductFrequency = self.productDataRepository.getBuyProductFrequency(product_id)
        buyingThisProductWith5DiscountFrequency = self.productDataRepository.get5DiscountFrequency(product_id)
        buyingThisProductWith10DiscountFrequency = self.productDataRepository.get10DiscountFrequency(product_id)
        buyingThisProductWith15DiscountFrequency = self.productDataRepository.get15DiscountFrequency(product_id)
        buyingThisProductWith20DiscountFrequency = self.productDataRepository.get20DiscountFrequency(product_id)
        buyingThisProductWithDiscountFrequency = self.productDataRepository.getBuyDiscountFrequency(product_id)
        buyingThisProductWithoutDiscountFrequency = self.productDataRepository.getBuyWithoutFrequency(product_id)

        userBuyingProductFrequency = self.userPerProductDataRepository.getBuyProductFrequency(product_id)
        userBuyingThisProductWith5DiscountFrequency = self.userPerProductDataRepository.get5DiscountFrequency(
            product_id)
        userBuyingThisProductWith10DiscountFrequency = self.userPerProductDataRepository.get10DiscountFrequency(
            product_id)
        userBuyingThisProductWith15DiscountFrequency = self.userPerProductDataRepository.get15DiscountFrequency(
            product_id)
        userBuyingThisProductWith20DiscountFrequency = self.userPerProductDataRepository.get20DiscountFrequency(
            product_id)
        userBuyingThisProductWithDiscountFrequency = self.userPerProductDataRepository.getBuyDiscountFrequency(
            product_id)
        userBuyingThisProductWithoutDiscountFrequency = self.userPerProductDataRepository.getBuyWithoutFrequency(
            product_id)

        buyingWithBiggerDiscountFrequency = 0
        buyingWithLowerDiscountFrequency = 0
        buyingThisProductWithBiggerDiscountFrequency = 0
        buyingThisProductWithLowerDiscountFrequency = 0
        userBuyingThisProductWithBiggerDiscountFrequency = 0
        userBuyingThisProductWithLowerDiscountFrequency = 0

        if discount == 0:
            buyingWithBiggerDiscountFrequency = \
                buyingWith5DiscountFrequency + \
                buyingWith10DiscountFrequency + \
                buyingWith15DiscountFrequency + \
                buyingWith20DiscountFrequency
            buyingWithLowerDiscountFrequency = 0

            buyingThisProductWithBiggerDiscountFrequency = \
                buyingThisProductWith5DiscountFrequency + \
                buyingThisProductWith10DiscountFrequency + \
                buyingThisProductWith15DiscountFrequency + \
                buyingThisProductWith20DiscountFrequency
            buyingThisProductWithLowerDiscountFrequency = 0

            userBuyingThisProductWithBiggerDiscountFrequency = \
                userBuyingThisProductWith5DiscountFrequency + \
                userBuyingThisProductWith10DiscountFrequency + \
                userBuyingThisProductWith15DiscountFrequency + \
                userBuyingThisProductWith20DiscountFrequency
            userBuyingThisProductWithLowerDiscountFrequency = 0
        if discount == 5:
            buyingWithBiggerDiscountFrequency = \
                buyingWith10DiscountFrequency + \
                buyingWith15DiscountFrequency + \
                buyingWith20DiscountFrequency
            buyingWithLowerDiscountFrequency = \
                buyingWithoutDiscountFrequency

            buyingThisProductWithBiggerDiscountFrequency = \
                buyingThisProductWith10DiscountFrequency + \
                buyingThisProductWith15DiscountFrequency + \
                buyingThisProductWith20DiscountFrequency
            buyingThisProductWithLowerDiscountFrequency = \
                buyingThisProductWithoutDiscountFrequency

            userBuyingThisProductWithBiggerDiscountFrequency = \
                userBuyingThisProductWith10DiscountFrequency + \
                userBuyingThisProductWith15DiscountFrequency + \
                userBuyingThisProductWith20DiscountFrequency
            userBuyingThisProductWithLowerDiscountFrequency = \
                userBuyingThisProductWithoutDiscountFrequency
        if discount == 10:
            buyingWithBiggerDiscountFrequency = \
                buyingWith15DiscountFrequency + \
                buyingWith20DiscountFrequency
            buyingWithLowerDiscountFrequency = \
                buyingWithoutDiscountFrequency + \
                buyingWith5DiscountFrequency

            buyingThisProductWithBiggerDiscountFrequency = \
                buyingThisProductWith15DiscountFrequency + \
                buyingThisProductWith20DiscountFrequency
            buyingThisProductWithLowerDiscountFrequency = \
                buyingThisProductWithoutDiscountFrequency + \
                buyingThisProductWith5DiscountFrequency

            userBuyingThisProductWithBiggerDiscountFrequency = \
                userBuyingThisProductWith15DiscountFrequency + \
                userBuyingThisProductWith20DiscountFrequency
            userBuyingThisProductWithLowerDiscountFrequency = \
                userBuyingThisProductWithoutDiscountFrequency + \
                userBuyingThisProductWith5DiscountFrequency
        if discount == 15:
            buyingWithBiggerDiscountFrequency = \
                buyingWith20DiscountFrequency
            buyingWithLowerDiscountFrequency = \
                buyingWithoutDiscountFrequency + \
                buyingWith5DiscountFrequency + \
                buyingWith10DiscountFrequency

            buyingThisProductWithBiggerDiscountFrequency = \
                buyingThisProductWith20DiscountFrequency
            buyingThisProductWithLowerDiscountFrequency = \
                buyingThisProductWithoutDiscountFrequency + \
                buyingThisProductWith5DiscountFrequency + \
                buyingThisProductWith10DiscountFrequency

            userBuyingThisProductWithBiggerDiscountFrequency = \
                userBuyingThisProductWith20DiscountFrequency
            userBuyingThisProductWithLowerDiscountFrequency = \
                userBuyingThisProductWithoutDiscountFrequency + \
                userBuyingThisProductWith5DiscountFrequency + \
                userBuyingThisProductWith10DiscountFrequency
        if discount == 20:
            buyingWithBiggerDiscountFrequency = 0
            buyingWithLowerDiscountFrequency = \
                buyingWithoutDiscountFrequency + \
                buyingWith5DiscountFrequency + \
                buyingWith10DiscountFrequency + \
                buyingWith15DiscountFrequency

            buyingThisProductWithBiggerDiscountFrequency = 0
            buyingThisProductWithLowerDiscountFrequency = \
                buyingThisProductWithoutDiscountFrequency + \
                buyingThisProductWith5DiscountFrequency + \
                buyingThisProductWith10DiscountFrequency + \
                buyingThisProductWith15DiscountFrequency

            userBuyingThisProductWithBiggerDiscountFrequency = 0
            userBuyingThisProductWithLowerDiscountFrequency = \
                userBuyingThisProductWithoutDiscountFrequency + \
                userBuyingThisProductWith5DiscountFrequency + \
                userBuyingThisProductWith10DiscountFrequency + \
                userBuyingThisProductWith15DiscountFrequency

        differenceBiggerLower = buyingThisProductWithBiggerDiscountFrequency - \
                                buyingThisProductWithLowerDiscountFrequency
        differenceDiscountWithout = buyingWithDiscountFrequency - \
                                    buyingWithoutDiscountFrequency
        differenceThisProductBiggerLower = buyingThisProductWithBiggerDiscountFrequency - \
                                           buyingThisProductWithLowerDiscountFrequency

        userDifferenceThisProductBiggerLower = userBuyingThisProductWithBiggerDiscountFrequency - \
                                               userBuyingThisProductWithLowerDiscountFrequency

        specimen.loc[0] = [discount,
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
        userDifferenceThisProductBiggerLower]

        return specimen

    def getPredictionA(self, user_id, product_id):
        prediction = self.discounts[len(self.discounts) - 1]

        for discount in self.discounts:
            x = self.getSpecimen(user_id, product_id, discount)
            clientWillBuyProductWithThisDiscountProbability = self.modelA.predict(x)
            if clientWillBuyProductWithThisDiscountProbability > 0.5:
                prediction = discount
                break

        return prediction

