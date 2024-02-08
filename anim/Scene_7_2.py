from manim import *

class Scene_7_2(MovingCameraScene):
    def construct(self):
        self.camera.background_color=GRAY_A
        # Set background
        frame_width = config.frame_width
        frame_height = config.frame_height
        lower_background = Rectangle(width=frame_width, height=frame_height/2, color=BLUE_D, fill_opacity=1).shift(DOWN*frame_height/4)

        # Create dots A and B
        dot_A = Dot(color=BLACK).move_to(UP*2+LEFT*4) 
        dot_B = Dot(color=BLACK).move_to(DOWN*2+RIGHT*4)

        dot_A.z_index = 1
        dot_B.z_index = 1 

        # Label dots
        label_A = Tex("A", color=BLACK).next_to(dot_A, UP)
        label_B = Tex("B", color=BLACK).next_to(dot_B, DOWN)

        # Create dot on horizontal line
        dividing_line_y = 0 
        dot_on_line = Dot(fill_opacity=0).move_to(dot_A.get_x()*RIGHT + dividing_line_y*UP)

        # Use always_redraw to dynamically create lines that adjust with the dot's movement
        A_to_middle = always_redraw(lambda: Line(dot_A.get_center(), dot_on_line.get_center(), color=ORANGE, stroke_width=4))
        Middle_to_B = always_redraw(lambda: Line(dot_on_line.get_center(), dot_B.get_center(), color=ORANGE, stroke_width=4))

        # Positions directly below A and B on the dividing line
        position_below_A = dot_A.get_x() * RIGHT + dividing_line_y * UP
        position_below_B = dot_B.get_x() * RIGHT + dividing_line_y * UP

        # Create the coordinate system
        axes = Axes(
            x_range=[0, 40, 3],  
            y_range=[-10, 10, 3],  
            x_length=5,  
            y_length=3,  
            axis_config={"color": BLACK},
            tips=False,
        ).scale(0.8)

        def func(x):
            return 1/100 * (x - 20)**2 + 3

        axes.to_corner(UR)
        x_label = Tex("x", color=BLACK, font_size=40).next_to(axes.x_axis.get_end() + LEFT*0.1)
        header_text = Tex("Travel time", color=BLACK, font_size=30).move_to(axes.x_axis.get_center() + UP * 1.2)

        # Create the graph of the function
        graph = axes.plot(func, color=BLACK, x_range=[0, 40])

        # Add the dots and labels to the scene
        self.wait(2)
        self.play(FadeIn(lower_background))
        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(header_text))
        self.play(FadeIn(dot_A, label_A), FadeIn(dot_B, label_B))
        self.play(FadeIn(dot_on_line))
        self.play(FadeIn(A_to_middle, Middle_to_B))
        self.wait(2)
        self.play(dot_on_line.animate.move_to(position_below_B), Create(graph), run_time=6)
        self.play(dot_on_line.animate.move_to(position_below_A), run_time=3)
        self.wait(2)

        # Fade out 
        objects = [lower_background, axes, x_label, header_text, dot_A, label_A, dot_B, label_B, dot_on_line, A_to_middle, Middle_to_B, graph]
        self.play(*[FadeOut(obj) for obj in objects])