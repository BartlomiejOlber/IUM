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
        model.add(keras.layers.InputLayer(input_shape=(20,)))

        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Dropout(0.2))
        model.add(
            keras.layers.Dense(50, activation=keras.layers.ReLU(),
                         kernel_initializer=keras.initializers.he_uniform))

        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Dropout(0.2))
        model.add(
            keras.layers.Dense(30, activation=keras.layers.ReLU(),
                         kernel_initializer=keras.initializers.he_uniform))
        #
        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Dropout(0.2))
        model.add(
            keras.layers.Dense(20, activation=keras.layers.ReLU(),
                         kernel_initializer=keras.initializers.he_uniform))


        model.add(keras.layers.Dense(1, activation=keras.activations.softmax))
        model.compile(optimizer=keras.optimizers.Nadam(clipnorm=1, learning_rate=3e-2),
                      loss=keras.losses.BinaryCrossentropy(), metrics=['accuracy'])

        return model



    def train(self, xTrain, yTrain, xTrainValidation, yTrainValidation ):
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=10,
                                                          restore_best_weights=True)
        xTrain = xTrain.astype('float')
        yTrain = pd.DataFrame(yTrain,columns=['Bought'])
        yTrain = yTrain.astype('float')

        xTrainValidation = xTrainValidation.astype('float')
        yTrainValidation = pd.DataFrame(yTrainValidation,columns=['Bought'])
        yTrainValidation = yTrainValidation.astype('float')


        self.model.fit(xTrain, yTrain, validation_data=(xTrainValidation, yTrainValidation), epochs=100,
                       callbacks=[early_stopping_cb])
        self.model.save(self.modelSavePath)

    def predict(self,specimen):
        return self.model.predict(specimen)