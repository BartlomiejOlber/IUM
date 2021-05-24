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
        'userDifferenceThisProductBiggerLower'])

        user = self.userDataRepository.getUser(user_id)
        product = self.productDataRepository.getProduct(product_id)
        userPerProduct = self.userPerProductDataRepository.getUserPerProduct(user_id, product_id)

        buyingFrequency = user.buy_frequency
        buyingWith5DiscountFrequency = user.buy_5_discount_frequency
        buyingWith10DiscountFrequency = user.buy_10_discount_frequency
        buyingWith15DiscountFrequency = user.buy_15_discount_frequency
        buyingWith20DiscountFrequency = user.buy_20_discount_frequency
        buyingWithDiscountFrequency = user.buy_discount_frequency
        buyingWithoutDiscountFrequency = user.buy_without_discount_frequency

        buyingProductFrequency = product.buy_frequency
        buyingThisProductWith5DiscountFrequency = product.buy_5_discount_frequency
        buyingThisProductWith10DiscountFrequency = product.buy_10_discount_frequency
        buyingThisProductWith15DiscountFrequency = product.buy_15_discount_frequency
        buyingThisProductWith20DiscountFrequency = product.buy_20_discount_frequency
        buyingThisProductWithDiscountFrequency = product.buy_discount_frequency
        buyingThisProductWithoutDiscountFrequency = product.buy_without_discount_frequency

        userBuyingProductFrequency = userPerProduct.buy_frequency
        userBuyingThisProductWith5DiscountFrequency = userPerProduct.buy_5_discount_frequency
        userBuyingThisProductWith10DiscountFrequency = userPerProduct.buy_10_discount_frequency
        userBuyingThisProductWith15DiscountFrequency = userPerProduct.buy_15_discount_frequency
        userBuyingThisProductWith20DiscountFrequency = userPerProduct.buy_20_discount_frequency
        userBuyingThisProductWithDiscountFrequency = userPerProduct.buy_discount_frequency
        userBuyingThisProductWithoutDiscountFrequency = userPerProduct.buy_without_discount_frequency

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
            print("\n" + str(discount) + ": " + clientWillBuyProductWithThisDiscountProbability)
            if clientWillBuyProductWithThisDiscountProbability > 0.5:
                prediction = discount
                break

        return prediction

