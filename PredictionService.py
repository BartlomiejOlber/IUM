
class PredictionService():
    def __init__(self, model, userDataRepository, productDataRepository):
        self.model = model
        self.discounts = [0, 5, 10, 15, 20]
        self.userDataRepository = userDataRepository
        self.productDataRepository = productDataRepository

    def getPrediction(self, user_id, product_id):
        prediction = self.discounts[len(self.discounts)-1]
        buyingProductFrequency = self.productDataRepository.getBuyProductFrequency(product_id)
        buyingFrequency = self.userDataRepository.getBuyFrequency(user_id)
        buyingWithBiggerDiscountFrequency = self.userDataRepository.getBuyBiggerDiscountFrequency(user_id)
        buyingWithLowerDiscountFrequency = self.userDataRepository.getBuyLowerDiscountFrequency(user_id)
        buyingWithDiscountFrequency = self.userDataRepository.getBuyDiscountFrequency(user_id)
        buyingWithoutDiscountFrequency = self.userDataRepository.getBuyWithoutFrequency(user_id)
        buyingThisProductWithBiggerDiscountFrequency = self.productDataRepository.getBuyBiggerFrequency(product_id)
        buyingThisProductWithLowerDiscountFrequency = self.productDataRepository.getBuyLowerFrequency(product_id)
        differenceBiggerLower = buyingThisProductWithBiggerDiscountFrequency \
                                - buyingThisProductWithLowerDiscountFrequency
        differenceDiscountWithout = buyingWithDiscountFrequency - buyingWithoutDiscountFrequency
        differenceThisProductBiggerLower = buyingThisProductWithBiggerDiscountFrequency \
                                           - buyingThisProductWithLowerDiscountFrequency
        for discount in self.discounts:
            clientWillBuyProductWithThisDiscount = self.model.predict(discount,
                                                   buyingProductFrequency,
                                   buyingFrequency,
                                   buyingWithBiggerDiscountFrequency,
                                   buyingWithLowerDiscountFrequency,
                                   buyingWithDiscountFrequency,
                                   buyingWithoutDiscountFrequency,
                                   buyingThisProductWithBiggerDiscountFrequency,
                                   buyingThisProductWithLowerDiscountFrequency,
                                   differenceBiggerLower,
                                   differenceDiscountWithout,
                                   differenceThisProductBiggerLower)
            if clientWillBuyProductWithThisDiscount:
                prediction = discount
                break
        return prediction