from manim import *

class Scale2(Scene):
    def construct(self):
        # Erstelle die Waage
        water_text = Text("Minimal Time in Water", color=GREEN).shift(LEFT * 2.5 + UP * 0.5)
        path_text = Text("Shortest Path", color=RED).shift(RIGHT * 3.5 + UP * 0.5)
        water_text.scale(0.65)
        path_text.scale(0.65)
        horizontal_line = Line(LEFT * 5, RIGHT * 5, color=BLACK)
        moving_object = VGroup(water_text, path_text, horizontal_line)
        triangle = Polygon(LEFT * 2, RIGHT * 2, UP * 3, color=BLACK).shift(DOWN * 3)

        self.camera.background_color=GRAY_A
        self.add(moving_object)
        self.add(triangle)
        self.play(Rotate(moving_object, angle=PI/12, about_point=ORIGIN, run_time=1))
        self.play(Rotate(moving_object, angle=-PI/7, about_point=ORIGIN, run_time=1))
        self.play(Rotate(moving_object, angle=PI/10, about_point=ORIGIN, run_time=1))
        self.play(Rotate(moving_object, angle=-PI/13, about_point=ORIGIN, run_time=1))
        self.play(Rotate(moving_object, angle=PI/15, about_point=ORIGIN, run_time=1))
        self.play(Rotate(moving_object, angle=-PI/18, about_point=ORIGIN, run_time=1))
        self.play(Rotate(moving_object, angle=PI/36, about_point=ORIGIN, run_time=1))
        self.wait(2)