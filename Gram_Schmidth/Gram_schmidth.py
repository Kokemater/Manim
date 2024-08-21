from manim import *
import numpy as np

class GramSchmidtProcess(VectorScene):
    def write_vector(self, vector):
        # Display vectors using LaTeX
        vector_tex = MathTex(r"\vec{w_1} = \begin{pmatrix} %d \\ %d \end{pmatrix}" % (vector[0], vector[1]))
        return vector_tex

    def normalize(self, vector):
        # Normalize the vector and display the normalization formula
        norm = np.linalg.norm(vector)
        normalized_vector = vector / norm
        normalization_tex = MathTex(
            r"\vec{u_1} = \frac{\begin{pmatrix} %d \\ %d \end{pmatrix}}{\sqrt{%d^2 + %d^2}}" % (
                vector[0], vector[1], vector[0], vector[1]
            )
        )
        normalization_tex.to_corner(UR)
        self.play(Write(normalization_tex))
        return normalized_vector

    def projection(self, v, u):
        # Projection of vector v onto vector u and display the projection formula
        projection_tex = MathTex(
            r"\text{proj}_{\vec{u_1}} \vec{w_2} = \frac{\vec{w_2} \cdot \vec{u_1}}{\vec{u_1} \cdot \vec{u_1}} \vec{u_1}"
        )
        projection_tex.to_corner(UR)
        self.play(Write(projection_tex))
        return np.dot(v, u) / np.dot(u, u) * u

    def construct(self):
        plane = NumberPlane(x_range=[-5, 5, 1], y_range=[-5, 5, 1], x_length=6, y_length=6).add_coordinates().scale(0.8)
        self.play(Create(plane))

        # Define initial vectors
        v1 = np.array([1, 1])
        v2 = np.array([2, 1])

        # Show vectors in LaTeX form
        vector1_tex = self.write_vector(v1).set_color(BLUE)
        vector2_tex = self.write_vector(v2).next_to(vector1_tex, DOWN).set_color(RED)
        v_tex = VGroup(vector1_tex, vector2_tex)
        self.play(v_tex.animate.to_corner(UL))

        # Add vectors to the scene
        vec_v1 = self.add_vector(v1, color=BLUE)
        vec_v2 = self.add_vector(v2, color=RED)
        self.wait(1)

        # Normalize the first vector and show the normalization process
        v1_normalized = self.normalize(v1)
        vec_v1_normalized = self.add_vector(v1_normalized, color=BLUE_A)
        self.play(Transform(vec_v1, vec_v1_normalized))

        # Project v2 onto v1 and show the projection
        proj_v2_on_v1 = self.projection(v2, v1_normalized)
        vec_proj = self.add_vector(proj_v2_on_v1, color=YELLOW)
        self.play(Create(vec_proj))

        # Subtract the projection from v2 to get the orthogonal vector
        orthogonal_v2 = v2 - proj_v2_on_v1
        vec_orthogonal_v2 = self.add_vector(orthogonal_v2, color=ORANGE)
        self.play(Transform(vec_v2, vec_orthogonal_v2))

        # Normalize the orthogonal vector
        orthogonal_v2_normalized = self.normalize(orthogonal_v2)
        vec_orthogonal_v2_normalized = self.add_vector(orthogonal_v2_normalized, color=RED_B)
        self.play(Transform(vec_orthogonal_v2, vec_orthogonal_v2_normalized))

        self.wait(2)
