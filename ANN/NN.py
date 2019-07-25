import numpy as np
import pandas as pd

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.y          = y              
        self.output     = np.zeros(self.y.shape)
        self.weights11   = np.random.rand(self.input.shape[1], self.input.shape[0]) 
        self.weights12   = np.random.rand(self.input.shape[1], self.input.shape[0])
        self.weights21   = np.random.rand(self.y.shape[0], self.y.shape[1])
        self.weights22   = np.random.rand(self.y.shape[0], self.y.shape[1])
        
    def feedforward(self):
        self.neuron11 = sigmoid(np.dot(self.input, self.weights11))   # 1st Layer : 1st Neuron
        self.neuron12 = sigmoid(np.dot(self.input, self.weights12))   # 1st Layer : 2nd Neuron
        self.output = sigmoid(np.dot(self.neuron11, self.weights21) + np.dot(self.neuron12, self.weights22)) # 2nd Layer : 1 Output

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights21 = np.dot(self.neuron11.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights22 = np.dot(self.neuron12.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights11 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights21.T) * sigmoid_derivative(self.neuron11)))
        d_weights12 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights22.T) * sigmoid_derivative(self.neuron12)))

        # update the weights with the derivative (slope) of the loss function
        self.weights11 += d_weights11
        self.weights12 += d_weights12
        self.weights21 += d_weights21
        self.weights22 += d_weights22

    # def predict(self, testing_data):
    #     self.layer1 = sigmoid(np.dot(testing_data, self.weights1))
    #     self.output = sigmoid(np.dot(self.layer1, self.weights2))
    #     return self.output

if __name__ == "__main__":
    # Data Location
    rawdata = r'D:\code\ANN\rawdata_edited.xlsx'

    # Training Set Data
    training_set = pd.read_excel(rawdata, sheetname=1)
    # training_set = training_set.head(400)
    training_set_inputs = np.array(training_set.loc[0:200, ['Suhu', 'Kelembapan']])
    training_set_outputs = np.array(training_set.loc[0:200, ['Label']])

    # Testing Set Data
    testing_set = pd.read_excel(rawdata, sheetname=2)
    # testing_set = testing_set.head(40)
    testing_set_inputs = np.array(testing_set.loc[0:100, ['Suhu','Kelembapan']])   
    testing_set_outputs = np.array(testing_set.loc[0:100, ['Label']])

    # Training Neural Network
    nn = NeuralNetwork(training_set_inputs, training_set_outputs)
    epoch = 10000
    for i in range(epoch):
        nn.feedforward()
        nn.backprop()
    print(nn.output)
    print()

    # # Testing Neural Network
    # prediction = nn.predict(testing_set_inputs)

    # print(prediction)
    # print()
    # print(testing_set_outputs)
    # print()
