import json
import matplotlib.pyplot as plt
from celluloid import Camera

# Load progress from JSON
with open('progress.json', 'r') as f:
    data = json.load(f)

categories = list(data.keys())
final_counts = list(data.values())
problems_solved = [0] * len(categories)

fig, ax = plt.subplots(figsize=(10, 6))
camera = Camera(fig)

# Animate
for step in range(1, max(final_counts) + 1):
    for i in range(len(problems_solved)):
        if problems_solved[i] < final_counts[i]:
            problems_solved[i] += 1
    bars = ax.bar(categories, problems_solved, color='mediumslateblue')
    ax.bar_label(bars, padding=3)
    ax.set_ylim(0, max(final_counts) + 5)
    ax.set_title(f'🚀 LeetCode Progress - Total Solved: {sum(problems_solved)}', fontsize=16)
    ax.set_ylabel("Problems Solved")
    camera.snap()

animation = camera.animate(interval=200)
animation.save('leetcode_progress.gif', writer='pillow')
