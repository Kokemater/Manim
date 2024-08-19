from manim import *
from numpy import *


def get_horizontal_line_to_graph(axes, function, x, width, color):
    result = VGroup()
    line = DashedLine(
        start =  axes.c2p(x, function.underlying_function(x)),
        end = axes.c2p(0, function.underlying_function(x)),
        stroke_width = width,
        stroke_color = color
    )
    dot = Dot().set_color(color).move_to(axes.c2p(x, function.underlying_function(x)))
    result.add(line, dot)
    return result

class Derivatives(Scene):
    def construct(self):
        x = ValueTracker(-2)
        interval = ValueTracker(2)
        plane1 =  NumberPlane (x_range=[-3, 4, 1], y_range= [-8, 9, 2], x_length= 10, y_length= 10).add_coordinates().to_corner(UL).shift(LEFT).scale(0.4)
        func1_text = MathTex(r"f(x) = \frac{1}{3}x^3").next_to(plane1, UP)
        func1 = plane1.plot(lambda x : 1/3* x**3)  
        plane2 =  NumberPlane (x_range=[-3, 4, 1], y_range= [-8, 9, 2], x_length= 10, y_length= 10).add_coordinates().to_corner(DR).shift(RIGHT).scale(0.4)
        func2_text = MathTex(r"f(x) = x^2").next_to(plane2, DOWN)
        func2 = plane2.plot(lambda x: x**2)
        slope_value = func2.underlying_function(x.get_value())
        Slope1 = Text("Slope = ").scale(0.9).to_corner(UL)
        Slope2 = always_redraw(lambda:
                            DecimalNumber(num_decimal_places=1).set_value(func2.underlying_function(x.get_value())).next_to(Slope1, RIGHT))        

        moving_slope = always_redraw(lambda:
            plane1.get_secant_slope_group(
                x = x.get_value(),
                graph = func1,
                dx = interval.get_value(),
                secant_line_length= func2.underlying_function(x.get_value()),
                secant_line_color= YELLOW
            ))
        hor_line = always_redraw(lambda:
                                 get_horizontal_line_to_graph(plane2, func2, x.get_value(), 2, RED))

        self.play(Create(plane1), Create(plane2))
        self.play(Create(func1_text))
        self.play(Create(func1))
        self.play(Create(func2_text))
        self.play(Create(func2))
        self.play(Create(hor_line))
        self.play(Create(moving_slope))

        self.play(interval.animate.set_value(0.01), rate_func = linear, run_time = 1)
        self.play(Create(Slope1), Create(Slope2))

        self.play(x.animate.set_value(3), rate_func = linear, run_time = 4)
        self.wait(2)


class integral_sum(Scene):
    def construct(self):
        axes = Axes(x_range=[0,10,1], y_range=[0,10,1], x_length=7, y_length=7).add_coordinates().to_edge(RIGHT)
        func1 = axes.plot(lambda x: x).set_color(BLUE)
        func2 = axes.plot(lambda x: 1/2 * x).set_color(RED)
        func3 = axes.plot(lambda x: x + 1/2*x)
        text = MathTex(r"\int f + g = \int f + \int g")
        func1_text = MathTex(r"f(x) = x").set_color(BLUE).next_to(text, DOWN)
        func2_text = MathTex(r"g(x) = \frac{1}{2}x").set_color(RED).next_to(func1_text, DOWN)
        func3_text = MathTex(r"f(x) + g(x) = x + \frac{1}{2}x").set_color(GREEN).next_to(func2_text, DOWN)

        func_text = VGroup(text, func1_text, func2_text, func3_text).to_edge(UP).scale(1)
        area_2 = axes.get_riemann_rectangles(graph=func2 , dx=1, x_range=[0,10]).set_color(RED)
        area_1 = axes.get_riemann_rectangles(graph=func1 , dx=1, x_range=[0,10]).set_color(BLUE)
        dx = ValueTracker(1)
        area_3 = always_redraw(lambda:
                                axes.get_riemann_rectangles(graph=func3 , dx=dx.get_value(), x_range=[0,10]))
        self.play(Write(func_text))
        self.play(func_text.animate.move_to(ORIGIN).to_edge(LEFT).scale(0.6))

        self.add(axes, func1, func2, func3, func_text, area_1, area_2)
        for i in range(10):
            self.play(area_2[i].animate.move_to(area_1[i].get_top(), UP).shift(UP*area_2[i].get_height()))
        self.wait()
        self.play(DrawBorderThenFill(area_3))
        self.remove(area_1, area_2)
        self.play(dx.animate.set_value(0.1), run_time=2, func_rate=smooth)

        self.wait(2)