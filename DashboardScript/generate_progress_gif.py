import json
import matplotlib.pyplot as plt
from celluloid import Camera

# Use a font that contains color emoji glyphs
plt.rcParams['font.family'] = 'Noto Color Emoji'

with open('progress.json', 'r') as f:
    data = json.load(f)

categories = list(data.keys())
final_counts = list(data.values())

# Safety check
if not categories or max(final_counts) == 0:
    raise ValueError("No progress data found in progress.json or all values are 0.")

problems_solved = [0] * len(categories)

fig, ax = plt.subplots(figsize=(12, 7))
plt.subplots_adjust(left=0.3)
camera = Camera(fig)

for step in range(1, max(final_counts) + 1):
    for i in range(len(problems_solved)):
        if problems_solved[i] < final_counts[i]:
            problems_solved[i] += 1

    bars = ax.barh(categories, problems_solved, color='mediumslateblue')
    ax.set_xlim(0, max(final_counts) + 5)
    ax.set_title(
        f'🏁 LeetCode Progress Race! 🧠🔥 Total Solved: {sum(problems_solved)}',
        fontsize=16
    )
    ax.set_xlabel("Problems Solved")

    for i, value in enumerate(problems_solved):
        ax.text(value + 0.5, i, "🏎️", va='center', fontsize=16)

    camera.snap()

animation = camera.animate(interval=200)
# Use ImageMagick writer to preserve true-color & emoji
animation.save('leetcode_progress.gif', writer='imagemagick')
