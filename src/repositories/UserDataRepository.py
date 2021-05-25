import sqlite3

from src.domain.User import User


class UserDataRepository():

    def __init__(self, userDataBasePath):
        self.userDataBasePath = userDataBasePath


    def createUsersTable(self):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("CREATE TABLE USERS "
                         "(USER_ID INTEGER PRIMARY KEY NOT NULL ,"
                         "BUY_FREQUENCY FLOAT NOT NULL,"
                         "VIEWS INTEGER NOT NULL,"
                         "BUY_WITHOUT_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_5_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_10_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_15_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_20_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                         "BUY_DISCOUNT_FREQUENCY FLOAT NOT NULL)")
        conToDataBase.commit()

    def deleteUsersTable(self):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("DROP TABLE USERS")
        conToDataBase.commit()

    def getUser(self, user_id):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT * FROM USERS WHERE USER_ID=?", (user_id,))
        row = cur.fetchone()
        if row == None:
            cur.execute("INSERT INTO USERS (USER_ID, "
                             "BUY_FREQUENCY, "
                             "VIEWS,"
                             "BUY_WITHOUT_DISCOUNT_FREQUENCY,"
                             "BUY_5_DISCOUNT_FREQUENCY,"
                             "BUY_10_DISCOUNT_FREQUENCY,"
                             "BUY_15_DISCOUNT_FREQUENCY,"
                             "BUY_20_DISCOUNT_FREQUENCY,"
                             "BUY_DISCOUNT_FREQUENCY) "
                             "VALUES (?,?,?,?,?,?,?,?,?)",
                             (user_id,
                              0,1,0,0,0,0,0,0))
            conToDataBase.commit()
            row = [user_id,0,1,0,0,0,0,0,0]

        return User.fromRow(row)

    def updateUser(self, user):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("UPDATE USERS "
                         "SET BUY_FREQUENCY = ?,"
                         "VIEWS = ?,"
                         "BUY_WITHOUT_DISCOUNT_FREQUENCY = ?,"
                         "BUY_5_DISCOUNT_FREQUENCY = ?,"
                         "BUY_10_DISCOUNT_FREQUENCY = ?,"
                         "BUY_15_DISCOUNT_FREQUENCY = ?,"
                         "BUY_20_DISCOUNT_FREQUENCY = ?,"
                         "BUY_DISCOUNT_FREQUENCY = ?"
                         "WHERE USER_ID=?", (user.buy_frequency,
                                             user.views,
                                             user.buy_without_discount_frequency,
                                             user.buy_5_discount_frequency,
                                             user.buy_10_discount_frequency,
                                             user.buy_15_discount_frequency,
                                             user.buy_20_discount_frequency,
                                             user.buy_discount_frequency,
                                             user.user_id))
        conToDataBase.commit()

    def getBuyFrequency(self, user_id):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_FREQUENCY FROM USERS WHERE USER_ID=?", (user_id,))
        return cur.fetchone()

    def get5DiscountFrequency(self, user_id):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_5_DISCOUNT_FREQUENCY FROM USERS WHERE USER_ID=?", (user_id,))
        return cur.fetchone()

    def get10DiscountFrequency(self, user_id):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_10_DISCOUNT_FREQUENCY FROM USERS WHERE USER_ID=?", (user_id,))
        return cur.fetchone()

    def get15DiscountFrequency(self, user_id):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_15_DISCOUNT_FREQUENCY FROM USERS WHERE USER_ID=?", (user_id,))
        return cur.fetchone()

    def get20DiscountFrequency(self, user_id):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_20_DISCOUNT_FREQUENCY FROM USERS WHERE USER_ID=?", (user_id,))
        return cur.fetchone()

    def getBuyDiscountFrequency(self, user_id):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_DISCOUNT_FREQUENCY FROM USERS WHERE USER_ID=?", (user_id,))
        return cur.fetchone()

    def getBuyWithoutFrequency(self, user_id):
        conToDataBase = sqlite3.connect(self.userDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_WITHOUT_DISCOUNT_FREQUENCY FROM USERS WHERE USER_ID=?", (user_id,))
        return cur.fetchone()
