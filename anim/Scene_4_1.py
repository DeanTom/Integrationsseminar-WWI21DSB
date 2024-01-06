from manim import *

class StraightAndCurvedDownwardLine(Scene):
    def construct(self):
        # Definition der Hintergrundfarbe
        self.camera.background_color=GRAY_A

        # Erstellung  des Punktes 'A'
        dotA = Dot(color=BLACK).scale(1.8)
        dotA.move_to(UP * 3 + LEFT * 6)

        A = Text("A", color=BLACK)
        A.next_to(dotA, UP, buff=0.2)

        # Erstellung des Punktes 'B'
        dotB = Dot(color=BLACK).scale(1.8)
        dotB.move_to(DOWN * 3 + RIGHT * 6)

        B = Text("B", color=BLACK)
        B.next_to(dotB, UP, buff=0.2)

        # Erstellung der Texte
        shortest_path_text = Text("This is the shortest path.", color=BLACK).scale(0.5)
        shortest_path_text.move_to(UP * 2.5 + RIGHT * 3)

        question_text = Text ("But is it also the fastest?", color=BLACK).scale(0.5)
        question_text.move_to(UP * 2 + RIGHT * 3)

        # Erstellung der StraightDownwardLine
        ax1 = Axes(
            x_range=[0, 10], 
            y_range=[0, 10], 
            axis_config={"include_tip": False}
        )

        t1 = ValueTracker(0)

        def func1(x):
            return -x + 10
        
        graph1 = ax1.plot(func1, color=BLACK)

        initial_point1 = [ax1.coords_to_point(t1.get_value(), func1(t1.get_value()))]
        dot1 = Dot(point=initial_point1, color=GREEN)
        dot1.scale(1.2)

        dot1.add_updater(lambda x: x.move_to(ax1.c2p(t1.get_value(), func1(t1.get_value()))))
        x_space = np.linspace(*ax1.x_range[:2],100)
        minimum_index1 = func1(x_space).argmin()

        # Erstellung der CurvedDownwardLine
        ax2 = Axes(
            x_range=[0.1, 10], y_range=[0, 10], axis_config={"include_tip": False}
        )

        t2 = ValueTracker(0.1)

        def func2(y):
            return (1/y)
            
        graph2 = ax2.plot(func2, color=BLACK)

        initial_point2 = [ax2.coords_to_point(t2.get_value(), func2(t2.get_value()))]
        dot2 = Dot(point=initial_point2, color=GREEN)
        dot2.scale(1.2)

        dot2.add_updater(lambda y: y.move_to(ax2.c2p(t2.get_value(), func2(t2.get_value()))))
        x_space = np.linspace(*ax2.x_range[:2],100)
        minimum_index = func2(x_space).argmin()

        # Erstellung der Bewegung der Punkte mit unterschiedlichen Geschwindigkeiten
        animation1 = AnimationGroup(
            t1.animate.set_value(x_space[minimum_index]),
            run_time=5
        )

        animation2 = AnimationGroup(
            t2.animate.set_value(x_space[minimum_index]),
            run_time=4.5
        )
        
        # Initiierung der Abläufe
        self.play(Create(dotA), Write(A))
        self.wait(2)

        self.play(Create(dotB))
        self.play(dotB.animate.shift(LEFT * 12), run_time=4)
        self.play(dotB.animate.shift(RIGHT * 12), run_time=0.5)
        self.wait(2)
        self.play(Write(B))
        self.wait(10)

        self.play(Create(graph1))
        self.add(dot1)
        self.play(animation1)
        self.play(FadeOut(dot1))

        self.play(Write(shortest_path_text))
        self.wait(2)
        self.play(Write(question_text))
        self.wait(2)
        self.play(FadeOut(shortest_path_text, question_text))
        self.wait(2)
        
        self.play(Create(graph2))
        self.add(dot1, dot2)
        self.play(animation1, animation2)
        self.wait()