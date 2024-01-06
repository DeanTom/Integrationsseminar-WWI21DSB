from manim import *

class ZeitstrahlScene(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE

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
        racecar_image.scale(0.05)

        newton_image = ImageMobject("img/Isaac_Newton.png").scale(0.5)
        newton_image.next_to(text_1697, UP)


        ### Kreis für Gallileo Erklärung hinzufügen
        circle = Circle(radius=2, color=BLACK)
        circle.move_to(LEFT * 11 + UP*4)
        # Definiere zwei Punkte auf dem Umfang des Kreises unten links
        point1 = circle.point_at_angle(5 * PI / 4) # 225 Grad
        point2 = circle.point_at_angle(3 * PI / 2) # 270 Grad
        # Erstelle Dot-Objekte für die Punkte
        dot1 = Dot(point1, color=RED)
        dot2 = Dot(point2, color=BLUE)
        # Linie zwischen Punkten
        arc = Arc(
            start_angle=5 * PI / 4, 
            angle=3 * PI / 2 - 5 * PI / 4, 
            radius=circle.radius, 
            color=YELLOW,
            arc_center=circle.get_center()
        )


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
        self.play(Create(arc))
        self.wait(2)
        self.play(MoveAlongPath(racecar_image, arc), run_time=2)
        self.play(self.camera.frame.animate.scale(5).move_to(ORIGIN + LEFT * 13 + UP * 2.5), run_time=2)
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(text_1697),run_time = 2)
        self.play(Create(line_1697))                                                                                                                                                                                                                                                                                                
        self.play(Write(text_1697))
        self.play(FadeIn(newton_image))
        self.wait(2)