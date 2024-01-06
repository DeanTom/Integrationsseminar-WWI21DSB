from manim import *

class SpongebobAndPatrickScene2(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GRAY_A

        # Create the images
        spongebob = ImageMobject("img\spongebob.png")
        patrick = ImageMobject("img\patrick_mirrored.png")
        spongebob.scale(0.7)
        patrick.scale(0.7)

        # # Add the finish flag
        # finish_flag = ImageMobject("img\racing_pole.png")

        # Create the first half of the mountain
        def custom_func(x):
            return np.where(x < 1, 1, np.where(1 <= x < 2, -x + 2, 0))

        custom_graph = FunctionGraph(
            custom_func,
            color=BLACK,
            x_range=[0, 3]
        )

        # Create the second half of the mountain
        def logistic_func(x):
            return np.where(x < 3, np.nan, np.where(3 <= x < 5, 1 / (1 + np.exp(-7 * x + 28)), 1))

        custom_graph2 = FunctionGraph(
            logistic_func,
            color=BLACK,
            x_range=[3, 6]
        )

        graph_group = VGroup(custom_graph, custom_graph2)
        graph_group.center()

        # Move the images to the top left corner
        spongebob.move_to(custom_graph.points[0]+ UP/2 + LEFT/2).scale(0.3)
        patrick.move_to(custom_graph2.points[-1] + UP/2 + RIGHT/2).scale(0.3)

        # # Move the flag to the finish line
        # finish_flag.move_to(custom_graph2.points[-1]).scale(0.3)

        # Add the racecars
        racecar1 = ImageMobject("img\RaceCar.png")
        racecar2 = ImageMobject("img\RaceCar_mirrored.png")
        racecar1.scale(0.2)
        racecar2.scale(0.2)
        racecar1.move_to(custom_graph.points[0])
        racecar2.move_to(custom_graph2.points[-1])

        # Reversed Graph to make it possible to move backwards
        reversed_graph2_points = custom_graph2.points[::-1]
        reversed_custom_graph2 = FunctionGraph(
            logistic_func,
            color=BLACK,
            x_range=[3, 6]
        )   
        reversed_custom_graph2.set_points_as_corners(reversed_graph2_points)

        # Add car animations
        caranimation1 = AnimationGroup(
            MoveAlongPath(racecar1, custom_graph),
            run_time=4
        )

        caranimation2 = AnimationGroup(
            MoveAlongPath(racecar2, reversed_custom_graph2),
            run_time=3
        )

        line_length1 = custom_graph.get_width()
        line1 = Line(LEFT * line_length1 / 2, RIGHT * line_length1 / 2, color=RED)  
        line2 = Line(LEFT * line_length1 / 2, RIGHT * line_length1 * 0.6, color=BLUE)

        # Position the line below custom_graph
        line1.next_to(custom_graph, DOWN, buff=0.5)  
        line2.next_to(line1, DOWN, buff=0.5)
        line2.shift(RIGHT * 0.14)

        self.play(Create(custom_graph))
        self.play(Create(custom_graph2))
        self.play(FadeIn(spongebob),FadeIn(patrick))
        self.play(self.camera.frame.animate.set(width=graph_group.get_width() * 1.5))
        self.play(ApplyMethod(custom_graph.set_color, RED))
        self.wait(1)
        self.play(FadeIn(line1))
        self.wait(1)
        self.play(ApplyMethod(custom_graph2.set_color, BLUE))
        self.wait(1)
        self.play(FadeIn(line2))
        self.wait(1)
        self.play(FadeOut(line2), FadeOut(line1))
        self.play(FadeIn(racecar1), FadeIn(racecar2))
        self.wait(1)
        self.play(caranimation1, caranimation2)
        self.wait(1)
        # List of all objects that are visible at the end
        objects = [spongebob, patrick, custom_graph, custom_graph2, racecar1, racecar2]

        # Fade out all objects
        self.play(*[FadeOut(obj) for obj in objects])