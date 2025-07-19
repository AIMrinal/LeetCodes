from manim import *
import json

class LeetCodeRace(Scene):
    def construct(self):
        with open("progress.json") as f:
            data = json.load(f)

        categories = list(data.items())
        max_val = max(v for _, v in categories)

        bars = []
        cars = []
        labels = []

        for i, (cat, val) in enumerate(categories):
            y = 3 - i
            bar = Rectangle(width=0.01, height=0.3, color=BLUE).move_to(LEFT * 5 + UP * y)
            car = Text("🏎️", font_size=30).next_to(bar, RIGHT)
            label = Text(cat, font_size=24).next_to(bar, LEFT).shift(LEFT * 0.5)
            self.add(bar, car, label)
            bars.append((bar, val))
            cars.append(car)

        self.wait(1)

        for (bar, val), car in zip(bars, cars):
            new_width = 10 * (val / max_val)
            self.play(bar.animate.stretch_to_fit_width(new_width), run_time=val * 0.05)
            self.play(car.animate.move_to(bar.get_right() + RIGHT * 0.5), run_time=0.2)

        self.wait(2)
