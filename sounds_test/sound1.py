from manim import *

class SoundExample(Scene):
    def construct(self):
        text = Text("Hello, Manim!").scale(1.5)
        self.play(Write(text))
        
        # Añadir un sonido en el segundo 0
        self.add_sound("sounds/correct.mp3", time_offset=0)
        
        self.wait(2)
