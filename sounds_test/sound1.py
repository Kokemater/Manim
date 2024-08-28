from manim import *

class SoundExample(Scene):
    def construct(self):
        text = Text("Hello, Manim!").scale(1.5)
        self.play(Write(text))
        
        # Add a sound at the start
        self.add_sound("swap.mp3", time_offset=0)
        
        self.wait(2)
