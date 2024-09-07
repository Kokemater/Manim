from manim import *


class Layer(VGroup):
    def __init__(self, n_nodes=4, n_right_steps=0, color=WHITE):
        super().__init__()
        # Crear nodos de la capa
        self.nodes = [Dot().shift(LEFT)]
        for i in range(1, n_nodes):
            self.nodes.append(Dot().next_to(self.nodes[i - 1], DOWN))
        self.add(*self.nodes)
        self.move_to(ORIGIN).shift(RIGHT * n_right_steps).set_color(color)

    def show_values(self, values):
        # Método para mostrar valores sobre cada nodo
        for i, value in enumerate(values):
            if i < len(self.nodes):
                text = MathTex(str(value)).next_to(self.nodes[i], RIGHT)
                self.nodes[i].add(text)

    def focus(self,index):
            node = self.nodes[index]
            return Succession(Indicate(node, scale_factor= 3))

class Connection(VGroup):
    def __init__(self, layer1, layer2):
        super().__init__()
        # Crear conexiones entre dos capas
        for prev_neuron in layer1.nodes:
            for next_neuron in layer2.nodes:
                line = Line(prev_neuron.get_center(), next_neuron.get_center(), stroke_width=1)
                self.add(line)
    def focus(self,index):
        line = self.lines[index]
        return Succession(Indicate(node, scale_factor= 3))

class NeuralNetworkScene(Scene):
    def create_layers(self, sizes):
        # Crear las capas de la red neuronal
        layers = VGroup()
        for i, size in enumerate(sizes):
            color = YELLOW if i == 0 else (RED if i == len(sizes) - 1 else WHITE)
            layer = Layer(n_nodes=size, n_right_steps=-5 + 2 * i, color=color)
            layers.add(layer)
        layers.move_to(ORIGIN)
        return layers

    def create_connections(self, layers):
        # Crear las conexiones entre capas
        connections = VGroup()
        for i in range(len(layers) - 1):
            connection = Connection(layers[i], layers[i + 1])
            connections.add(connection)
        return connections

class nn_example1(NeuralNetworkScene):
    def construct(self):
        layers = self.create_layers([3, 10, 5, 2])  # Crear las capas
        connections = self.create_connections(layers)  # Crear las conexiones
        self.add(layers)  # Añadir las capas a la escena

        # Hacer brillar el primer nodo en la primera capa
        shine_animation = layers[0].focus(index=0)
        if shine_animation:
            self.play(shine_animation)
        self.wait()

