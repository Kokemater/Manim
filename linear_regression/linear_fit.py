from manim import *

class AjusteLineal(Scene):
    def construct(self):
        # Presentación
        titulo = Text("Ajuste con 2 parámetros", color=YELLOW).scale(1.2).to_edge(UP)
        subtitulo = Text("Ejercicio", color=WHITE).next_to(titulo, DOWN)
        descripcion = Text("Tenemos 3 puntos: (0, 3), (3, 1), (4, 2)", color=BLUE).next_to(subtitulo, DOWN)
        presentacion = VGroup(titulo, subtitulo, descripcion)

        # Ecuación
        ecuacion_texto = Text("Encontrar la recta ", color=BLUE).next_to(descripcion, DOWN)
        ecuacion = MathTex("y = a_0 + a_1x", color=BLUE).next_to(ecuacion_texto, RIGHT)
        ecuacion_completa = VGroup(ecuacion_texto, ecuacion).arrange(RIGHT)


        # Configuración de ejes
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[0, 4, 1],
            axis_config={"color": WHITE},
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        )

        # Mostrar la ecuación de la recta
        ecuacion_linea = MathTex("y = 2.2 - 0.4x", color=GREEN).next_to(axes, RIGHT)
        self.play(Write(titulo))
        self.play(Write(subtitulo))
        self.play(Write(descripcion))
        self.play(Write(ecuacion_completa))
        self.play(FadeOut(presentacion))
        self.play(
            ecuacion_completa.animate.to_corner(UR).scale(0.5)  # Mover y escalar al mismo tiempo
        )
        self.wait(2)
        self.play(Create(axes))
        self.wait(2)
        puntos = [Dot(axes.c2p(0, 3), color=RED), Dot(axes.c2p(3, 1), color=RED), Dot(axes.c2p(4, 2), color=RED)]
        for punto in puntos:
            self.play(FadeIn(punto))
        # Dibujar las posibles rectas (calculada previamente)
    # Inicializar los valores de a_0 y a_1
        a_0 = ValueTracker(2)
        a_1 = ValueTracker(0.5)

        # Función de la línea que varía con los parámetros a_0 y a_1
        linea = always_redraw(lambda: 
            axes.plot(lambda x: a_0.get_value() - a_1.get_value() * x, color=GREEN)
        )

        # Mostrar la línea inicial
        self.play(Create(linea))

        # Animar el cambio de los valores de a_0 y a_1
        self.play(a_0.animate.set_value(3), a_1.animate.set_value(-0.5), run_time=3)
        self.play(a_0.animate.set_value(1), a_1.animate.set_value(1.5), run_time=3)
        self.play(Create(linea))

# Para ejecutar este código, asegúrate de tener instalado Manim y ejecuta este archivo.

