import pandas as pd
import tensorflow as tf
from tensorflow import keras

class ModelB():

    def __init__(self):
        self.model = self.createModel()

    def createModel(self):

        model = keras.Sequential()
        model.add(keras.Input(shape=(20)))

        model.add(keras.layers.BatchNormalization())
        model.add(keras.Dropout(0.2))
        model.add(
            keras.layers.Dense(100, activation=keras.layers.LeakyReLU(alpha=0.2),
                         kernel_initializer=keras.initializers.he_uniform))

        model.add(keras.layers.BatchNormalization())
        model.add(keras.Dropout(0.2))
        model.add(
            keras.layers.Dense(50, activation=keras.layers.LeakyReLU(alpha=0.2),
                         kernel_initializer=keras.initializers.he_uniform))

        model.add(keras.layers.BatchNormalization())
        model.add(keras.Dropout(0.2))
        model.add(
            keras.layers.Dense(10, activation=keras.layers.LeakyReLU(alpha=0.2),
                         kernel_initializer=keras.initializers.he_uniform))


        model.add(keras.layers.Dense(1, activation=keras.activations.logistic))
        model.compile(optimizer=keras.optimizers.Nadam(clipnorm=1, learning_rate=3e-2),
                      loss=keras.losses.CrossEntropy())




    def train(self,
              xTrain, yTrain):
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=10,
                                                          restore_best_weights=True)
        self.model.fit(xTrain, yTrain, callbacks=early_stopping_cb)

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
                uesrDifferenceThisProductBiggerLower):
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
             uesrDifferenceThisProductBiggerLower]
        return self.model.predict(x)