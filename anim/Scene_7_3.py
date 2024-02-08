from manim import *

class Scene_7_3(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GRAY_A
        # Kreieren der Punkte A und B inkl. Text
        point_a = Dot(UP * 2.5 + LEFT * 5, color=BLACK)
        point_b = Dot(RIGHT * 5, color=BLACK)

        label_a = Tex("A", color=BLACK).next_to(point_a, UP)
        label_b = Tex("B", color=BLACK).next_to(point_b, UP)

        # Kreieren zweier Ellipsen
        partial_circle_left = Arc(
            start_angle=PI/2,
            angle=PI,
            color=BLACK
        ).scale(3).stretch_to_fit_width(1)

        partial_circle_right = Arc(
            start_angle=-PI/2,
            angle=PI,
            color=BLACK
        ).scale(3).stretch_to_fit_width(1)

        label_lens = Tex("Lens", color=BLACK).next_to(partial_circle_left.get_start(), UP)

        # Kreieren der Punkte auf den Ellipsen
        start_proportion_left = 0.125
        end_proportion_left = 0.5
        point_on_ellipse_left = Dot(partial_circle_left.point_from_proportion(start_proportion_left), color=BLACK, radius=0.01)

        start_proportion_right = 0.75
        end_proportion_right = 0.5
        point_on_ellipse_right = Dot(partial_circle_right.point_from_proportion(start_proportion_right), color=RED, radius=0.01)

        # Kreieren der Strahlen
        strahl_a_to_left = always_redraw(lambda: Line(point_a.get_center(), point_on_ellipse_left.get_center(), color=ORANGE))
        strahl_left_to_right = always_redraw(lambda: Line(point_on_ellipse_left.get_center(), point_on_ellipse_right.get_center(), color=ORANGE))
        strahl_right_to_b = always_redraw(lambda: Line(point_on_ellipse_right.get_center(), point_b.get_center(), color=ORANGE))

        # Anzeige
        self.play(FadeIn(point_a, point_b, label_a, label_b))
        self.play(FadeIn(partial_circle_left, partial_circle_right, label_lens))
        self.play(Create(strahl_a_to_left), rate_func=linear)
        self.play(Create(strahl_left_to_right), rate_func=linear)
        self.play(Create(strahl_right_to_b), rate_func=linear)
        self.add(point_on_ellipse_left, point_on_ellipse_right)
        self.wait(1)
        self.play(MoveAlongPath(point_on_ellipse_right, partial_circle_right, rate_func=lambda t: interpolate(start_proportion_right, end_proportion_right, t)), run_time=2)
        self.play(MoveAlongPath(point_on_ellipse_left, partial_circle_left, rate_func=lambda t: interpolate(start_proportion_left, end_proportion_left, t)), run_time=2)
        self.wait(2)

        # Fade Out
        objects = [point_a, point_b, label_a, label_b, partial_circle_left, partial_circle_right, label_lens, point_on_ellipse_left, point_on_ellipse_right, strahl_a_to_left, strahl_left_to_right, strahl_right_to_b]
        self.play(*[FadeOut(obj) for obj in objects])

