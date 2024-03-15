import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_input_hidden = np.random.randn(1, self.hidden_size)
        
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_hidden_output = np.random.randn(1, self.output_size)
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def forward(self, inputs):
        # Input to hidden layer
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_input)
        
        # Hidden to output layer
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_hidden_output
        self.output_layer_output = self.sigmoid(self.output_layer_input)
        
        return self.output_layer_output

# Example usage
input_size = 2
hidden_size = 3
output_size = 1

# Create neural network
nn = NeuralNetwork(input_size, hidden_size, output_size)

# Example input
inputs = np.array([[0, 1]])

# Perform forward pass
output = nn.forward(inputs)
print("Output:", output)
