from src.domain.BasicEntityData import BasicEntityData


class Product(BasicEntityData):

    def __init__(self, product_id,
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
        self.product_id = product_id


    @classmethod
    def fromRow(cls, row):
        product_id = row[0]
        buy_frequency = row[1]
        views = row[2]
        buy_without_discount_frequency = row[3]
        buy_5_discount_frequency = row[4]
        buy_10_discount_frequency = row[5]
        buy_15_discount_frequency = row[6]
        buy_20_discount_frequency = row[7]
        buy_discount_frequency = row[8]
        return cls(product_id,
                 buy_frequency,
                 views,
                 buy_without_discount_frequency,
                 buy_5_discount_frequency,
                 buy_10_discount_frequency,
                 buy_15_discount_frequency,
                 buy_20_discount_frequency,
                 buy_discount_frequency)
