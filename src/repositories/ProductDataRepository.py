import sqlite3

from src.domain.Product import Product


class ProductDataRepository():

    def __init__(self, productDataBasePath):
        self.productDataBasePath = productDataBasePath

    def createUsersTable(self):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("CREATE TABLE PRODUCTS "
                         "(PRODUCT_ID INTEGER PRIMARY KEY NOT NULL ,"
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
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("DROP TABLE PRODUCTS")
        conToDataBase.commit()

    def getProduct(self, product_id):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT * FROM PRODUCTS WHERE PRODUCT_ID=?", (product_id,))
        row = cur.fetchone()

        if row == None:
            cur.execute("INSERT INTO PRODUCTS (PRODUCT_ID, "
                             "BUY_FREQUENCY, "
                             "VIEWS,"
                             "BUY_WITHOUT_DISCOUNT_FREQUENCY,"
                             "BUY_5_DISCOUNT_FREQUENCY,"
                             "BUY_10_DISCOUNT_FREQUENCY,"
                             "BUY_15_DISCOUNT_FREQUENCY,"
                             "BUY_20_DISCOUNT_FREQUENCY,"
                             "BUY_DISCOUNT_FREQUENCY) "
                             "VALUES (?,?,?,?,?,?,?,?,?)",
                             (product_id,
                              0,1,0,0,0,0,0,0))
            conToDataBase.commit()
            row = [product_id,0,1,0,0,0,0,0,0]

        return Product.fromRow(row)

    def updateProduct(self, product):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("UPDATE PRODUCTS "
                         "SET BUY_FREQUENCY = ?,"
                         "VIEWS = ?,"
                         "BUY_WITHOUT_DISCOUNT_FREQUENCY = ?,"
                         "BUY_5_DISCOUNT_FREQUENCY = ?,"
                         "BUY_10_DISCOUNT_FREQUENCY = ?,"
                         "BUY_15_DISCOUNT_FREQUENCY = ?,"
                         "BUY_20_DISCOUNT_FREQUENCY = ?,"
                         "BUY_DISCOUNT_FREQUENCY = ?"
                         "WHERE PRODUCT_ID=?", (product.buy_frequency,
                                                product.views,
                                                product.buy_without_discount_frequency,
                                                product.buy_5_discount_frequency,
                                                product.buy_10_discount_frequency,
                                                product.buy_15_discount_frequency,
                                                product.buy_20_discount_frequency,
                                                product.buy_discount_frequency,
                                                product.product_id))
        conToDataBase.commit()

    def getBuyProductFrequency(self,product_id):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_FREQUENCY FROM PRODUCTS WHERE PRODUCT_ID=?", (product_id,))
        return cur.fetchone()

    def getProductViews(self, product_id):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT VIEWS FROM PRODUCTS WHERE PRODUCT_ID=?", (product_id,))
        return cur.fetchone()

    def get5DiscountFrequency(self, product_id):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_5_DISCOUNT_FREQUENCY FROM PRODUCTS WHERE PRODUCT_ID=?", (product_id,))
        return cur.fetchone()

    def get10DiscountFrequency(self, product_id):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_10_DISCOUNT_FREQUENCY FROM PRODUCTS WHERE PRODUCT_ID=?", (product_id,))
        return cur.fetchone()

    def get15DiscountFrequency(self, product_id):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_15_DISCOUNT_FREQUENCY FROM PRODUCTS WHERE PRODUCT_ID=?", (product_id,))
        return cur.fetchone()

    def get20DiscountFrequency(self, product_id):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_20_DISCOUNT_FREQUENCY FROM PRODUCTS WHERE PRODUCT_ID=?", (product_id,))
        return cur.fetchone()

    def getBuyDiscountFrequency(self, product_id):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_DISCOUNT_FREQUENCY FROM PRODUCTS WHERE PRODUCT_ID=?", (product_id,))
        return cur.fetchone()

    def getBuyWithoutFrequency(self, product_id):
        conToDataBase = sqlite3.connect(self.productDataBasePath)
        cur = conToDataBase.cursor()
        cur.execute("SELECT BUY_WITHOUT_DISCOUNT_FREQUENCY FROM PRODUCTS WHERE PRODUCT_ID=?", (product_id,))
        return cur.fetchone()
