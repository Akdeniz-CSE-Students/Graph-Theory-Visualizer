# -----------------------------------------------
# Code by Yahya Efe Kuruçay - 20220808005
# Website: https://efekurucay.com
# GitHub: https://github.com/Akdeniz-CSE-Students/
# This code is part of my graph theory project.
# -----------------------------------------------
from manim import *

class CountingGraphsComplete(Scene):
    def construct(self):
        # 🚀 Introduction Scene 🚀
        title = Text("Counting Graphs", font_size=48, color=WHITE)
        subtitle = Text("How many different simple graphs can be created?", font_size=32, color=LIGHT_GRAY)
        title.to_edge(UP)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1)

        # 🚀 Theoretical Edge Calculation 🚀
        formula = MathTex(r"B(n, 2) = \frac{n(n - 1)}{2}", font_size=44)
        formula.next_to(subtitle, DOWN, buff=0.4)

        description = Text("This formula calculates the total number of edges in a graph.", font_size=28)
        description.next_to(formula, DOWN, buff=0.3)

        self.play(ReplacementTransform(title, formula))
        self.play(Write(description))
        self.wait(2)

        # Hide formula and description
        self.play(FadeOut(subtitle, shift=UP), FadeOut(formula, shift=UP), FadeOut(description, shift=UP))
        self.wait(0.5)

        # 🚀 Non-Isomorphic Graphs for n=3 🚀
        n3_title = Text("For n=3", font_size=36).to_edge(UP)
        self.play(Write(n3_title))

        p0, p1, p2 = LEFT, RIGHT, UP * 0.7
        dots_n3 = [Dot(p, color=WHITE) for p in [p0, p1, p2]]
        all_8_graphs_n3 = VGroup(
            VGroup(*dots_n3).copy(),
            VGroup(*dots_n3, Line(p0, p1, color=BLUE)).copy(),
            VGroup(*dots_n3, Line(p0, p2, color=BLUE)).copy(),
            VGroup(*dots_n3, Line(p1, p2, color=BLUE)).copy(),
            VGroup(*dots_n3, Line(p0, p1), Line(p0, p2), color=BLUE).copy(),
            VGroup(*dots_n3, Line(p0, p1), Line(p1, p2), color=BLUE).copy(),
            VGroup(*dots_n3, Line(p0, p2), Line(p1, p2), color=BLUE).copy(),
            VGroup(*dots_n3, Line(p0, p1), Line(p0, p2), Line(p1, p2), color=BLUE).copy()
        ).arrange_in_grid(rows=2, cols=4, buff=0.5).scale(0.6).to_edge(DOWN, buff=1.5)

        self.play(LaggedStart(*[Create(graph) for graph in all_8_graphs_n3], lag_ratio=0.1))
        self.wait(1)

        # 🚀 Fading Out Isomorphic Graphs 🚀
        non_iso_indices_n3 = [0, 1, 4, 7]
        for i, graph in enumerate(all_8_graphs_n3):
            if i not in non_iso_indices_n3:
                self.play(graph.animate.set_opacity(0.3).set_color(DARK_GRAY), run_time=0.5)
        self.wait(1)

        # 🚀 Isomorphism Explanation 🚀
        self.play(FadeOut(n3_title))
        self.play(all_8_graphs_n3.animate.shift(UP * 2))
        self.wait(0.5)
        
        # Two isomorphic graphs side by side
        iso_left = VGroup(
            Dot(LEFT * 1.5 + UP * 0.5), Dot(RIGHT * 1.5 + UP * 0.5), Dot(DOWN * 0.7),
            Line(LEFT * 1.5 + UP * 0.5, RIGHT * 1.5 + UP * 0.5, color=BLUE),
            Line(RIGHT * 1.5 + UP * 0.5, DOWN * 0.7, color=BLUE)
        )
        iso_right = VGroup(
            Dot(LEFT * 1.5), Dot(RIGHT * 1.5), Dot(DOWN * 1.5),
            Line(LEFT * 1.5, DOWN * 1.5, color=BLUE),
            Line(RIGHT * 1.5, DOWN * 1.5, color=BLUE)
        )
        iso_text = Text("Why?", font_size=36).next_to(iso_left, UP)

        self.play(FadeIn(iso_left, shift=LEFT), FadeIn(iso_right, shift=RIGHT))
        self.play(Write(iso_text))
        self.wait(1)

        # Right graph transforms into the left one
        self.play(Transform(iso_right, iso_left.copy()), run_time=1.5)
        self.play(iso_text.animate.set_text("Because they are isomorphic!"), run_time=1)
        self.wait(1)

        # n=3 graphs disappear
        self.play(FadeOut(all_8_graphs_n3), FadeOut(iso_left), FadeOut(iso_right), FadeOut(iso_text))
        self.wait(0.5)

        # 🚀 Continue to n=4 🚀
        self.create_n4_graphs_section()

        # 🚀 Closing Message 🚀
        closing_text = Text("Greetings from Efe...", font_size=30)
        github_text = Text("For more resources, visit: github.com/Akdeniz-CSE-Students/", font_size=24)
        closing_text.to_edge(DOWN, buff=1)
        github_text.next_to(closing_text, DOWN, buff=0.2)
        
        self.play(Write(closing_text), FadeIn(github_text, shift=UP))
        self.wait(2)

    def create_n4_graphs_section(self):
        n4_title = Text("11 different non-isomorphic graphs for n=4", font_size=34).to_edge(UP, buff=0.5)
        subtitle_n4 = Text("Only 11 unique structures among 64 possibilities", font_size=24).next_to(n4_title, DOWN, buff=0.15)
        
        self.play(Write(n4_title), Write(subtitle_n4))
        all_graphs_n4 = self.create_n4_graphs()
        all_graphs_n4.shift(DOWN * 0.7)

        self.play(LaggedStart(*[Create(graph) for graph in all_graphs_n4], lag_ratio=0.1), run_time=5)
        self.wait(1)

    def create_n4_graphs(self):
        p0, p1, p2, p3 = UP * 1.2 + LEFT * 1.2, UP * 1.2 + RIGHT * 1.2, DOWN * 1.2 + LEFT * 1.2, DOWN * 1.2 + RIGHT * 1.2
        base_positions = [p0, p1, p2, p3]
        def create_graph(edges):
            return VGroup(
                VGroup(*[Dot(p, color=WHITE) for p in base_positions]),
                *[Line(base_positions[i], base_positions[j], color=BLUE) for i, j in edges]
            )
        
        graphs = [
            create_graph([]), create_graph([(0, 1)]), create_graph([(0, 1), (1, 2)]),
            create_graph([(0, 1), (2, 3)]), create_graph([(0, 1), (0, 2), (0, 3)]),
            create_graph([(0, 1), (1, 2), (2, 3)]), create_graph([(0, 1), (1, 2), (2, 0)]),
            create_graph([(0, 1), (1, 3), (3, 2), (2, 0)]), create_graph([(0, 1), (0, 2), (1, 2)]),
            create_graph([(0, 1), (0, 2), (1, 3), (2, 3)]),
            create_graph([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
        ]

        return VGroup(*graphs).arrange_in_grid(rows=3, cols=4, buff=0.6).scale(0.55)
