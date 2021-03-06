import sqlite3

from src.domain.UserPerProduct import UserPerProduct


class UserPerProductDataRepository():

    def __init__(self, userPerProductDataBasePath):
        self.userPerProductDataBasePath = userPerProductDataBasePath

    def createUserPerProductTable(self):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("CREATE TABLE USER_PER_PRODUCT "
                    "(USER_ID INTEGER NOT NULL ,"
                    "PRODUCT_ID INTEGER NOT NULL ,"
                    "BUY_FREQUENCY FLOAT NOT NULL,"
                    "VIEWS INTEGER NOT NULL,"
                    "BUY_WITHOUT_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                    "BUY_5_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                    "BUY_10_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                    "BUY_15_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                    "BUY_20_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                    "BUY_DISCOUNT_FREQUENCY FLOAT NOT NULL,"
                    "PRIMARY KEY (USER_ID, PRODUCT_ID),"
                    "FOREIGN KEY(USER_ID) REFERENCES USERS(USER_ID),"
                    "FOREIGN KEY(PRODUCT_ID) REFERENCES PRODUCTS(PRODUCT_ID))")
        conToDataBase.commit()

    def deleteUserPerProductTable(self):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("DROP TABLE USER_PER_PRODUCT")
        conToDataBase.commit()

    def getUserPerProduct(self, user_id, product_id):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT * FROM USER_PER_PRODUCT "
                    "WHERE USER_ID=? AND PRODUCT_ID=?", (user_id, product_id))
        row = cur.fetchone()

        if row == None:
            cur.execute("INSERT INTO USER_PER_PRODUCT (USER_ID,PRODUCT_ID, "
                        "BUY_FREQUENCY, "
                        "VIEWS,"
                        "BUY_WITHOUT_DISCOUNT_FREQUENCY,"
                        "BUY_5_DISCOUNT_FREQUENCY,"
                        "BUY_10_DISCOUNT_FREQUENCY,"
                        "BUY_15_DISCOUNT_FREQUENCY,"
                        "BUY_20_DISCOUNT_FREQUENCY,"
                        "BUY_DISCOUNT_FREQUENCY) "
                        "VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (user_id, product_id,
                         0, 1, 0, 0, 0, 0, 0, 0))
            conToDataBase.commit()
            row = [user_id, product_id, 0, 1, 0, 0, 0, 0, 0, 0]

        return UserPerProduct.fromRow(row)

    def updateUserPerProduct(self, userPerProduct):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("UPDATE USER_PER_PRODUCT "
                    "SET BUY_FREQUENCY = ?,"
                    "VIEWS = ?,"
                    "BUY_WITHOUT_DISCOUNT_FREQUENCY = ?,"
                    "BUY_5_DISCOUNT_FREQUENCY = ?,"
                    "BUY_10_DISCOUNT_FREQUENCY = ?,"
                    "BUY_15_DISCOUNT_FREQUENCY = ?,"
                    "BUY_20_DISCOUNT_FREQUENCY = ?,"
                    "BUY_DISCOUNT_FREQUENCY = ?"
                    "WHERE USER_ID=?"
                    "AND PRODUCT_ID=?", (userPerProduct.buy_frequency,
                                         userPerProduct.views,
                                         userPerProduct.buy_without_discount_frequency,
                                         userPerProduct.buy_5_discount_frequency,
                                         userPerProduct.buy_10_discount_frequency,
                                         userPerProduct.buy_15_discount_frequency,
                                         userPerProduct.buy_20_discount_frequency,
                                         userPerProduct.buy_discount_frequency,
                                         userPerProduct.user_id,
                                         userPerProduct.product_id))
        conToDataBase.commit()

    def getBuyProductFrequency(self, user_id, product_id):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_FREQUENCY "
                    "FROM USER_PER_PRODUCT "
                    "WHERE USER_ID=? "
                    "AND PRODUCT_ID=?", (user_id, product_id))
        return cur.fetchone()

    def getProductViews(self, user_id, product_id):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT VIEWS "
                    "FROM USER_PER_PRODUCT "
                    "WHERE USER_ID=? "
                    "AND PRODUCT_ID=?", (user_id, product_id))
        return cur.fetchone()

    def get5DiscountFrequency(self, user_id, product_id):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_5_DISCOUNT_FREQUENCY "
                    "FROM USER_PER_PRODUCT "
                    "WHERE USER_ID=? "
                    "AND PRODUCT_ID=?", (user_id, product_id))
        return cur.fetchone()

    def get10DiscountFrequency(self, user_id, product_id):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_10_DISCOUNT_FREQUENCY "
                    "FROM USER_PER_PRODUCT "
                    "WHERE USER_ID=? "
                    "AND PRODUCT_ID=?", (user_id, product_id))
        return cur.fetchone()

    def get15DiscountFrequency(self, user_id, product_id):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_15_DISCOUNT_FREQUENCY "
                    "FROM USER_PER_PRODUCT "
                    "WHERE USER_ID=? "
                    "AND PRODUCT_ID=?", (user_id, product_id))
        return cur.fetchone()

    def get20DiscountFrequency(self, user_id, product_id):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_20_DISCOUNT_FREQUENCY "
                    "FROM USER_PER_PRODUCT "
                    "WHERE USER_ID=? "
                    "AND PRODUCT_ID=?", (user_id, product_id))
        return cur.fetchone()

    def getBuyDiscountFrequency(self, user_id, product_id):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_DISCOUNT_FREQUENCY "
                    "FROM USER_PER_PRODUCT "
                    "WHERE USER_ID=? "
                    "AND PRODUCT_ID=?", (user_id, product_id))
        return cur.fetchone()

    def getBuyWithoutFrequency(self, user_id, product_id):
        conToDataBase = sqlite3.connect(self.userPerProductDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_WITHOUT_DISCOUNT_FREQUENCY "
                    "FROM USER_PER_PRODUCT "
                    "WHERE USER_ID=? "
                    "AND PRODUCT_ID=?", (user_id, product_id))
        return cur.fetchone()
