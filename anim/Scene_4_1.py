from manim import *

class Scene_4_1(MovingCameraScene):
    def construct(self):
        # Definition der Hintergrundfarbe
        self.camera.background_color=GRAY_A

        # Erstellung  des Punktes 'A'
        dotA = Dot(color=BLACK, radius=0.16)
        dotA.move_to(UP * 3 + LEFT * 6)

        A = Tex("A", color=BLACK)
        A.next_to(dotA, UP, buff=0.2)

        # Erstellung des Punktes 'B'
        dotB = Dot(color=BLACK, radius=0.16)
        dotB.move_to(DOWN * 3 + RIGHT * 6)

        B = Tex("B", color=BLACK)
        B.next_to(dotB, UP)

        # Erstellung der Texte
        this_is_shortest_path_text = Tex("This is the shortest path.", color=BLACK).scale(0.8)
        this_is_shortest_path_text.move_to(UP * 2.5 + RIGHT * 3)

        question_text = Tex("But is it also the fastest?", color=BLACK).scale(0.8)
        question_text.move_to(UP * 2 + RIGHT * 3)

        shortest_path_text = Tex("Shortest path", color=BLUE).scale(0.8)
        shortest_path_text.move_to(UP * 2 + RIGHT * 0.5)

        uneven_text = Text(" ≠ ", color=BLACK).scale(0.5)
        uneven_text.move_to(UP * 2 + RIGHT * 2)

        shortest_time_text = Tex("Shortest time ", color=BLACK).scale(0.8)
        shortest_time_text.move_to(UP * 2 + RIGHT * 3.5)

        # Erstellung der StraightDownwardLine
        ax1 = Axes(
            x_range=[0, 10], 
            y_range=[0, 10], 
            axis_config={"include_tip": False}
        )

        def func1(x):
            return -x + 10
        
        graph1 = ax1.plot(func1, color=BLACK, stroke_width=2)
        graph1.set_z_index(dotA.z_index - 1)

        dot1 = Dot(graph1.points[0], color=BLUE, radius=0.12)

        # Erstellung der CurvedDownwardLine
        ax2 = Axes(
            x_range=[0.1, 10], 
            y_range=[0, 10], 
            axis_config={"include_tip": False}
        )

        def func2(y):
            return (1/y)
        
        graph2 = ax2.plot(func2, color=BLACK, stroke_width=2)

        dot2 = Dot(graph2.points[0], color=BLUE, radius=0.12)

        # Erstellung des Loopings

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

        starting_point = Dot(looping.points[0], color=BLACK, radius=0.16)
        label_starting_point = Tex("A", color=BLACK).next_to(starting_point, UP)

        ending_point = Dot(looping.points[-1], color=BLACK, radius=0.16)
        label_ending_point = Tex("B", color=BLACK).next_to(ending_point, UP)
        
        dot3 = Dot(looping.points[0], color=BLUE, radius=0.12)
        
        # Erstellung der Bewegung der Punkte mit unterschiedlichen Geschwindigkeiten
        animation1 = AnimationGroup(
            MoveAlongPath(dot1, graph1),
            run_time=5
        )

        animation2 = AnimationGroup(
            MoveAlongPath(dot2, graph2),
            run_time=4
        )
        
        # Initiierung der Abläufe
        self.play(Create(dotA), Write(A))
        self.wait(2)

        self.play(Create(dotB))
        self.play(dotB.animate.shift(LEFT * 12), run_time=4)
        self.play(dotB.animate.shift(RIGHT * 12), run_time=0.5)
        self.wait(2)
        self.play(Write(B))
        self.wait(2)

        self.play(Create(graph1))
        self.add(dot1)
        self.play(animation1)
        self.play(FadeOut(dot1))

        self.play(Write(this_is_shortest_path_text))
        self.wait(2)
        self.play(Write(question_text))
        self.wait(2)
        self.play(FadeOut(this_is_shortest_path_text, question_text))
        self.wait(2)
        
        self.play(Create(graph2))
        self.add(dot1, dot2)
        self.play(animation1, animation2)
        self.clear()
        self.wait(3)

        self.play(FadeIn(starting_point), Write(label_starting_point))
        self.play(FadeIn(ending_point), Write(label_ending_point))
        self.play(Create(looping))
        self.play(FadeIn(dot3))
        self.play(MoveAlongPath(dot3, looping, rate_func=smooth), run_time=4)
        objects = [looping, starting_point, label_starting_point, ending_point, label_ending_point, dot3]
        self.play(*[FadeOut(obj) for obj in objects])

        self.play(Create(dotA), Write(A), Create(dotB), Write(B))
        self.play(Create(graph1), Create(graph2))
        self.play(ApplyMethod(graph1.set_color, BLUE))
        self.play(Write(shortest_path_text), Write(uneven_text), Write(shortest_time_text))
        self.play(shortest_path_text.animate.shift(UP * 0.5))
        self.play(shortest_path_text.animate.shift(DOWN * 0.5))
        self.play(shortest_time_text.animate.shift(UP * 0.5))
        self.play(shortest_time_text.animate.shift(DOWN * 0.5))

        # Fade out all objects
        objects = [dotA, A, dotB, B, graph1, graph2, shortest_path_text, uneven_text, shortest_time_text]
        self.play(*[FadeOut(obj) for obj in objects])
        self.wait(1)