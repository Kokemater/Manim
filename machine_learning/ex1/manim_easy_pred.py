from manim import *
from manim import *

class Abstract(Scene):
    def construct(self):
        # Crear el texto del título "Abstract" y centrarlo
        abs_title = Text("Abstract", font_size=48)
        abs_title.shift(UP)
        
        # Crear el cuerpo del abstracto y centrarlo debajo del título
        abs_body = Text(
            "Estudio de una red neuronal sencilla con\n"
            "un nodo de entrada, un nodo oculto y un nodo de salida.",
            font_size=24, line_spacing=1.5
        ).next_to(abs_title, DOWN, buff=0.5)

        # Animaciones: escribir el título y el cuerpo
        self.play(Write(abs_title))
        self.play(FadeIn(abs_body, shift=UP))
        self.wait(2)
        
        # Animación: mover el abstracto hacia arriba y desvanecer
        self.play(
            abs_title.animate.shift(UP*3),
            abs_body.animate.shift(UP*3)
        )
        self.play(FadeOut(abs_title), FadeOut(abs_body))


class Introduccion(Scene):
    def construct(self):
        
        # Título
        intro = Text("Sección 1: \n Introducción").move_to(ORIGIN)
        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(intro))
        
        title = Text("Red Neuronal Simple").to_edge(UP)
        self.play(Write(title))

        # Neuronas de la capa de entrada
        input_neuron = Circle(radius=0.3, color=BLUE).shift(LEFT * 4)
        input_text = Text("Input (m^2)", font_size=24).next_to(input_neuron, UP, buff = 0.5)
        # Neuronas de la capa oculta
        hidden_neuron = Circle(radius=0.3, color=GREEN).shift(LEFT * 1)
        hidden_text = Text("Hidden Layer 1", font_size=24).next_to(hidden_neuron, UP, buff=0.5)

        # Neurona de la capa de salida
        output_neuron = Circle(radius=0.3, color=RED).shift(RIGHT * 2)
        output_text = Text("Output\n(Price)", font_size=24).next_to(output_neuron, UP, buff = 0.5)

        # Dibujar las neuronas
        self.play(FadeIn(input_neuron, input_text))
        self.play(FadeIn(hidden_neuron, hidden_text))
        self.play(FadeIn(output_neuron, output_text))
        self.play(Transform(input_text, Text("x_1").move_to(input_neuron).scale(0.3).set_color(BLUE) ))
        self.play(Transform(hidden_text, Text("a_1").move_to(hidden_neuron).scale(0.3).set_color(GREEN) ))
        self.play(Transform(output_text, MathTex("\hat{y}").move_to(output_neuron).scale(0.5).set_color(RED) ))

        # Conexiones (Pesos)
        input_to_hidden = Line(input_neuron.get_right(), hidden_neuron.get_left(), color=WHITE)
        hidden_to_output = Line(hidden_neuron.get_right(), output_neuron.get_left(), color=WHITE)
        w1_label = MathTex("w_1").next_to(input_to_hidden, DOWN, buff=0.1)
        w_out_label = MathTex("w_2").next_to(hidden_to_output, DOWN, buff=0.1)

        # Añadir conexiones
        self.play(Create(input_to_hidden), Write(w1_label))
        self.play(Create(hidden_to_output), Write(w_out_label))

        # Etiquetas de activaciones y sesgos
        bias1_label = MathTex("b_1").next_to(hidden_neuron, DOWN, buff=0.5)
        z1_label = MathTex("z_1 = w_1x_1 + b_1").next_to(hidden_neuron, UP, buff=0.5).scale(0.5).set_color(GREEN)
        activation1_label = MathTex("a_1 = ReLU(z_1)").next_to(z1_label, UP, buff=0.5).scale(0.5).set_color(GREEN)
        ac = MathTex(r"	\begin{cases}z_1, & \text{si } z_1 > 0 \\0, & \text{si } z_1 \leq 0\end{cases}").move_to(activation1_label).set_color(GREEN).scale(0.6)

        bias_out_label = MathTex("b_2").next_to(output_neuron, DOWN, buff=0.5)
        z_out_label = MathTex("z_2 = w_2a_1 + b_2").next_to(output_neuron, UP, buff=0.5).scale(0.5).set_color(RED)

        # Mostrar etiquetas de activación y sesgos
        self.play(Write(bias1_label), Write(bias_out_label))
        self.play(Write(z1_label))
        self.play(Write(z_out_label))

        self.play(Write(activation1_label))
        self.wait(1)
        self.play(Transform(activation1_label, ac))
        
        # SET COLORS
        self.play(w1_label.animate.set_color(YELLOW).scale(1.5))
        self.play(w_out_label.animate.set_color(YELLOW).scale(1.5))
        self.play(bias1_label.animate.set_color(YELLOW).scale(1.5))
        self.play(bias_out_label.animate.set_color(YELLOW).scale(1.5))

        x = MathTex(r"\textbf{x} = \begin{bmatrix} w_1\\ b_1\\w_2\\ b_2 \end{bmatrix}").set_color(YELLOW).to_corner(RIGHT).shift(LEFT)
        self.play(FadeIn(x))
        # Despedida
        self.play(FadeOut(output_neuron, hidden_neuron, input_neuron,
                          input_to_hidden, hidden_to_output, title, input_text, hidden_text, output_text,
                          w1_label, w_out_label, bias1_label, activation1_label, z1_label, z_out_label, bias_out_label, x))
        

from manim import *

class GradientDescent(Scene):
    def construct(self):
        # Definir las fórmulas
        gradient_formula = MathTex(
            r"\mathbf{\nabla} f(\mathbf{x}) =\begin{bmatrix} \frac{\partial C(\mathbf{x})}{\partial w_1} \\ \frac{\partial C(\mathbf{x})}{\partial b_1} \\            \frac{\partial C(\mathbf{x})}{\partial w_2} \\           \frac{\partial C(\mathbf{x})}{\partial b_2}\end{bmatrix}"
        ).scale(0.8)

        partial_w2 = MathTex(
            r"\frac{\partial C}{\partial w_2} =",
            r"\frac{\partial C}{\partial \hat{y}}",
            r"\frac{\partial \hat{y}}{\partial w_2}"
        ).scale(0.8)

        partial_b2 = MathTex(
            r"\frac{\partial C}{\partial b_2} =",
            r"\frac{\partial C}{\partial \hat{y}}",
            r"\frac{\partial \hat{y}}{\partial b_2}"
        ).scale(0.8).next_to(partial_w2, DOWN, buff=0.5)
        partial_2 = VGroup(partial_w2, partial_b2)

        derivative_C_hat_y = MathTex(
            r"\frac{\partial C}{\partial \hat{y}} =",
            r"\frac{\partial }{\partial \hat{y}} \left(\frac{1}{2}(\hat{y} - y )^2\right) = \hat{y} - y"
        ).scale(0.5).to_edge(LEFT).shift(DOWN)

        derivative_y_w2 = MathTex(
            r"\frac{\partial \hat{y}}{\partial w_2} =",
            r"\frac{\partial}{\partial w_2} \left(w_2 a_1 + b_2\right) = a_1"
        ).scale(0.8).next_to(derivative_C_hat_y, RIGHT, buff=0.5).shift(UP)

        derivative_y_b2 = MathTex(
            r"\frac{\partial \hat{y}}{\partial b_2} =",
            r"\frac{\partial}{\partial b_2} \left(w_2 a_1 + b_2\right) = 1"
        ).scale(0.5).next_to(derivative_y_w2, DOWN, buff=0.5)

        partial_w1 = MathTex(
            r"\frac{\partial C}{\partial w_1} =",
            r"\frac{\partial C}{\partial \hat{y}}",
            r"\frac{\partial \hat{y}}{\partial a_1}",
            r"\frac{\partial a_1}{\partial z_1}",
            r"\frac{\partial z_1}{\partial w_1}"
        ).scale(0.5).to_edge(UP)

        partial_b1 = MathTex(
            r"\frac{\partial C}{\partial b_1} =",
            r"\frac{\partial C}{\partial \hat{y}}",
            r"\frac{\partial \hat{y}}{\partial a_1}",
            r"\frac{\partial a_1}{\partial z_1}",
            r"\frac{\partial z_1}{\partial b_1}"
        ).scale(0.5).next_to(partial_w1, DOWN, buff=0.5)

        a1 = MathTex(r"\frac{\partial \hat{y}}{\partial a_1} = \frac{\partial}{\partial a_1}(w_2a_1 + b_2) = w_2").next_to(partial_b1, DOWN).scale(0.5).shift(RIGHT)
        a2 = MathTex(r"	\frac{\partial a_1}{\partial z_1} =  \frac{\partial}{\partial z_1}(\text{ReLU}(z_1)) =\frac{\partial}{\partial z_1}\begin{cases} z_1, & \text{si } z_1 > 0 \\ 0, & \text{si } z_1 \leq 0 \end{cases}	 =  \begin{cases} 1, & \text{si } z_1 > 0 \\ 0, & \text{si } z_1 \leq 0 \end{cases} ").next_to(a1, DOWN).scale(0.5)
        a3 = MathTex(r"	\frac{\partial z_1}{\partial w_1} = \frac{\partial}{\partial w_1} (w_1x_1 + b_1) = x_1").next_to(a2, DOWN).scale(0.5)
        a4 = MathTex(r"	\frac{\partial z_1}{\partial w_1} = \frac{\partial}{\partial b_1} (w_1x_1 + b_1) = 1").next_to(a3, DOWN).scale(0.5)
        a5 = MathTex(r"	\frac{\partial C}{\partial w_1} = (\hat{y} - y)w_2\frac{\partial}{\partial z_1}(\text{ReLU}(z_1))x_1").next_to(a4, DOWN).scale(0.5)
        a6 = MathTex(r"	\frac{\partial C}{\partial b_1} = (\hat{y} - y)w_2\frac{\partial}{\partial z_1}(\text{ReLU}(z_1))").next_to(a5, DOWN).scale(0.5)



        # Animar las fórmulas
        self.play(Write(gradient_formula))
        self.play(gradient_formula.animate.to_corner(UL))
        self.wait(1)
        self.play(Write(partial_2))
        self.play(partial_2.animate.to_edge(UP))
        self.play(Write(derivative_C_hat_y))
        self.wait(1)
        self.play(Write(derivative_y_w2))
        self.wait(1)
        self.play(Write(derivative_y_b2))
        self.wait(1)
        
        final_partial_w2 = MathTex(
            r"\frac{\partial C}{\partial w_2} = (\hat{y} - y) a_1"
        ).scale(0.8).move_to(partial_w2)

        final_partial_b2 = MathTex(
            r"\frac{\partial C}{\partial b_2} = (\hat{y} - y)"
        ).scale(0.8).move_to(partial_b2)

        self.play(Transform(partial_w2, final_partial_w2))
        self.play(Transform(partial_b2, final_partial_b2))

        self.play(derivative_C_hat_y.animate.to_corner(DL).scale(0.5))
        self.play(derivative_y_w2.animate.next_to(derivative_C_hat_y, UP).scale(0.5))
        self.play(derivative_y_b2.animate.next_to(derivative_y_w2, UP).scale(0.5))
        self.play(partial_2.animate.next_to(derivative_y_b2, UP).scale(0.5))

        self.wait(2)
        self.play(Write(partial_w1))
        self.wait(1)
        self.play(Write(partial_b1))
        self.play(Write(a1))
        self.wait(1)
        self.play(Write(a2))
        self.wait(1)
        self.play(Write(a3))
        self.wait(1)
        self.play(Write(a4))
        self.wait(1)
        self.play(Write(a5))
        self.wait(1)
        self.play(Write(a6))
        self.wait(1)
        self.wait(2)

class ShowGradient(Scene):
    def construct(self):
        final_gradient = MathTex(
            r"\nabla C =",
            r"\begin{bmatrix}(\hat{y} - y) a_1 \\ (\hat{y} - y) \\(\hat{y} - y) w_2 \frac{\partial}{\partial z_1}(\text{ReLU}(z_1)) x_1 \\ (\hat{y} - y) w_2 \frac{\partial}{\partial z_1}(\text{ReLU}(z_1)) \end{bmatrix}").scale(0.8)
        self.play(Write(final_gradient))
        self.wait(4)
        self.play(Unwrite(final_gradient))

class ShowCode1(Scene):
    def construct(self):
        # Creando el objeto Code para mostrar el código
        codigo = Code(
            code="""
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
    """,
            language="Python",
        )

        # Mostrar el código en pantalla
        self.play(Write(codigo))
        self.wait(2)

class ShowCode2(Scene):
    def construct(self):
        # Creando el objeto Code para mostrar el código
        codigo = Code(
            code="""

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
    """,
            language="Python",
        )

        # Mostrar el código en pantalla
        self.play(Write(codigo))
        self.wait(2)




class ShowCode3(Scene):
    def construct(self):
        # Creando el objeto Code para mostrar el código
        codigo = Code(
            code="""

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

    """,
            language="Python",
        )

        # Mostrar el código en pantalla
        self.play(Write(codigo))
        self.wait(2)


