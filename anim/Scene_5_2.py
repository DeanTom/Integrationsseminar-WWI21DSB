from manim import*

class Scene_5_2(MovingCameraScene):
    def construct(self):
        # Erstelle die Waage
        short_text = Text("Short", color=GREEN).shift(LEFT * 3 + UP * 0.5)
        steep_text = Text("Steep", color=RED).shift(RIGHT * 3 + UP * 0.5)
        horizontal_line = Line(LEFT * 4, RIGHT * 4, color=BLACK)
        moving_object = VGroup(short_text, steep_text, horizontal_line)
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

          # Add all objects to a list
        objects = [moving_object, triangle]

        # Fade out all objects
        self.play(*[FadeOut(obj) for obj in objects])