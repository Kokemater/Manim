import numpy as np

# Función de activación (sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide (para el cálculo del gradiente)
def sigmoid_derivada(x):
    return x * (1 - x)

# Datos de entrada (4 ejemplos, 3 características cada uno)
X = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [0, 0, 0],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 0],
              [1, 1, 1],
              ])

# A3s esperadas (para un problema de clasificación binaria)
y = np.array([[0],
              [0],
              [0],
              [0],
              [1],
              [1],
              [1],
              [1]])

# Semilla para obtener resultados reproducibles
np.random.seed(42)

# Inicialización de los pesos y bias (valores aleatorios pequeños)
W1 = np.random.rand(3, 4) - 0.5
b1 = np.random.rand(1, 4) - 0.5

W2 = np.random.rand(4, 4) - 0.5
b2 = np.random.rand(1, 4) - 0.5

W3 = np.random.rand(4, 1) - 0.5
b3 = np.random.rand(1, 1) - 0.5

# Parámetros de entrenamiento
epochs = 10000
learning_rate = 0.1

# Entrenamiento de la red
for epoch in range(epochs):
    # Propagación hacia adelante
    A1 = sigmoid(np.dot(X, W1) + b1)
    A2 = sigmoid(np.dot(A1, W2) + b2)
    A3 = sigmoid(np.dot(A2, W3) + b3)
    
    # Cálculo del error utilizando MSE
    mse = np.mean(np.square(y - A3))
    # Backpropagation utilizando el gradiente del MSE
    error_A3 = -1*(y - A3)
    
    delta_A3 = error_A3 * sigmoid_derivada(A3)
    delta_A2 = delta_A3.dot(W3.T) * sigmoid_derivada(A2)
    delta_A1 = delta_A2.dot(W2.T) * sigmoid_derivada(A1)
    
    # Actualización de los pesos y bias
    W3 -= A2.T.dot(delta_A3) * learning_rate
    b3 -= np.sum(delta_A3, axis=0, keepdims=True) * learning_rate
    
    W2 -= A1.T.dot(delta_A2) * learning_rate
    b2 -= np.sum(delta_A2, axis=0, keepdims=True) * learning_rate
    
    W1 -= X.T.dot(delta_A1) * learning_rate
    b1 -= np.sum(delta_A1, axis=0, keepdims=True) * learning_rate

# Resultados después del entrenamiento
print("A3 final después del entrenamiento:")
print(A3)

# Imprimir el valor del MSE al final del entrenamiento
print(f"Error cuadrático medio final (MSE): {mse}")