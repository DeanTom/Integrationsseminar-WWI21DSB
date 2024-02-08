from manim import *

class Scene_5_1(MovingCameraScene):
    def construct(self):
        shortest_text = Text("SHORTEST", color=GREEN)
        time_text = Text("TIME?", color=RED)
        full_shortest_time_text = VGroup(shortest_text, time_text).arrange(RIGHT)

        brachisto_text = Text("BRACHISTO", color=GREEN)
        brachisto_text.shift(UP + LEFT * 3)
        chrone_text = Text("CHRONE", color=RED)
        chrone_text.shift(UP + RIGHT * 3)

        diagonal_line_1 = Line(UP * 0.5 + LEFT * 0.5, DOWN * 0.5+ RIGHT * 0.5, color=BLACK).shift(LEFT * 3)
        diagonal_line_2 = Line(UP * 0.5 + RIGHT * 0.5, DOWN * 0.5 + LEFT * 0.5, color=BLACK).shift(RIGHT * 3)

        self.camera.background_color=GRAY_A
        self.play(Write(full_shortest_time_text))
        self.wait(2)
        self.play(full_shortest_time_text.animate.shift(DOWN))
        self.add(diagonal_line_1)
        self.play(Write(brachisto_text))
        self.wait(2)
        self.add(diagonal_line_2)
        self.play(Write(chrone_text))
        self.wait(2)
        self.play(FadeOut(diagonal_line_1), FadeOut(diagonal_line_2))
        self.play(brachisto_text.animate.shift(RIGHT * 1.3), chrone_text.animate.shift(LEFT * 0.9))
        self.play(self.camera.frame.animate.set(width=full_shortest_time_text.get_width() * 1.8))
        self.wait(2)