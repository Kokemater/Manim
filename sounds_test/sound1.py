from manim import *

class SoundExample(Scene):
    def construct(self):
        # Crear un texto simple
        text = Text("Hello, Manim!").scale(1.5)
        self.play(Write(text))
        
        # Añadir un sonido en el segundo 1
        self.add_sound("sounds/correct.mp3", time_offset=1)
        
        self.wait(2)
