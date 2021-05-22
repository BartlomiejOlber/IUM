import sqlite3

class UserDataRepository():

    def __init__(self, userDataBasePath):
        self.conToDataBase = sqlite3.connect(userDataBasePath)
        self.cur = self.conToDataBase.cursor()

    def createUsersTable(self):
        self.cur.execute("CREATE TABLE USERS "
                         "(USER_ID INTEGER PRIMARY KEY NOT NULL ,"
                         "BUY_FREQUENCY FLOAT NOT NULL,"
                         "BUY_WITHOUT_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_5_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_10_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_15_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_20_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_DISCOUNT_FREQUENCY FLOAT NOT NULL)")
        self.conToDataBase.commit()

    def deleteUsersTable(self):
        self.cur.execute("DROP TABLE USERS")
        self.conToDataBase.commit()

    def getBuyFrequency(user_id):

        return 1

    def get5DiscountFrequency(user_id):

        return 1

    def get10DiscountFrequency(user_id):

        return 1

    def get15DiscountFrequency(user_id):

        return 1

    def get20DiscountFrequency(user_id):

        return 1

    def getBuyDiscountFrequency(user_id):

        return 1

    def getBuyWithoutFrequency(user_id):

        return 1
