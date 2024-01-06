from manim import *

class SpongebobAndPatrickScene2(MovingCameraScene):
     def construct(self):
        self.camera.background_color=GRAY_A

        # Create the images
        spongebob = ImageMobject("img\spongebob.png")
        patrick = ImageMobject("img\patrick_mirrored.png")
        lightbulb = ImageMobject("img\lightbulb.png")
        spongebob.scale(0.7)
        lightbulb.scale(0.2)

        lightbulb.move_to(ORIGIN + 2* UP + 2* LEFT)
        patrick.move_to(ORIGIN)
        self.play(FadeIn(patrick))
        self.play(FadeIn(lightbulb))
        self.wait(1)
        self.play(FadeOut(lightbulb), FadeOut(patrick))
        patrick.scale(0.7)


        # # Add the finish flag
        # finish_flag = ImageMobject("img\racing_pole.png")

        # Create the first half of the mountain
        def custom_func(x):
            return np.where(x < 1, 1, np.where(1 <= x < 2, -x + 2, 0))

        custom_graph = FunctionGraph(
            custom_func,
            color=BLACK,
            x_range=[0, 3],
            stroke_width=2,
        )

        # Create the second half of the mountain
        def logistic_func(x):
            return np.where(x < 3, np.nan, np.where(3 <= x < 5, 1 / (1 + np.exp(-7 * x + 28)), 1))

        custom_graph2 = FunctionGraph(
            logistic_func,
            color=BLACK,
            x_range=[3, 6],
            stroke_width=2,
        )

        graph_group = VGroup(custom_graph, custom_graph2)
        graph_group.center()

        # Move the images to the top left corner
        spongebob.move_to(custom_graph.points[0]+ 2/3 * UP + LEFT/2).scale(0.3)
        patrick.move_to(custom_graph2.points[-1] + 2/3 * UP + RIGHT/2).scale(0.3)

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
        line1 = Line(LEFT * line_length1 / 2, RIGHT * line_length1 / 2, color=RED, stroke_width=2)  
        line2 = Line(LEFT * line_length1 / 2, RIGHT * line_length1 * 0.6, color=BLUE, stroke_width=2)

        # Position the line below custom_graph
        line1.next_to(custom_graph, DOWN, buff=0.5)  
        line2.next_to(line1, DOWN, buff=0.5)
        line2.shift(RIGHT * 0.14)

        # Define start text
        start_text =  Tex("3", color=BLACK, font_size =  45).move_to(graph_group.get_center() + UP)
        start_text2 =  Tex("2", color=BLACK, font_size =  45).move_to(graph_group.get_center() + UP)
        start_text3 =  Tex("1", color=BLACK, font_size = 45).move_to(graph_group.get_center() + UP)
        start_text4 =  Tex("GO!", color=BLACK, font_size =  45).move_to(graph_group.get_center() + UP)

        # Define patrick wins text
        patrick_wins_text =  Tex("Patrick wins!", color=BLACK, font_size= 35).next_to(graph_group, DOWN).shift(DOWN/2)

        # Define end text
        end_text =  Tex("But how is this possible?", color=BLACK, font_size = 7).next_to(patrick, UP/6)
        end_text2 =  Tex("Well, let's change the scenery", color=BLACK, font_size = 7).next_to(patrick, UP/6)

        self.play(Create(custom_graph))
        self.play(Create(custom_graph2))
        # self.play(FadeIn(spongebob),FadeIn(patrick))
        self.play(self.camera.frame.animate.set(width=graph_group.get_width() * 1.4),FadeIn(spongebob),FadeIn(patrick))
        self.wait(1)
        self.play(ApplyMethod(custom_graph2.set_color, BLUE))
        self.wait(1)
        self.play(ApplyMethod(custom_graph.set_color, RED))
        self.wait(1)
        self.play(FadeIn(line1))
        self.wait(1)
        self.play(FadeIn(line2))
        self.wait(1)
        self.play(FadeOut(line2), FadeOut(line1), ApplyMethod(custom_graph2.set_color, BLACK), ApplyMethod(custom_graph.set_color, BLACK))
        self.play(FadeIn(racecar1), FadeIn(racecar2))
        self.wait(1)
        self.play(Write(start_text))
        self.play(ReplacementTransform(start_text, start_text2))
        self.play(ReplacementTransform(start_text2, start_text3))
        self.play(ReplacementTransform(start_text3, start_text4))
        self.play(FadeOut(start_text4), caranimation1, caranimation2)
        self.wait(1)
        self.play(Write(patrick_wins_text))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(patrick).set(width=patrick.get_width() * 2.7))
        self.wait(1)
        self.play(FadeIn(end_text))
        self.wait(1)
        self.play(Transform(end_text, end_text2))
        self.wait(1)


        # List of all objects that are visible at the end
        objects = [end_text2, end_text, patrick]

        # Fade out all objects
        self.play(*[FadeOut(obj) for obj in objects])