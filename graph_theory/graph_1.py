from manim import *

class GraphBFS(Scene):
    def construct(self):
        # Crear los nodos del grafo
        nodes = {
            "A": np.array([-2, 2, 0]),
            "B": np.array([2, 2, 0]),
            "C": np.array([-2, 0, 0]),
            "D": np.array([2, 0, 0]),
            "E": np.array([0, -2, 0]),
        }

        # Crear las aristas del grafo
        edges = [
            ("A", "B"),
            ("A", "C"),
            ("B", "D"),
            ("C", "E"),
            ("D", "E"),
        ]

        # Dibujar los nodos
        vertex_circles = {node: Dot(point=pos) for node, pos in nodes.items()}
        vertex_labels = {node: Text(node).next_to(pos, UP) for node, pos in nodes.items()}

        for node in vertex_circles:
            self.play(Create(vertex_circles[node]), Write(vertex_labels[node]))

        # Dibujar las aristas
        edge_lines = []
        for edge in edges:
            start, end = edge
            line = Line(vertex_circles[start].get_center(), vertex_circles[end].get_center())
            edge_lines.append(line)
            self.play(Create(line))

        self.wait(1)

        # BFS Explicación
        bfs_order = ["A", "B", "C", "D", "E"]
        queue_label = Text("Queue:").to_edge(DOWN)
        queue = VGroup(*[Text(node) for node in bfs_order]).arrange(RIGHT).next_to(queue_label, RIGHT)
        self.play(Write(queue_label), Write(queue))

        current = vertex_circles["A"]
        self.play(current.animate.set_color(RED))

        for node in bfs_order[1:]:
            next_node = vertex_circles[node]
            self.play(next_node.animate.set_color(RED), run_time=0.5)
            self.wait(0.5)

        self.wait(2)
