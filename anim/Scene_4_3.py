from manim import *

class Scene_4_3(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GRAY_A

        def looping_func(t):
            t = (5 * np.pi / 2) * (t - 0.5)
            return np.array([(t / 3 - np.sin(t)), (np.cos(t) + (t ** 2) / 10), 0])

        looping = ParametricFunction(
            looping_func,
            t_range = np.array([0, 0.9, 0.01]),
            color = BLACK,
            stroke_width = 2,
        ).scale(4)

        looping.center()
        point = Dot(looping.points[0], color=BLUE, radius=0.12)
        starting_point = Dot(looping.points[0], color=BLACK, radius=0.12)
        label_starting_point = Tex("A", color=BLACK).next_to(starting_point, UP)
        ending_point = Dot(looping.points[-1], color=BLACK, radius=0.12)
        label_ending_point = Tex("B", color=BLACK).next_to(ending_point, UP)
        

        self.play(Create(looping))
        self.play(FadeIn(starting_point), Write(label_starting_point))
        self.play(FadeIn(ending_point), Write(label_ending_point))
        self.play(FadeIn(point))
        self.play(MoveAlongPath(point, looping, rate_func=smooth), run_time=4)

        # Add all objects to a list
        objects = [looping, starting_point, label_starting_point, ending_point, label_ending_point, point]

        # Fade out all objects
        self.play(*[FadeOut(obj) for obj in objects])