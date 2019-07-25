#ANN_2.py : Program ANN sederhana
#Ridhan Fadhilah
#19-02-2019

# Library
from numpy import exp, array, asarray, random, dot, mean
import pandas as pd

# Neural Network Object
class NeuralNetwork():
    # Initiazion
    def __init__(self):
        random.seed(1)
        self.synaptic_weights = 2 * random.random((2, 1)) - 1
        self.synaptic_bias = random.random()

    # Sigmoid Function
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))    

    # Slope Function
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # Train Function
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            prediction_output = self.think(training_set_inputs)

            error = training_set_outputs - prediction_output
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(prediction_output))
            self.synaptic_weights += adjustment
            
            # Cost Function for Synaptic Bias
            cost = 0.5 * dot(error, error.T) / len(error)
            slope_of_cost =  mean(error)
            self.synaptic_bias -= (0.1 * slope_of_cost)

    # Think Function
    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights) + self.synaptic_bias)

# Main Program
if __name__ == "__main__":

    # Intialise a single neuron neural network.
    neural_network = NeuralNetwork()

    print("Random starting synaptic weights: ")
    print(neural_network.synaptic_weights)
    print()

    # Data Location
    berkas = r'D:\code\ANN\rawdata_edited.xlsx'

    # Training Set Data
    training_set = pd.read_excel(berkas, sheetname=1)
    training_set_inputs = []
    training_set_outputs = []
    for data in training_set.head(300).itertuples():
        training_set_inputs.append([data[1],data[2]])
        training_set_outputs.append([data[4]])
    
    training_set_inputs = array(training_set_inputs)
    training_set_outputs = array(training_set_outputs)

    # Test Set Data
    test_set = pd.read_excel(berkas, sheetname=2)
    test_set_inputs = []
    test_set_outputs = []
    for data in test_set.head().itertuples():
        test_set_inputs.append([data[1],data[2]])
        test_set_outputs.append([data[4]])

    test_set_inputs = array(test_set_inputs)   
    test_set_outputs = array(test_set_outputs)

    # Train 10.000 times
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print("New synaptic weights after training: ")
    print(neural_network.synaptic_weights)
    print()

    # Test a new data with Neural Network
    print("Perdiction for new situation: ")
    result = neural_network.think(test_set_inputs)
    error = (result - test_set_outputs)
    print(result)
    print()
    print(mean(error))
