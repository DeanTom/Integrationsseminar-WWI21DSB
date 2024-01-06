from manim import *

class SpongebobAndPatrickScene1(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GRAY_A

        # Create the images
        spongebob = ImageMobject("img\spongebob.png")
        patrick = ImageMobject("img\patrick.png")

        spongebob.scale(0.7)
        patrick.scale(0.7)

        spongebob.move_to(20 * LEFT)
        patrick.move_to(20 * RIGHT)
        self.add(spongebob, patrick)


        # Move the images to the edges of the screen
        spongebob_animation = AnimationGroup(
            FadeIn(spongebob),
            spongebob.animate.to_edge(RIGHT, buff=1),
        )

        patrick_animation = AnimationGroup(
            FadeIn(patrick),
            patrick.animate.to_edge(LEFT, buff=1),
        )

        self.play(spongebob_animation, patrick_animation)
        self.wait(1)

        # Add the text
        text_spongebob = Text("Spongebob", color = BLACK).next_to(spongebob, UP)
        text_patrick = Text("Patrick", color = BLACK).next_to(patrick, UP)
        self.play(Write(text_patrick), Write(text_spongebob))
        self.wait(3)
        self.play(FadeOut(text_patrick), FadeOut(text_spongebob))

        # Define the mountainside
        def custom_func(x):
            return np.where(x < 1, 1, np.where(1 <= x < 2, -x + 2, 0))

        custom_graph = FunctionGraph(
            custom_func,
            color=BLACK,
            x_range=[0, 3]
        ).scale(1.5)

        # Define the tracks for the other car so its visible
        def custom_func2(x):
            return np.where(x < 1, 1, np.where(1 <= x < 2, -x + 2, 0))

        custom_graph2 = FunctionGraph(
            custom_func2,
            color=GRAY_A,
            x_range=[0, 3]
        ).scale(1.5)
        graph_label = Text("Let's do a race", color=BLACK, font_size = 20).next_to(custom_graph, DOWN * 3)

        custom_graph.center()
        custom_graph2.center()
        custom_graph2.shift(UP * 0.2)

        # Move the images to the top left corner
        spongebob_animation_to_corner = AnimationGroup(
            spongebob.animate.move_to(custom_graph.points[0] + LEFT + UP/2).scale(0.3),
        )

        patrick_animation_to_corner = AnimationGroup(
            patrick.animate.move_to(custom_graph.points[0] + 2/3* UP + 1/3 * LEFT).scale(0.3),
        )

        # Group the animations together and add lag
        animations = AnimationGroup(
            spongebob_animation_to_corner,
            patrick_animation_to_corner,
            lag_ratio=0.5  
        )

        # Add the animations to the scene
        self.play(animations)
        self.play(self.camera.frame.animate.set(width=custom_graph.get_width() * 1.8))
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
        # finish_flag = ImageMobject("img\rennflagge.png")
        # finish_flag.scale(0.1)
        # finish_flag.move_to(custom_graph.points[-1]).scale(0.3)

        # Play the race
        self.play(FadeIn(racecar1), FadeIn(racecar2))
        self.wait(1)
        self.play(MoveAlongPath(racecar1, custom_graph, rate_func=smooth), MoveAlongPath(racecar2, custom_graph2, rate_func=smooth), run_time=2)
        self.wait(1)

        # Next up : Woahh, both arrive at the same time 
        graph_label2 = Text("Both arrive at the same time!", color=BLACK, font_size= 20).next_to(custom_graph, DOWN)
        self.play(Write(graph_label2))
        self.wait(1)
        
        # Add all objects to a list
        objects = [spongebob, patrick, custom_graph, custom_graph2, racecar1, racecar2, graph_label2]

        # Fade out all objects
        self.play(*[FadeOut(obj) for obj in objects])