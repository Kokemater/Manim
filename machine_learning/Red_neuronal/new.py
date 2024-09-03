from manim import *

class NeuralNetworkScene(Scene):
    def construct(self):
        # Create the input layer with 1000 nodes
        
        def create_layer(n_nodes=4, n_right_steps= 0, color = WHITE):
            circles = []
            circles.append(Dot().shift(LEFT))
            for i in range(1,n_nodes):
                circles.append(Dot().next_to(circles[i-1], DOWN))
            circles = VGroup(*circles).move_to(ORIGIN).shift(RIGHT*n_right_steps).set_color(color)
            return circles
        def create_connections(layers):
            lines = []
            for i in range(len(layers) - 1):
                layer = layers[i]
                for prev_neuron in layers[i]:
                    for next_neuron in layers[i+1]:
                        line = Line(prev_neuron.get_center(), next_neuron.get_center(),stroke_width=1)
                        self.add(line)
        def create_neural_network(sizes):
            layers = []
            for i in range(len(sizes)):
                if i == 0:
                    color = YELLOW
                elif i == len(sizes) - 1: 
                    color = RED
                else:
                    color = WHITE
                layers.append(create_layer(n_nodes=sizes[i], n_right_steps= -5 + 2 * i, color=color))
                self.add(layers[i])
            return layers
        layers = create_neural_network([3, 10, 5, 2])

        create_connections(layers)


