from manim import *

class NameofAnimation(Scene):
    def construct(self):
        box = Rectangle(stroke_color = GREEN, stroke_opacity = 0.7,
                        fill_color = RED, fill_opacity = 0.4, height= 1, width= 1)
        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time = 1)


class FittingObjects(Scene):
    def construct(self):
        axes = Axes(x_range = [-3, 3,1], y_range=[-3,3 ,1])
        axes.to_edge(LEFT, buff = 0.5)
        
        circle = Circle(radius=1)
        triangle = Triangle()
        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        self.play(circle.animate.to_corner(UR))
        self.play(Transform(circle, triangle))

class Updaters(Scene):
    def construct(self):
        rectangle = RoundedRectangle()
        text = MathTex(r"\frac{1}{2}")
        text.set_color_by_gradient(GREEN, PINK)
        text.move_to(rectangle.get_center())
        text.add_updater(lambda x: x.move_to(rectangle.get_center()))
        self.play(FadeIn(rectangle))
        self.add(text)
        self.play(rectangle.animate.shift(RIGHT))
        text.clear_updaters()
        self.play(rectangle.animate.to_corner(DR))


class ValueTrackers(Scene):
    def construct(self):
        r = ValueTracker(0)
        circle = always_redraw(lambda: 
        Circle(radius = r.get_value()))
        self.play(Create(circle))
        self.play(r.animate.set_value(3), rate_func = smooth)

