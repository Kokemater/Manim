import numpy as np

# Función de activación (Sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Inicialización de los datos de entrada y salida esperada
inputs = np.array([[1.0, 0.0]])
expected_output = np.array([[0.0, 1.0]])

# Inicialización de los pesos y biases
W_1 = np.random.rand(2, 2)
b_1 = np.random.rand(1, 2)
W_2 = np.random.rand(2, 2)
b_2 = np.random.rand(1, 2)

# Parámetros de aprendizaje
learning_rate = 0.1
epochs = 10000

# Entrenamiento de la red neuronal
for epoch in range(epochs):
    # Forward propagation
    Z_1 = np.dot(inputs, W_1) + b_1
    A_1 = sigmoid(Z_1)
    
    Z_2 = np.dot(A_1, W_2) + b_2
    A_2 = sigmoid(Z_2)
    
    # Cálculo del error
    dCda_2 = -(expected_output - A_2)
    da_2dz_2 = sigmoid_derivative(Z_2)
    d_output = dCda_2 * da_2dz_2

    error_hidden_layer = d_output.dot(W_2.T)
    d_hidden = error_hidden_layer * sigmoid_derivative(Z_1)
    
    # Gradient descent
    W_2 -= learning_rate * A_1.T.dot(d_output)
    b_2 -= learning_rate * d_output
    
    W_1 -= learning_rate * d_hidden.T.dot(inputs)
    b_1 -= learning_rate * d_hidden

# Resultado final después del entrenamiento
print("Pesos de la capa oculta después del entrenamiento:\n", W_1)
print("Biases de la capa oculta después del entrenamiento:\n", b_1)
print("Pesos de la capa de salida después del entrenamiento:\n", W_2)
print("Biases de la capa de salida después del entrenamiento:\n", b_2)

print("\nSalidas finales después del entrenamiento:\n", A_2)

print(f"MSE {0.5*((inputs[0][0] - A_1[0][0])**2 + (inputs[0][1] - A_1[0][1])**2)}")
