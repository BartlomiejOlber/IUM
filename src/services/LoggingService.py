import pandas as pd
import numpy as np
class LoggingService():

    def __init__(self, userDataRepository, productDataRepository, userPerProductDataRepository):
        self.userDataRepository = userDataRepository
        self.productDataRepository = productDataRepository
        self.userPerProductDataRepository = userPerProductDataRepository

    def log(self, user_id, product_id, isBought, discount):

        user= self.userDataRepository.getUser(user_id)
        product= self.productDataRepository.getProduct(product_id)
        userPerProduct= self.userPerProductDataRepository.getUserPerProduct(user_id, product_id)

        entities = [user, product, userPerProduct]
        if isBought:
            for entity in entities:
                entity.buy_frequency = ((entity.buy_frequency * entity.views) + 1) / entity.views
                if discount == 0:
                    entity.buy_without_discount_frequency = ((entity.buy_without_discount_frequency *
                                                              entity.views) + 1) / entity.views


                if discount == 5:
                    entity.buy_5_discount_frequency = ((entity.buy_5_discount_frequency *
                                                        entity.views) + 1) / entity.views


                if discount == 10:
                    entity.buy_10_discount_frequency = ((entity.buy_10_discount_frequency *
                                                         entity.views) + 1) / entity.views


                if discount == 15:
                    entity.buy_15_discount_frequency = ((entity.buy_15_discount_frequency *
                                                         entity.views) + 1) / entity.views


                if discount == 20:
                    entity.buy_20_discount_frequency = ((entity.buy_20_discount_frequency *
                                                         entity.views) + 1) / entity.views


                if discount != 0:
                    entity.buy_discount_frequency = ((entity.buy_discount_frequency *
                                                      entity.views) + 1) / entity.views

        else:
            user.views = user.views + 1
            product.views = product.views + 1
            userPerProduct.views = userPerProduct.views + 1

        self.userDataRepository.updateUser(user)
        self.productDataRepository.updateProduct(product)
        self.userPerProductDataRepository.updateUserPerProduct(userPerProduct)
        return True

    def logAndSplitFromJsonl(self, sessionsJsonlPath, sessionsTrainPath, sessionsTestPath):
        sessions = pd.read_json(sessionsJsonlPath, lines=True, orient='records')

        sessions.sort_values(by=['timestamp'], inplace=True, ascending=True)

        sessionsTrain = sessions.iloc[ 0:int(0.8*len(sessions)) , : ]
        sessionsTest = sessions.iloc[ int(0.8*len(sessions)) : len(sessions) , : ]
        sessionsTrain.to_json(sessionsTrainPath, orient='records', lines=True)
        sessionsTest.to_json(sessionsTestPath, orient='records', lines=True)

        for index, row in sessionsTrain.iterrows():

            # TODO: check if entity exist and if not add new
            user = self.userDataRepository.getUser(row.user_id)
            product = self.productDataRepository.getProduct(row.product_id)
            userPerProduct = self.userPerProductDataRepository.getUserPerProduct(row.user_id, row.product_id)

            entities = [user, product, userPerProduct]
            isBought = False
            if row.event_type == "BUY_PRODUCT":
                isBought = True

            discount = row.offered_discount
            if isBought:
                for entity in entities:
                    entity.buy_frequency = ((entity.buy_frequency * entity.views) + 1) / entity.views
                    if discount == 0:
                        entity.buy_without_discount_frequency = ((entity.buy_without_discount_frequency *
                                                                  entity.views) + 1) / entity.views

                    if discount == 5:
                        entity.buy_5_discount_frequency = ((entity.buy_5_discount_frequency *
                                                            entity.views) + 1) / entity.views

                    if discount == 10:
                        entity.buy_10_discount_frequency = ((entity.buy_10_discount_frequency *
                                                             entity.views) + 1) / entity.views

                    if discount == 15:
                        entity.buy_15_discount_frequency = ((entity.buy_15_discount_frequency *
                                                             entity.views) + 1) / entity.views

                    if discount == 20:
                        entity.buy_20_discount_frequency = ((entity.buy_20_discount_frequency *
                                                             entity.views) + 1) / entity.views

                    if discount != 0:
                        entity.buy_discount_frequency = ((entity.buy_discount_frequency *
                                                          entity.views) + 1) / entity.views

            else:
                user.views = user.views + 1
                product.views = product.views + 1
                userPerProduct.views = userPerProduct.views + 1

            self.userDataRepository.updateUser(user)
            self.productDataRepository.updateProduct(product)
            self.userPerProductDataRepository.updateUserPerProduct(userPerProduct)
        return True