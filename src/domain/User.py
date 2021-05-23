from src.domain.BasicEntityData import BasicEntityData


class User(BasicEntityData):

    def __init__(self, user_id,
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

    @classmethod
    def fromRow(cls, row):
        user_id = row[0]
        buy_frequency = row[1]
        views = row[2]
        buy_without_discount_frequency = row[3]
        buy_5_discount_frequency = row[4]
        buy_10_discount_frequency = row[5]
        buy_15_discount_frequency = row[6]
        buy_20_discount_frequency = row[7]
        buy_discount_frequency = row[8]
        return cls(user_id,
                   buy_frequency,
                   views,
                   buy_without_discount_frequency,
                   buy_5_discount_frequency,
                   buy_10_discount_frequency,
                   buy_15_discount_frequency,
                   buy_20_discount_frequency,
                   buy_discount_frequency)