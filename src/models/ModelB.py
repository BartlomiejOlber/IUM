import pandas as pd
import tensorflow as tf
from tensorflow import keras

class ModelB():

    def __init__(self, modelSavePath):
        self.model = self.createModel()
        self.modelSavePath = modelSavePath

        if modelSavePath.is_file():
            self.model = keras.models.load_model(modelSavePath)

    def createModel(self):

        model = keras.Sequential()
        model.add(keras.Input(shape=(20)))

        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Dropout(0.2))
        model.add(
            keras.layers.Dense(100, activation=keras.layers.LeakyReLU(alpha=0.2),
                         kernel_initializer=keras.initializers.he_uniform))

        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Dropout(0.2))
        model.add(
            keras.layers.Dense(50, activation=keras.layers.LeakyReLU(alpha=0.2),
                         kernel_initializer=keras.initializers.he_uniform))

        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Dropout(0.2))
        model.add(
            keras.layers.Dense(10, activation=keras.layers.LeakyReLU(alpha=0.2),
                         kernel_initializer=keras.initializers.he_uniform))


        model.add(keras.layers.Dense(1, activation=keras.activations.softmax))
        model.compile(optimizer=keras.optimizers.Nadam(clipnorm=1, learning_rate=3e-2),
                      loss=keras.losses.BinaryCrossentropy())




    def train(self,
              xTrain, yTrain):
        # early_stopping_cb = keras.callbacks.EarlyStopping(patience=10,
        #                                                   restore_best_weights=True)
        self.model.fit(xTrain, yTrain, epochs=100)
        self.model.save(self.modelSavePath)

    def predict(self,
                discount,
                buyingProductFrequency,
                buyingFrequency,
                userBuyingProductFrequency,
                buyingWithBiggerDiscountFrequency,
                buyingWithLowerDiscountFrequency,
                buyingWithDiscountFrequency,
                buyingWithoutDiscountFrequency,
                buyingThisProductWithBiggerDiscountFrequency,
                buyingThisProductWithLowerDiscountFrequency,
                buyingThisProductWithDiscountFrequency,
                buyingThisProductWithoutDiscountFrequency,
                userBuyingThisProductWithBiggerDiscountFrequency,
                userBuyingThisProductWithLowerDiscountFrequency,
                userBuyingThisProductWithDiscountFrequency,
                userBuyingThisProductWithoutDiscountFrequency,
                differenceBiggerLower,
                differenceDiscountWithout,
                differenceThisProductBiggerLower,
                userDifferenceThisProductBiggerLower):
        x = [discount,
             buyingProductFrequency,
             buyingFrequency,
             userBuyingProductFrequency,
             buyingWithBiggerDiscountFrequency,
             buyingWithLowerDiscountFrequency,
             buyingWithDiscountFrequency,
             buyingWithoutDiscountFrequency,
             buyingThisProductWithBiggerDiscountFrequency,
             buyingThisProductWithLowerDiscountFrequency,
             buyingThisProductWithDiscountFrequency,
             buyingThisProductWithoutDiscountFrequency,
             userBuyingThisProductWithBiggerDiscountFrequency,
             userBuyingThisProductWithLowerDiscountFrequency,
             userBuyingThisProductWithDiscountFrequency,
             userBuyingThisProductWithoutDiscountFrequency,
             differenceBiggerLower,
             differenceDiscountWithout,
             differenceThisProductBiggerLower,
             userDifferenceThisProductBiggerLower]
        return self.model.predict(x)