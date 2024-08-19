from manim import *
from numpy import *


class Vectors(VectorScene):
    def construct(self):
        plane = self.add_plane(animate=True).add_coordinates()
        basis = self.get_basis_vectors()
        self.play(Create(basis))
        vector2 = self.add_vector([-2,2])
        self.write_vector_coordinates(vector=vector2)

        self.wait(2)

class Matrix_aplication(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True
        )
    def construct(self):
        matrix = [[1,2], [2,1]]
        matrix_tex = MathTex(r"\begin{tbmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}").to_edge(UL).add_background_rectangle()

        sq = self.get_unit_square()
        text = always_redraw(lambda : 
                             Tex("Det(A)").move_to(sq.get_center()).scale(0.5))
        vect = self.get_vector([1, -2], color=PURE_BLUE)
        rect1 = Rectangle(height = 1, width=2).shift(3*LEFT + 2*UP)
        circ1 = Circle(radius =2, stroke_color=BLUE, fill_color= YELLOW, fill_opacity = 0.6)
        circ1.shift(2*RIGHT + 2 * DOWN)
        self.add_transformable_mobject(vect, sq, rect1, circ1)
        self.add_background_mobject(text, matrix_tex)
        self.apply_matrix(matrix)
        self.wait()

class playing_with_vectors(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-5,5,1], y_range=[-5,5,1], x_length=6, y_length=6)
        plane.shift(LEFT + UP)
        v1 = Line(start= plane.c2p(0,0), end= plane.c2p(2,2), color = RED).add_tip()
        v1_text = MathTex(r"\vec{v_1}", color = RED).next_to(v1, RIGHT).scale(0.5)
        vector1 = VGroup(v1, v1_text)
        v2 = Line(start= plane.c2p(0,0), end = plane.c2p(-1,0), color = GREEN).add_tip()
        v2_text = MathTex(r"\vec{v_2}", color = GREEN).next_to(v2, DOWN).scale(0.5)
        vector2 = VGroup(v2, v2_text)
        v3 = Line(start = plane.c2p(2,2), end = plane.c2p(1,2), color = GREEN).add_tip()
        v3_text = MathTex(r"\vec{v_2}", color = GREEN).next_to(v3, UP).scale(0.5)
        v4 = Line(start = plane.c2p(0,0), end = plane.c2p(1,2), color = ORANGE).add_tip()
        v4_text = MathTex(r"\vec{v_1} + \vec{v_2}", color = ORANGE).next_to(v4, LEFT).scale(0.5)


        plane.add_coordinates()
        self.play(Create(plane))
        self.play(GrowFromPoint(vector1[0], point= vector1[0].get_start()), Write(vector1[1]))
        self.wait(1)
        self.play(GrowFromPoint(vector2[0], point= vector2[0].get_start()), Write(vector2[1]))
        self.wait(1)
        self.play(Transform(v2, v3), Transform(v2_text, v3_text))
        self.wait(1)
        self.play(GrowFromPoint(v4, point= v4.get_start()), Write(v4_text))
        self.wait(2)

class Gram_Schmidt(VectorScene):
    def construct(self):
        plane = NumberPlane(x_range=[-5,5,1], y_range=[-5,5,1], x_length=6, y_length=6).add_coordinates().scale(0.8)
        self.play(Create(plane))

        v1 = self.add_vector([1,1],color=BLUE)
        v2 = self.add_vector([2,1], color = RED)
        self.play(FadeOut(v1), run_time = 0.8)
        v1 = self.add_vector([1/sqrt(2),1/sqrt(2)],color=BLUE)
        self.wait(1)
        line = Line(start = v1.get_end(), end = v2.get_end()).add_tip()
        self.play(Create(line))
        self.play(FadeOut(v2), run_time = 0.8)
        v2 = self.add_vector([1/2, -1/2], color = RED)
        self.play(FadeOut(v2), run_time = 0.8)
        v2 = self.add_vector([1/sqrt(2), -1/sqrt(2)], color = RED)


        self.wait(1)



        





    





