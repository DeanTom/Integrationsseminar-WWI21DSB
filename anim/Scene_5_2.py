from manim import*

class Scene_5_2(MovingCameraScene):
  def construct(self):
    # Erstelle die Waage
    short_text = Tex("Short", color=RED).shift(LEFT * 3.4 + UP * 0.5)
    steep_text = Tex("Steep", color=BLUE).shift(RIGHT * 3.4 + UP * 0.5)
    horizontal_line = Line(LEFT * 4, RIGHT * 4, color=BLACK)
    moving_object = VGroup(short_text, steep_text, horizontal_line)
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

    # Add all objects to a list
    objects = [moving_object, triangle]

    # Fade out all objects
    self.play(*[FadeOut(obj) for obj in objects])
    self.wait(1)