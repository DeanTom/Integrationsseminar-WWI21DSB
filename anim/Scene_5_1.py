from manim import *

class Scene_5_1(MovingCameraScene):
    def construct(self):
        shortest_text = Tex("SHORTEST", color=RED)
        time_text = Tex("TIME?", color=BLUE)
        full_shortest_time_text = VGroup(shortest_text, time_text).arrange(RIGHT)

        brachisto_text = Tex("BRACHISTO", color=RED)
        brachisto_text.shift(UP + LEFT * 3.5)
        chrone_text = Tex("CHRONE", color=BLUE)
        chrone_text.shift(UP + RIGHT * 3.5)

        diagonal_line_1 = Line(UP * 0.5 + LEFT * 0.5, DOWN * 0.5+ RIGHT * 0.5, stroke_width=2, color=BLACK).shift(LEFT * 3)
        diagonal_line_2 = Line(UP * 0.5 + RIGHT * 0.5, DOWN * 0.5 + LEFT * 0.5, stroke_width=2, color=BLACK).shift(RIGHT * 3)

        self.camera.background_color=GRAY_A
        self.play(Write(full_shortest_time_text))
        self.wait(2)
        self.play(full_shortest_time_text.animate.shift(DOWN))
        self.add(diagonal_line_1)
        self.play(Write(brachisto_text))
        self.add(diagonal_line_2)
        self.play(Write(chrone_text))
        self.wait(2)
        self.play(FadeOut(diagonal_line_1), FadeOut(diagonal_line_2))
        self.play(brachisto_text.animate.shift(RIGHT * 2.3), chrone_text.animate.shift(LEFT * 2.1))
        self.play(self.camera.frame.animate.set(width=full_shortest_time_text.get_width() * 1.8))
        self.wait(2)

        # Add all created objects to a list for fading out
        objects = [full_shortest_time_text, brachisto_text, chrone_text]

        # Fade out all objects
        self.play(*[FadeOut(obj) for obj in objects])
        self.wait(1)