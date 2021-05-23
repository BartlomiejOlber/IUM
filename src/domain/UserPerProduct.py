from src.domain.BasicEntityData import BasicEntityData


class UserPerProduct(BasicEntityData):

    def __init__(self, user_id, product_id,
                 buy_frequency,
                 views,
                 buy_without_discount_frequency,
                 buy_5_discount_frequency,
                 buy_10_discount_frequency,
                 buy_15_discount_frequency,
                 buy_20_discount_frequency,
                 buy_discount_frequency):
        super().__init__(buy_frequency,
                         views,
                         buy_without_discount_frequency,
                         buy_5_discount_frequency,
                         buy_10_discount_frequency,
                         buy_15_discount_frequency,
                         buy_20_discount_frequency,
                         buy_discount_frequency)
        self.user_id = user_id
        self.product_id = product_id

    @classmethod
    def fromRow(cls, row):
        user_id = row[0]
        product_id = row[1]
        buy_frequency = row[2]
        views = row[3]
        buy_without_discount_frequency = row[4]
        buy_5_discount_frequency = row[5]
        buy_10_discount_frequency = row[6]
        buy_15_discount_frequency = row[7]
        buy_20_discount_frequency = row[8]
        buy_discount_frequency = row[9]
        return cls(user_id,
                   product_id,
                   buy_frequency,
                   views,
                   buy_without_discount_frequency,
                   buy_5_discount_frequency,
                   buy_10_discount_frequency,
                   buy_15_discount_frequency,
                   buy_20_discount_frequency,
                   buy_discount_frequency)
