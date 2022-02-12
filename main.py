# -*- coding: utf-8 -*-

from manim import *
from manim_presentation import Slide
import cv2
from numpy import array


# RUN:

class Main(Slide):

    def construct(self):
        EARTH_RADIUS = 2
        MOON_RADIUS = 0.8
        EARTH_IDX = 0
        MOON_IDX = 1
        radius = [EARTH_RADIUS, MOON_RADIUS]

        def resize_radius(factor):
            return [x * factor for x in radius]

        def make_solar_system(model_center, earth_freq, moon_freq):
            sun = Dot(color=YELLOW).shift(model_center)

            earth_route = Circle(color=WHITE, radius=radius[EARTH_IDX],
                                 stroke_opacity=0). \
                shift(sun.get_center())
            earth = Dot(color=BLUE).shift(earth_route.get_start())

            moon_route = Circle(color=WHITE, radius=radius[MOON_IDX],
                                stroke_opacity=0.2). \
                shift(earth.get_center())
            moon = Dot().move_to(moon_route.get_start())

            earth_trace = TracedPath(earth_route.get_start,
                                     dissipating_time=5,
                                     stroke_opacity=[0, 0])
            moon_trace = TracedPath(moon_route.get_start,
                                    dissipating_time=16,
                                    stroke_opacity=[0, 1])

            earth_route.add_updater(lambda x: x.rotate(earth_freq))
            earth.add_updater(lambda a: a.move_to(earth_route.get_start()))

            moon_route.add_updater(lambda g: g.move_to(earth.get_center()))
            moon_route.add_updater(lambda f: f.rotate(moon_freq))
            moon.add_updater(lambda c: c.move_to(moon_route.get_start()))

            return (earth, earth_route, earth_trace, sun, moon_trace, moon,
                    moon_route)

        #################### main explain

        quote = Text("Math is the only place where truth and beauty\n"
                     "mean the same thing.", t2c={'truth': RED,
                                                  'beauty': BLUE,
                                                  'same thing': GREEN
                                                  }, font_size=38,
                     disable_ligatures=True).move_to(UP * 3)
        writer = Text("-Danica McKellar", color=YELLOW,
                      font_size=38).next_to(quote, DOWN)
        title = Text(r"מסימפסון ועד הירח", font="Calibri", font_size=88)
        self.wait(2)
        self.play(FadeIn(quote))
        self.play(Create(writer))
        self.wait(5)
        self.play(FadeIn(title))
        self.pause()

        self.play(FadeOut(quote, writer, title))
        self.pause()
        self.wait()
        ##################### scene 1 #############################
        scene1_title = Text("Earth's orbit", font_size=55).move_to(UP * 3)
        scene1_title2 = Text("Moon's orbit", font_size=55).move_to(UP * 3)
        mainSolar = make_solar_system(Dot().get_center(), 0.04, 0.24)
        creates = [Create(mainSolar[x]) for x in range(len(mainSolar)) if
                   x < 4]
        self.play(Create(scene1_title))
        self.wait(3)
        self.play(*creates)
        self.start_loop()
        self.play(mainSolar[0].animate, run_time=22, rate_func=linear)
        self.wait(5)
        self.end_loop()
        self.pause()

        creates = [Create(mainSolar[x]) for x in range(len(mainSolar)) if
                   x > 4]
        self.play(Transform(scene1_title, scene1_title2))
        self.play(*creates)
        self.start_loop()
        self.wait(22)
        self.end_loop()
        self.pause()

        uncreate = [Uncreate(mainSolar[x]) for x in range(len(mainSolar))]
        self.play(*uncreate, Uncreate(scene1_title2), Uncreate(scene1_title))
        self.pause()
        self.pause()
        self.wait()

        ##################### scene 2 #############################
        image = ImageMobject(
            r'D:\projects\familyTed\media\images\main\ancientEpycyclesMap.png')
        self.play(FadeIn(image))
        self.wait(10)
        self.pause()
        self.play(FadeOut(image))
        self.pause()
        self.pause()
        self.wait()

        ##################### scene 3 #############################

        scene1_title2 = Text("Star's orbit around earth",
                             font_size=55).move_to(UP * 3)
        mainSolar = make_solar_system(Dot().get_center(), 0.04, 0.24)
        creates = [Create(mainSolar[x]) for x in range(len(mainSolar))]

        self.play(Create(scene1_title2))
        self.play(*creates)
        self.start_loop()
        self.play(mainSolar[0].animate, run_time=22, rate_func=linear)
        self.wait(10)
        self.end_loop()

        uncreate = [Uncreate(mainSolar[x]) for x in range(len(mainSolar))]
        self.play(*uncreate, Uncreate(scene1_title2))
        self.pause()
        self.wait()

        ##################### scene 3 #############################

        image = ImageMobject(
            r'D:\projects\familyTed\media\images\main\starsmovement.png')
        self.play(FadeIn(image))
        self.wait(10)
        self.pause()
        self.play(FadeOut(image))
        self.pause()
        self.wait()
        ##################### scene 2 #############################
        radius = resize_radius(0.7)

        solar1 = make_solar_system(Dot().get_center() + RIGHT * 4 + UP * 2,
                                   0.02,
                                   0.03)
        solar2 = make_solar_system(Dot().get_center() + LEFT * 4 + UP * 2,
                                   0.02,
                                   0.06)
        solar3 = make_solar_system(Dot().get_center() + RIGHT * 4 + DOWN * 2,
                                   0.02,
                                   0.09)
        solar4 = make_solar_system(Dot().get_center() + LEFT * 4 + DOWN * 2,
                                   0.02,
                                   0.12)
        creates = [Create(x) for solar in [solar1, solar2, solar3, solar4]
                   for x in solar]
        self.play(*creates)
        self.start_loop()
        self.play(solar1[0].animate, run_time=44, rate_func=linear)
        self.wait(10)
        self.end_loop()
        self.pause()
        uncreate = [Uncreate(x) for solar in [solar1, solar2, solar3, solar4]
                    for x in solar]
        self.play(*uncreate)
        self.pause()
        self.wait()

        ##################### scene 3 #############################

        image = ImageMobject(
            r'D:\projects\familyTed\media\images\main\starsMap.png')
        self.play(FadeIn(image))
        self.wait(10)
        self.pause()
        self.play(FadeOut(image))
        self.pause()
        self.wait()

        scene1_title2 = Text("Thanks!")
        self.play(Create(scene1_title2))
        self.pause()
        self.wait()
