import numpy as np

# Función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Derivada de la función ReLU
def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Función de costo (error cuadrático medio)
def mean_squared_error(prediction, target):
    return 0.5 * np.square(prediction - target)

# Derivada de la función de costo respecto a la predicción
def mse_derivative(prediction, target):
    return prediction - target

# Pesos y sesgos iniciales
w1 = 0.5  # Peso de la capa de entrada a la capa oculta
b1 = 0.1  # Sesgo de la neurona en la capa oculta

w_out = 0.4  # Peso de la capa oculta a la capa de salida
b_out = 0.2  # Sesgo de la neurona en la capa de salida


# Entrada (tamaño de la casa en metros cuadrados) y el precio objetivo (en miles de dólares)
input_data = 50  # Tamaño de la casa
target = 300  # Precio de la casa

# Propagación hacia adelante
z1 = w1 * input_data + b1  # Entrada a la neurona de la capa oculta
a1 = relu(z1)  # Salida de la neurona de la capa oculta

z_out = w_out * a1 + b_out  # Entrada a la neurona de salida
prediction = z_out  # Como no aplicamos una función de activación en la salida, la predicción es z_out

print(f"Predicción inicial: {prediction}")

# Cálculo del error
error = mean_squared_error(prediction, target)
print(f"Error inicial: {error}")

# Tasa de aprendizaje
learning_rate = 0.00001

# Derivada del error con respecto a la salida de la red (z_out)
d_error_d_z_out = mse_derivative(prediction, target)

# Derivada de z_out respecto a los pesos y sesgos en la salida
d_z_out_d_w_out = a1
d_z_out_d_b_out = 1

# Actualización de pesos y sesgos de la capa de salida
w_out -= learning_rate * d_error_d_z_out * d_z_out_d_w_out
b_out -= learning_rate * d_error_d_z_out * d_z_out_d_b_out

# Derivada de z_out respecto a la salida de la capa oculta (a1)
d_z_out_d_a1 = w_out

# Derivada del error respecto a la salida de la capa oculta (a1)
d_error_d_a1 = d_error_d_z_out * d_z_out_d_a1

# Derivada de la salida de la capa oculta (a1) respecto a su entrada (z1)
d_a1_d_z1 = relu_derivative(z1)

# Derivada de z1 respecto a los pesos y sesgos en la capa oculta
d_z1_d_w1 = input_data
d_z1_d_b1 = 1

# Actualización de pesos y sesgos de la capa oculta
w1 -= learning_rate * d_error_d_a1 * d_a1_d_z1 * d_z1_d_w1
b1 -= learning_rate * d_error_d_a1 * d_a1_d_z1 * d_z1_d_b1

print(f"Peso w1 actualizado: {w1}")
print(f"Sesgo b1 actualizado: {b1}")
print(f"Peso w_out actualizado: {w_out}")
print(f"Sesgo b_out actualizado: {b_out}")

# Número de iteraciones de entrenamiento
epochs = 1000

for epoch in range(epochs):
    # Propagación hacia adelante
    z1 = w1 * input_data + b1
    a1 = relu(z1)

    z_out = w_out * a1 + b_out
    prediction = z_out

    # Cálculo del error
    error = mean_squared_error(prediction, target)

    # Retropropagación
    d_error_d_z_out = mse_derivative(prediction, target)

    # Actualización de la capa de salida
    w_out -= learning_rate * d_error_d_z_out * d_z_out_d_w_out
    b_out -= learning_rate * d_error_d_z_out * d_z_out_d_b_out

    d_z_out_d_a1 = w_out
    d_error_d_a1 = d_error_d_z_out * d_z_out_d_a1
    d_a1_d_z1 = relu_derivative(z1)

    # Actualización de la capa oculta
    w1 -= learning_rate * d_error_d_a1 * d_a1_d_z1 * d_z1_d_w1
    b1 -= learning_rate * d_error_d_a1 * d_a1_d_z1 * d_z1_d_b1

    # Imprimir el progreso cada 100 iteraciones
    if epoch % 100 == 0:
        print(f"Iteración {epoch+1}/{epochs}, Error: {error}, Predicción: {prediction}")

# Predicción final
print(f"Predicción final después del entrenamiento: {prediction}")
