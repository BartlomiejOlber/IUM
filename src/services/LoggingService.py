import pandas as pd
import numpy as np


class LoggingService():

    def __init__(self, userDataRepository, productDataRepository, userPerProductDataRepository):
        self.userDataRepository = userDataRepository
        self.productDataRepository = productDataRepository
        self.userPerProductDataRepository = userPerProductDataRepository

    def log(self, user_id, product_id, isBought, discount):

        user = self.userDataRepository.getUser(user_id)
        product = self.productDataRepository.getProduct(product_id)
        userPerProduct = self.userPerProductDataRepository.getUserPerProduct(user_id, product_id)

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

        sessionsTrain = sessions.iloc[0:int(0.8 * len(sessions)), :]
        sessionsTest = sessions.iloc[int(0.8 * len(sessions)): len(sessions), :]
        sessionsTrain.to_json(sessionsTrainPath, orient='records', lines=True)
        sessionsTest.to_json(sessionsTestPath, orient='records', lines=True)

        users = sessionsTrain.groupby("user_id").user_id.unique()
        products = sessionsTrain.groupby("product_id").product_id.unique()

        for userA in users:
            user = int(userA[0])
            thisUser = sessionsTrain[sessionsTrain['user_id'] == user]
            views = int(len(thisUser[thisUser['event_type'] == "VIEW_PRODUCT"].index))
            userDTO = self.userDataRepository.getUser(user)
            userDTO.buy_frequency = float(len(thisUser[thisUser['event_type'] == "BUY_PRODUCT"].index) / views)
            userDTO.buy_without_discount_frequency = \
                float(len(thisUser[thisUser['event_type'] == "BUY_PRODUCT"][
                          thisUser['offered_discount'] == 0].index) / views)
            userDTO.buy_5_discount_frequency = float(len(thisUser[thisUser['event_type'] == "BUY_PRODUCT"][
                                                         thisUser['offered_discount'] == 5].index) / views)
            userDTO.buy_10_discount_frequency = float(len(thisUser[thisUser['event_type'] == "BUY_PRODUCT"][
                                                          thisUser['offered_discount'] == 10].index) / views)
            userDTO.buy_15_discount_frequency = float(len(thisUser[thisUser['event_type'] == "BUY_PRODUCT"][
                                                          thisUser['offered_discount'] == 15].index) / views)
            userDTO.buy_20_discount_frequency = float(len(thisUser[thisUser['event_type'] == "BUY_PRODUCT"][
                                                          thisUser['offered_discount'] == 20].index) / views)
            userDTO.buy_discount_frequency = float(len(thisUser[thisUser['event_type'] == "BUY_PRODUCT"][
                                                       thisUser['offered_discount'] != 0].index) / views)
            userDTO.views = views
            self.userDataRepository.updateUser(userDTO)

        for productA in products:
            product = int(productA[0])
            thisProduct = sessionsTrain[sessionsTrain['product_id'] == product]
            views = int(len(thisProduct[thisProduct['event_type'] == "VIEW_PRODUCT"].index))
            productDTO = self.productDataRepository.getProduct(product)
            productDTO.buy_frequency = float(len(thisProduct[thisProduct['event_type'] == "BUY_PRODUCT"].index) / views)
            productDTO.buy_without_discount_frequency = \
                float(len(thisProduct[thisProduct['event_type'] == "BUY_PRODUCT"][
                          thisProduct['offered_discount'] == 0].index) / views)
            productDTO.buy_5_discount_frequency = float(len(thisProduct[thisProduct['event_type'] == "BUY_PRODUCT"][
                                                            thisProduct['offered_discount'] == 5].index) / views)
            productDTO.buy_10_discount_frequency = float(len(thisProduct[thisProduct['event_type'] == "BUY_PRODUCT"][
                                                             thisProduct['offered_discount'] == 10].index) / views)
            productDTO.buy_15_discount_frequency = float(len(thisProduct[thisProduct['event_type'] == "BUY_PRODUCT"][
                                                             thisProduct['offered_discount'] == 15].index) / views)
            productDTO.buy_20_discount_frequency = float(len(thisProduct[thisProduct['event_type'] == "BUY_PRODUCT"][
                                                             thisProduct['offered_discount'] == 20].index) / views)
            productDTO.buy_discount_frequency = float(len(thisProduct[thisProduct['event_type'] == "BUY_PRODUCT"][
                                                          thisProduct['offered_discount'] != 0].index) / views)
            productDTO.views = views
            self.productDataRepository.updateProduct(productDTO)

        for userA in users:
            user = int(userA[0])
            for productA in products:
                product = int(productA[0])
                thisUsersProduct = sessionsTrain[sessionsTrain['user_id'] == user][
                    sessionsTrain['product_id'] == product]
                views = int(len(thisUsersProduct[thisUsersProduct['event_type'] == "VIEW_PRODUCT"].index))
                if views == 0:
                    views = 1
                userPerProduct = self.userPerProductDataRepository.getUserPerProduct(user, product)
                userPerProduct.buy_frequency = float(
                    len(thisUsersProduct[thisUsersProduct['event_type'] == "BUY_PRODUCT"].index) / views)
                userPerProduct.buy_without_discount_frequency = float(
                    len(thisUsersProduct[thisUsersProduct['event_type'] == "BUY_PRODUCT"][
                        thisUsersProduct['offered_discount'] == 0].index) / views)
                userPerProduct.buy_5_discount_frequency = \
                    float(len(thisUsersProduct[thisUsersProduct['event_type'] == "BUY_PRODUCT"][
                              thisUsersProduct['offered_discount'] == 5].index) / views)
                userPerProduct.buy_10_discount_frequency = \
                    float(len(thisUsersProduct[thisUsersProduct['event_type'] == "BUY_PRODUCT"][
                              thisUsersProduct['offered_discount'] == 10].index) / views)
                userPerProduct.buy_15_discount_frequency = \
                    float(len(thisUsersProduct[thisUsersProduct['event_type'] == "BUY_PRODUCT"][
                              thisUsersProduct['offered_discount'] == 15].index) / views)
                userPerProduct.buy_20_discount_frequency = \
                    float(len(thisUsersProduct[thisUsersProduct['event_type'] == "BUY_PRODUCT"][
                              thisUsersProduct['offered_discount'] == 20].index) / views)
                userPerProduct.buy_discount_frequency = \
                    float(len(thisUsersProduct[thisUsersProduct['event_type'] == "BUY_PRODUCT"][
                              thisUsersProduct['offered_discount'] != 0].index) / views)
                userPerProduct.views = views
                self.userPerProductDataRepository.updateUserPerProduct(userPerProduct)
        return True
