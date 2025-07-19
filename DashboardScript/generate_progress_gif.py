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

        title = Text("LeetCode Progress", font_size=48, color=WHITE).to_edge(UP)
        self.add(title)

        for i, (cat, val) in enumerate(categories):
            y = 3 - i * 0.9  # Vertical spacing
            label = Text(cat, font_size=28, color=WHITE).move_to(LEFT * 5.5 + UP * y)
            bar = Rectangle(width=0.2, height=0.4, color=BLUE, fill_opacity=1).move_to(LEFT * 4 + UP * y)
            car = Text("🏎️", font_size=36).next_to(bar, RIGHT, buff=0.2)

            self.add(label, bar, car)
            bars.append((bar, val))
            cars.append(car)

        self.wait(1)

        for (bar, val), car in zip(bars, cars):
            new_width = 9 * (val / max_val)
            self.play(bar.animate.stretch_to_fit_width(new_width), run_time=val * 0.05)
            self.play(car.animate.move_to(bar.get_right() + RIGHT * 0.5), run_time=0.2)

        self.wait(2)
