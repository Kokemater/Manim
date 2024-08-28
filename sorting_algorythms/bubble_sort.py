from manim import *

class BubbleSort(Scene):
    def bubble_sort(self, labels):
        n = len(labels)
        for i in range(n):        
            for j in range(0, n - 1):
                text = Text(f"N = 5").to_corner(UL)
                j_text = always_redraw(lambda: Text(f"j = {j}").next_to(text, RIGHT).shift(RIGHT).set_color(GREEN))
                jnext_text = always_redraw(lambda: Text(f"j + 1 = {j + 1}").next_to(j_text, RIGHT).shift(RIGHT).set_color(RED))
                self.add(text, j_text, jnext_text)
                j_arrow = always_redraw(lambda: 
                Arrow(start = labels[j].get_top() + UP, end = labels[j].get_top()).set_color(GREEN))
                j_arrow_next = always_redraw(lambda: 
                Arrow(start = labels[j+1].get_top() + UP, end = labels[j + 1].get_top()).set_color(RED))
                
                # Add sound when comparing elements
                self.play(FadeIn(j_arrow), FadeIn(j_arrow_next), run_time = 1.5)

                if int(labels[j][1].text) > int(labels[j+1][1].text):
                    self.play(labels[j].animate.set_color(RED), labels[j + 1].animate.set_color(RED), run_time = 0.1)

                    # Add sound for swapping elements
                    self.add_sound("sounds_folder/swap.mp3")

                    # Swap the labels visually
                    self.play(
                        labels[j].animate.move_to(labels[j+1].get_center()),
                        labels[j+1].animate.move_to(labels[j].get_center())
                    )
                    self.play(labels[j].animate.set_color(BLUE), labels[j + 1].animate.set_color(BLUE))

                    # Swap the labels in the list
                    labels[j], labels[j+1] = labels[j+1], labels[j]

    def construct(self):
        # Create the array to be sorted
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
        # Position the array and labels on the screen
        self.play(Write(labels))
        self.play(Write(index))

        # Add background music (optional)
        self.add_sound("sounds_folder/meditation.mp3", gain=-10)
        
        # Perform bubble sort with visualized swaps
        self.bubble_sort(labels)
        self.add_sound("sounds_folder/correct.mp3", gain=-10)


        # Show the final sorted array
        self.wait(1)


class ShowCode(Scene):
    def construct(self):
        # Crear un bloque de código en Python
        code = Code(
            code="""
int main(void)
{
    int list[N] = {6, 3, 8, 5, 2};
    int i;
    int j;

    i = 0;
    while (i < N)
    {
        j = 0;
        while(j < N - 1)
        {
            if (list[j] > list[j+1])
                swap(&list[j], &list[j+1]);
            j++;
        }
        i++;
    }

    print_list(list, N);

}
""",
            tab_width=4,
            background="window",
            language="c",
            font="Monospace",
            insert_line_no=False,  # No insertar números de línea
            style="monokai",  # Estilo de color (por ejemplo, 'monokai')
        )

        # Añadir el bloque de código a la escena
        self.play(Write(code))

        # Add a typing sound effect
        self.add_sound("typing.mp3", time_offset=0)
        self.wait(2)



class ShowCode(Scene):
    def construct(self):
        # Crear un bloque de código en Python
        code = Code(
            code="""
int main(void)
{
    int list[N] = {6, 3, 8, 5, 2};
    int i;
    int j;

    i = 0;
    while (i < N)
    {
        j = 0;
        while(j < N - 1)
        {
            if (list[j] > list[j+1])
                swap(&list[j], &list[j+1]);
            j++;
        }
        i++;
    }

    print_list(list, N);

}
""",
            tab_width=4,
            background="window",
            language="c",
            font="Monospace",
            insert_line_no=False,  # No insertar números de línea
            style="monokai",  # Estilo de color (por ejemplo, 'monokai')
        )

        # Añadir el bloque de código a la escena
        self.play(Write(code))
        self.wait(2)



