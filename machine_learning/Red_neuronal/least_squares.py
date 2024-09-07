from manim import *

class ErrorScene(Scene):
    def construct(self):
        puntos = [(0, 3), (3, 1), (4, 2)]

        # Definir los puntos y los ejes
        axes = Axes(x_range=[0, 5], y_range=[0, 5], axis_config={"color": GREEN})

        # Crear las variables a_0 y a_1
        a_0 = ValueTracker(2)  # Valor inicial de a_0
        a_1 = ValueTracker(-0.5)  # Valor inicial de a_1

        # Dibujar los puntos originales
        puntos_dibujados = VGroup(*[Dot(axes.c2p(x, y)) for x, y in puntos])
        self.play(Create(axes), Create(puntos_dibujados))

        # Mostrar la ecuación de la recta
        f_eq = always_redraw(lambda: 
            Text(f"f(x) = {a_0.get_value():.2f} + {a_1.get_value():.2f}x")
            .to_corner(UR).scale(0.5))
        self.play(Create(f_eq))
        # Graficar la función
        f = always_redraw(lambda:
            axes.plot(lambda x: a_0.get_value() + a_1.get_value()*x, color=BLUE))
        self.play(Create(f))

        # Mostrar el error cuadrático total (SSE)
        costo = always_redraw(lambda:
            MathTex(r"C(a_0, a_1) = \sum_{i=1}^{n} (y_i - (a_0 + a_1x_i))^2 ="  + f"{self.SSE(a_0, a_1, puntos):.2f}").set_color(RED).to_corner(UL).scale(0.5))

        self.play(Create(costo))
        
        # Crear las líneas de error dinámicas para todos los puntos
        errores = VGroup()
        for x, y in puntos:
            error_line = always_redraw(
                lambda x=x, y=y: Line(
                    start=axes.c2p(x, y),
                    end=axes.c2p(x, a_0.get_value() + a_1.get_value() * x),
                    color=YELLOW,
                    stroke_width=2,
                )
            )
            errores.add(error_line)

        # Agregar todas las líneas de error a la escena
        self.add(errores)

        # Animar el cambio de los parámetros a_0 y a_1
        self.play(a_0.animate.set_value(1), a_1.animate.set_value(0.5), run_time=4, rate_func=smooth)
        self.wait(0.4)
        self.play(a_0.animate.set_value(5), a_1.animate.set_value(-1), run_time=4, rate_func=smooth)


        # Mantener la escena por un tiempo
        self.wait(2)

    def SSE(self, a_0, a_1, puntos):
        error = 0
        for x, y in puntos:
            error += (y - (a_0.get_value() + a_1.get_value() * x))**2
        return error
class ShowCuadratic(Scene):
    def construct(self):
        text = MathTex(r"C(a_0, a_1) = \sum_{i=1}^{n} (y_i - (a_0 + a_1x_i))^2")
        text1 = MathTex(r"C(a_0, a_1) = (y_0 - \hat{y_0})^2 + (y_1 - \hat{y_1})^2 + (y_2 - \hat{y_2})^2")
        text2 = MathTex(r"C(a_0, a_1) = (3 - \hat{y_0})^2 + (1 - \hat{y_1})^2 + (2 - \hat{y_2})^2")
        text3 = MathTex(r"C(a_0, a_1) = (3 - (a_0 + a_10)^2 + (1 - (a_0 + a_13)^2 + (2 - (a_0 + a_12)^2")
        self.play(Write(text))        
        self.pause(2)
        self.play(Transform(text, text1))
        self.pause(2)
        self.play(Transform(text, text2))
        self.pause(2)
        self.play(Transform(text, text3))
        self.pause(2)


