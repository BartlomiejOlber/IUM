
class LoggingService():

    def __init__(self, userDataRepository, productDataRepository):
        self.userDataRepository = userDataRepository
        self.productDataRepository = productDataRepository

    def log(self, user_id, product_id):

        return True