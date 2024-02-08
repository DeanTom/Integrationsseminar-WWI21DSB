from manim import *

class Scene_6(MovingCameraScene):
    def construct(self):
        self.camera.background_color = GRAY_A

        ### Zeitstrahl erstellen
        timeline = NumberLine(
            x_range=[1500, 2200, 10],
            length=50,
            #include_numbers=True,
            #label_direction=UP,
            color = BLACK
        )

        for x in range(1500, 2201, 50):
            number = Text(str(x), color=BLACK).next_to(timeline.n2p(x), DOWN)
            self.add(number)

        ### Markierungen für Zeitstrahl erstellen
        
        line_2024 = Line(timeline.number_to_point(2024), timeline.number_to_point(2024) + 1 * np.array([np.cos(PI/4), np.sin(PI/4), 0]) , color =BLACK)
        text_2024 = Tex(str(2024)+ " - " + "Spongebob", color = BLACK).next_to(line_2024, UP * 0.9 + RIGHT * 0.5)

        line_1638 = Line(timeline.number_to_point(1638), timeline.number_to_point(1638) + 1 * np.array([np.cos(PI/4), np.sin(PI/4), 0]) , color =BLACK)
        text_1638 = Tex(str(1638)+ " - " + "Gallileo", color = BLACK).next_to(line_1638, UP * 0.9 + RIGHT * 0.5)

        line_1697 = Line(timeline.number_to_point(1697), timeline.number_to_point(1697) + 4 * np.array([np.cos(PI/4), 0.5 * np.sin(PI/4), 0]) , color =BLACK)
        text_1697 = Tex(str(1697)+ " - " + "Newton", color = BLACK).next_to(line_1697, UP * 0.9 + RIGHT)

        # Bilder Hinzufügen 
        gallileo_image = ImageMobject("img/Galileo_Galilei.png")
        gallileo_image.move_to(LEFT * 16 + UP * 3)
        # Group
        spongebob_image = ImageMobject("img/spongebob.png").scale(0.7)
        spongebob_image.move_to(RIGHT * 16 + UP * 3)

        patrick_image = ImageMobject("img/patrick.png")
        patrick_image.move_to(RIGHT * 12 + UP * 2.3)

        racecar_image = ImageMobject("img/RaceCar.png")
        racecar_image.scale(0.07)

        newton_image = ImageMobject("img/Isaac_Newton.png").scale(0.5)
        newton_image.next_to(text_1697, UP)


        ### Kreis für Gallileo Erklärung hinzufügen
        circle = Circle(radius=2, color=BLACK)
        circle.move_to(LEFT * 11 + UP*4)
        # Definiere zwei Punkte auf dem Umfang des Kreises unten links
        point1 = circle.point_at_angle(5 * PI / 4) # 225 Grad
        point2 = circle.point_at_angle(3 * PI / 2) # 270 Grad
        # Erstelle Dot-Objekte für die Punkte
        dot1 = Dot(point1, color=BLACK).scale(0.7)
        dot2 = Dot(point2, color=BLACK).scale(0.7)
        dot1text = Tex("A", color=BLACK).scale(0.3).next_to(dot1, DOWN/2)
        dot2text = Tex("B", color=BLACK).scale(0.3).next_to(dot2, DOWN/2)
        
        # Linie zwischen Punkten
        arc = Arc(
            start_angle=5 * PI / 4, 
            angle=3 * PI / 2 - 5 * PI / 4, 
            radius=circle.radius, 
            color=BLACK,
            stroke_width=2,
            arc_center=circle.get_center()
        )

        # Erstelle die Waage
        triangle = Polygon(LEFT * 2, RIGHT * 2, UP * 3, color=BLACK, stroke_width=1).scale(0.1)
        triangle.next_to(arc.get_center(), 3/4 * UP + RIGHT/4)
        horizontal_line = Line(start=triangle.get_top() + LEFT*4, end=triangle.get_top() + RIGHT*4, color=BLACK, stroke_width=1).scale(0.1)
        horizontal_line.shift(0.01 * UP)
        short_text = Tex("Short", color=BLUE).scale(0.2).next_to(horizontal_line.get_start(), 0.09 * UP)
        steep_text = Tex("Steep", color=RED).scale(0.2).next_to(horizontal_line.get_end(), 0.03 * UP)
        moving_object = VGroup(short_text, steep_text, horizontal_line)


        # objekte an richtige stelle bringen:   
        # Objekte zu image hinzufügen.
        self.add(timeline)
        #self.add(circle,dot1,dot2,arc)
        #self.add(racecar_image)

        
        # Camera setup für Frame creation
        self.camera.frame.move_to(RIGHT * 13 + UP)
        self.play(Create(line_2024))
        self.play(Write(text_2024))
        self.play(FadeIn(patrick_image,spongebob_image))
        self.play(self.camera.frame.animate.shift(LEFT * 26), run_time = 3)
        self.play(Create(line_1638))
        self.play(Write(text_1638))
        self.play(FadeIn(gallileo_image))
        self.play(self.camera.frame.animate.shift(UP * 1.5), Run_time = 2)
        self.play(Create(circle))
        self.play(self.camera.frame.animate.scale(0.2).move_to(arc),run_time = 2)
        self.play(FadeIn(dot1))
        self.play(FadeIn(dot2))
        self.play(Write(dot1text), Write(dot2text))
        self.play(Create(arc))
        self.wait(2)
        self.play(MoveAlongPath(racecar_image, arc), run_time=2)
        self.wait(2)
        # Waage einfügen und abspielen
        self.play(FadeIn(triangle, moving_object))
        self.wait(0.5)
        self.play(Rotate(moving_object, angle=PI/12, about_point=triangle.get_top(), run_time=2))
        self.play(Rotate(moving_object, angle=-PI/7, about_point=triangle.get_top(), run_time=2))
        self.play(Rotate(moving_object, angle=PI/10, about_point=triangle.get_top(), run_time=2))
        self.wait(2)
        # Waage Ende
        self.play(self.camera.frame.animate.scale(5).move_to(ORIGIN + LEFT * 13 + UP * 2.5), run_time=2)
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(text_1697),run_time = 2)
        self.play(Create(line_1697))                                                                                                                                                                                                                                                                                                
        self.play(Write(text_1697))
        self.play(FadeIn(newton_image))
        self.wait(2)
        self.play(self.camera.frame.animate.scale(0.35).move_to(newton_image),run_time = 2)
        self.wait(2)

        # Add all objects to a list
        objects = [newton_image]

        # Fade out all objects
        self.play(*[FadeOut(obj) for obj in objects])
        self.wait(2)