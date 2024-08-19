from manim import *
from numpy import *

class Graph1(Scene):
    def construct(self):
        axes = Axes(x_range=[-10,10,2], y_range= [-10, 10, 2],axis_config={"include_numbers": True})
        equation = MathTex(r"f(x) = x^2", color = BLUE).to_corner(UL)
        f = axes.plot(lambda x: pow(x,2))
        area = axes.get_riemann_rectangles(x_range=[-3,3], dx= 0.1, graph= f)
        point = Dot(point=array((axes.c2p(2, 2))))

        self.play(Create(point))
        self.play(Create(axes), runtime= 2)
        self.play(Write(equation))
        self.play(Write(f))
        self.play(Write(area), func_rate= smooth)
        self.play(Create(point))
        self.wait(1)


