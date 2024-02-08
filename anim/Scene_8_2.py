from manim import *

class Scene_8_2(MovingCameraScene):
    def construct(self):
        # Erstelle die Waage
        water_text = Tex("Minimal Time in Water", color=RED).shift(LEFT * 2.6 + UP * 0.5)
        path_text = Tex("Shortest Path", color=BLUE).shift(RIGHT * 3.6 + UP * 0.5)
        water_text.scale(0.9)
        path_text.scale(0.9)

        horizontal_line = Line(LEFT * 5, RIGHT * 5, color=BLACK)
        moving_object = VGroup(water_text, path_text, horizontal_line)
        triangle = Polygon(LEFT * 1.5, RIGHT * 1.5, UP * 2.25, color=BLACK).shift(DOWN * 2.26)

        self.camera.background_color=GRAY_A
        self.add(moving_object)
        self.add(triangle)
        self.play(Rotate(moving_object, angle=PI/12, about_point=ORIGIN, run_time=1.5))
        self.play(Rotate(moving_object, angle=-PI/7, about_point=ORIGIN, run_time=1.5))
        self.play(Rotate(moving_object, angle=PI/10, about_point=ORIGIN, run_time=1.5))
        self.play(Rotate(moving_object, angle=-PI/13, about_point=ORIGIN, run_time=1.5))
        self.play(Rotate(moving_object, angle=PI/15, about_point=ORIGIN, run_time=1.5))
        self.play(Rotate(moving_object, angle=-PI/18, about_point=ORIGIN, run_time=1.5))
        self.play(Rotate(moving_object, angle=PI/36, about_point=ORIGIN, run_time=1.5))
        self.wait(2)

        objects = [moving_object, triangle]
        self.play(*[FadeOut(obj) for obj in objects])