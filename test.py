from manim import *
from random import *
def box(n):
    result = VGroup()
    sq = Square(fill_color = BLUE, fill_opacity = 0.5)
    Texto = Integer(n)
    Texto.move_to(sq.get_center())
    result.add(sq,Texto)
    result.to_edge(LEFT).scale(0.5)
    return result
    
    
class test(Scene):
    def construct(self):
        cajas = VGroup()
        for i in range(10):
            cajas.add(box(randint(1, 100)))
            if (i >= 1):
                cajas[i].move_to(cajas[i-1].get_center()).shift(RIGHT)
        
        Prueba = Text("Prueba")


        
        self.play(FadeIn(cajas))
        self.wait(1)
        for i in range(9):
            if (cajas[i][1].number >  cajas[i][1].number):
                self.play(Write(Prueba))
        self.play(FadeOut(cajas))