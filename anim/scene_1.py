from manim import *

class SpongebobAndPatrickScene1(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GRAY_A

        # Create the images
        spongebob = ImageMobject("img\spongebob.png")
        patrick = ImageMobject("img\patrick.png")
        racecar_intro =  ImageMobject("img\RaceCar.png")

        spongebob.scale(0.7)
        patrick.scale(0.7)

        spongebob.to_edge(LEFT)
        patrick.to_edge(RIGHT)
        racecar_intro.move_to(ORIGIN + LEFT/3)
        self.add(spongebob, patrick)


        # Move the images to the edges of the screen
        spongebob_animation = AnimationGroup(
            FadeIn(spongebob),
            spongebob.animate.to_edge(RIGHT),
        )

        patrick_animation = AnimationGroup(
            FadeIn(patrick),
            patrick.animate.to_edge(LEFT),
        )

        self.play(spongebob_animation, patrick_animation)
        self.wait(1)

        # Add the text
        text_spongebob = Tex("Spongebob", color = BLACK).next_to(spongebob, UP)
        text_patrick = Tex("Patrick", color = BLACK).next_to(patrick, UP)
        text_racecar_intro = Tex("Soapbox car", color = BLACK).next_to(racecar_intro, UP)
        text_racecar_intro2 = Tex("trust, this has no motor", color = BLACK, font_size = 30).next_to(racecar_intro, DOWN)
        self.play(Write(text_patrick), Write(text_spongebob))
        self.wait(3)
        self.play(FadeIn(racecar_intro))
        self.wait(1)
        self.play(Write(text_racecar_intro), Write(text_racecar_intro2))
        self.wait(1)
        self.play(FadeOut(text_patrick), FadeOut(text_spongebob), FadeOut(racecar_intro), FadeOut(text_racecar_intro), FadeOut(text_racecar_intro2))

        # Define the mountainside
        def custom_func(x):
            return np.where(x < 1, 1, np.where(1 <= x < 2, -x + 2, 0))

        custom_graph = FunctionGraph(
            custom_func,
            color=BLACK,
            x_range=[0, 3],
            stroke_width=2,
        ).scale(1.5)

        # Define the tracks for the other car so its visible
        def custom_func2(x):
            return np.where(x < 1, 1, np.where(1 <= x < 2, -x + 2, 0))

        custom_graph2 = FunctionGraph(
            custom_func2,
            color=GRAY_A,
            x_range=[0, 3],
        ).scale(1.5)
        graph_label = Tex("Let's do a race", color=BLACK, font_size = 25).next_to(custom_graph, DOWN * 3)

        custom_graph.center()
        custom_graph2.center()
        custom_graph2.shift(UP * 0.2)

        # Move the images to the top left corner
        spongebob_animation_to_corner = AnimationGroup(
            spongebob.animate.move_to(custom_graph.points[0] + LEFT + UP/2).scale(0.3),
        )

        patrick_animation_to_corner = AnimationGroup(
            patrick.animate.move_to(custom_graph.points[0] + UP + 1/3 * LEFT).scale(0.3),
        )

        # Group the animations together and add lag
        animations = AnimationGroup(
            spongebob_animation_to_corner,
            patrick_animation_to_corner,
            lag_ratio=0.5  
        )

        # Add the animations to the scene
        # self.play(animations)
        self.play(animations, self.camera.frame.animate.set(width=custom_graph.get_width() * 1.8))
        self.play(Create(custom_graph), Create(custom_graph2), Write(graph_label))
        self.wait(3)
        self.play(FadeOut(graph_label))
        self.wait(1)

        # Add the racecars
        racecar1 = ImageMobject("img\RaceCar.png")
        racecar2 = ImageMobject("img\RaceCar.png")
        racecar1.scale(0.15)
        racecar2.scale(0.15)
        racecar1.move_to(custom_graph.points[0])
        racecar2.move_to(custom_graph2.points[0])

        # # Add the finish flag
        # finish_flag = ImageMobject("img\racing_pole.png")
        # finish_flag.scale(0.1)
        # finish_flag.move_to(custom_graph.points[-1]).scale(0.3)

        # Play the race
        self.play(FadeIn(racecar1), FadeIn(racecar2))
        self.wait(1)

        start_text =  Tex("3", color=BLACK, font_size = 45).move_to(ORIGIN + UP + RIGHT)
        start_text2 =  Tex("2", color=BLACK, font_size = 45).move_to(ORIGIN + UP+ RIGHT)
        start_text3 =  Tex("1", color=BLACK, font_size = 45).move_to(ORIGIN + UP+ RIGHT)
        start_text4 =  Tex("GO!", color=BLACK, font_size = 45).move_to(ORIGIN + UP+ RIGHT)
        self.play(Write(start_text))
        self.play(ReplacementTransform(start_text, start_text2))
        self.play(ReplacementTransform(start_text2, start_text3))
        self.play(ReplacementTransform(start_text3, start_text4))
        self.play(FadeOut(start_text4), MoveAlongPath(racecar1, custom_graph, rate_func=smooth), MoveAlongPath(racecar2, custom_graph2, rate_func=smooth), run_time=3)
        self.wait(1)
        self.wait(1)

        # Next up : Woahh, both arrive at the same time 
        graph_label2 = Tex("Both arrive at the same time!", color=BLACK, font_size = 35).next_to(custom_graph, DOWN).shift(DOWN/2)
        self.play(Write(graph_label2))
        self.wait(1)
        
        # Add all objects to a list
        objects = [spongebob, patrick, custom_graph, custom_graph2, racecar1, racecar2, graph_label2]

        # Fade out all objects
        self.play(*[FadeOut(obj) for obj in objects])