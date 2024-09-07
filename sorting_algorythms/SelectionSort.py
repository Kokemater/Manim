from manim import *

class SelectionSort(Scene):
    def update_text(self, text, i, j, min_index,i_text, j_text, min_index_text, labels):
        text.become(Text(f"N = 5").to_corner(UL)).scale(0.5)
        i_text.become(Text(f"i = {i}").next_to(text, RIGHT).set_color(GREEN)).scale(0.5)
        j_text.become(Text(f"j = {j}").next_to(i_text, RIGHT).set_color(RED)).scale(0.5)
        min_index_text_0 = Text("min_index =").set_color(YELLOW)
        min_index_text_1 = Text(f"{min_index}").set_color(YELLOW).next_to(min_index_text_0)
        min_index_text_2 = Text("list[min_index] = ").set_color(YELLOW).next_to(min_index_text_1)
        min_index_text_3 = Text(f"{labels[min_index][1].text}").set_color(YELLOW).next_to(min_index_text_2)
        min_index_text.become(        
        VGroup(min_index_text_0, min_index_text_1, min_index_text_2, min_index_text_3).next_to(j_text, RIGHT).set_color(RED).scale(0.5)
        )
        self.wait(1)


    def update_arrows(self, i_arrow, j_arrow, labels, i, j):
        i_arrow.become(Arrow(start=labels[i].get_top() + UP, end=labels[i].get_top()).set_color(GREEN))
        j_arrow.become(Arrow(start=labels[j].get_top() + UP, end=labels[j].get_top()).set_color(RED))
        self.add_sound("sounds_folder/next.mp3")


    def selection_sort(self, labels):
        n = len(labels)
        
        # Crear textos y flechas solo una vez
        text = Text(f"N = 5").to_corner(UL).scale(0.5)
        i_text = Text(f"i = 0").next_to(text, RIGHT).set_color(RED).scale(0.5)
        j_text = Text(f"j = 0").next_to(i_text, RIGHT).set_color(RED).scale(0.5)
        min_index_text_0 = Text("min_index =").set_color(YELLOW)
        min_index_text_1 = Text(f"{0}").set_color(YELLOW).next_to(min_index_text_0)
        min_index_text_2 = Text("list[min_index]").set_color(YELLOW).next_to(min_index_text_1).shift(RIGHT*0.2)
        min_index_text_3 = Text(f"{labels[0][1].text} =").set_color(YELLOW).next_to(min_index_text_2)
        min_index_text = VGroup(min_index_text_0, min_index_text_1, min_index_text_2, min_index_text_3).next_to(j_text, RIGHT).set_color(RED).scale(0.5)

        i_arrow = Arrow(start=labels[0].get_top() + UP, end=labels[0].get_top()).set_color(GREEN)
        j_arrow = Arrow(start=labels[1].get_top() + UP, end=labels[1].get_top()).set_color(RED)
        self.add(i_text, j_text, min_index_text, i_arrow, j_arrow)
        
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                # Actualizar textos y flechas
                self.update_text(text, i, j, min_index, i_text, j_text, min_index_text, labels)

                self.update_arrows(i_arrow, j_arrow, labels, i, j)
                self.wait(0.5)
                ask_0 = Text(f"{int(labels[j][1].text)} < {int(labels[min_index][1].text)}")
                ask_1 = Text("????").next_to(ask_0)
                ask = VGroup(ask_0, ask_1).move_to(ORIGIN).to_edge(DOWN)
                self.play(Write(ask), runtime=0.4)
                self.pause(0.2)
                if int(labels[min_index][1].text) > int(labels[j][1].text):
                    ask.set_color(GREEN)
                    min_index = j
                    self.add_sound("sounds_folder/correct.mp3")

                    self.play(labels[min_index].animate.set_color(RED),
                              labels[j].animate.set_color(RED), runtime=0.5)
                    self.play(labels[min_index].animate.set_color(BLUE),
                              labels[j].animate.set_color(BLUE), runtime=0.5)
                else:            
                    ask.set_color(RED)
                    self.add_sound("sounds_folder/error.mp3")
                
                self.play(Unwrite(ask), runtime= 0.2)
                    
                    
            # Intercambiar elementos visualmente
            if min_index != i:
                self.add_sound("sounds_folder/swap.mp3")

                self.play(
                    labels[min_index].animate.move_to(labels[i].get_center()),
                    labels[i].animate.move_to(labels[min_index].get_center()), runtime = 1.4
                )

                labels[min_index], labels[i] = labels[i], labels[min_index]
            self.wait(0.5)

    def construct(self):
        # Crear el array a ordenar
        array_values = [6, 3, 8, 5, 2]
        
        labels = VGroup(*[VGroup(
            Square().set_fill(BLUE, opacity=0.5).set_stroke(BLUE_E, width=2),
                Text(str(array_values[i]), font_size=24),
            ) for i in range(5)
            ])
        index = VGroup(*[Integer(i).scale(0.65).set_color(YELLOW) for i in range(5)])
        labels.arrange(RIGHT, buff=0.5)
        for i in range(5):
            index[i].next_to(labels[i], DOWN)
        # Posicionar el array y las etiquetas en la pantalla
        self.play(Write(labels))
        self.play(Write(index))
        self.wait(1)

        # Ejecutar Selection Sort con intercambios visualizados
        self.selection_sort(labels)

        # Mostrar el array ordenado final
        self.wait(1)
