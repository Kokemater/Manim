import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Definir la función objetivo y su gradiente
def f(a0, a1):
    return 3 - (a0)**2 + (1 - (a0 + 3*a1)**2) + (2 - (a0 + 2*a1)**2)

def grad_f(a0, a1):
    dfd_a0 = -2 * a0 - 2 * (1 - (a0 + 3*a1)) - 2 * (2 - (a0 + 2*a1))
    dfd_a1 = -3 * (1 - (a0 + 3*a1)) - 2 * (2 - (a0 + 2*a1))
    return np.array([dfd_a0, dfd_a1])

# Parámetros del descenso por gradiente
learning_rate = 0.001
num_steps = 200
a0_init = 5
a1_init = 5

# Inicializar el punto
a0_values = [a0_init]
a1_values = [a1_init]

a0 = a0_init
a1 = a1_init

for _ in range(num_steps):
    grad = grad_f(a0, a1)
    a0 -= learning_rate * grad[0]
    a1 -= learning_rate * grad[1]
    a0_values.append(a0)
    a1_values.append(a1)

# Crear datos de prueba
x = np.linspace(-1000, 1000, 100)
y = np.linspace(-1000, 1000, 100)
x, y = np.meshgrid(x, y)
z = f(x, y)

# Crear figura y eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Configurar etiquetas y título
ax.set_xlabel('a0')
ax.set_ylabel('a1')
ax.set_zlabel('f(a0, a1)')
ax.set_title('Descenso por Gradiente en 3D')

# Crear la línea para la trayectoria
trajectory_line, = ax.plot([], [], [], 'r-', linewidth=2)

# Crear el punto grande
point = ax.plot([], [], [], 'ro', markersize=10)[0]

# Función de actualización para la animación
def update(frame):
    ax.view_init(elev=30, azim=frame)
    
    # Actualizar el punto y la trayectoria
    if frame < num_steps:
        # Actualizar el punto
        point.set_data([a0_values[frame]], [a1_values[frame]])
        point.set_3d_properties([f(a0_values[frame], a1_values[frame])])
        
        # Actualizar la trayectoria
        trajectory_line.set_data(a0_values[:frame+1], a1_values[:frame+1])
        trajectory_line.set_3d_properties([f(a0_values[i], a1_values[i]) for i in range(frame+1)])
    
    return point, trajectory_line

# Crear animación
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), blit=False)

# Guardar la animación como un archivo de video
ani.save('gradient_descent_with_trajectory.mp4', writer='ffmpeg', fps=30)

# Mostrar la gráfica (opcional)
plt.show()
