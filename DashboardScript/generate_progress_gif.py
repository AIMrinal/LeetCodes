import json
import matplotlib.pyplot as plt
from celluloid import Camera

# Load progress from JSON
with open('progress.json', 'r') as f:
    data = json.load(f)

categories = list(data.keys())
final_counts = list(data.values())
problems_solved = [0] * len(categories)

fig, ax = plt.subplots(figsize=(12, 7))
camera = Camera(fig)

for step in range(1, max(final_counts) + 1):
    # Update progress values
    for i in range(len(problems_solved)):
        if problems_solved[i] < final_counts[i]:
            problems_solved[i] += 1

    # Re-draw the bars
    bars = ax.barh(categories, problems_solved, color='mediumslateblue')
    ax.set_xlim(0, max(final_counts) + 5)
    ax.set_title(f'🏁 LeetCode Progress Race! 🧠🔥 Total Solved: {sum(problems_solved)}', fontsize=16)
    ax.set_xlabel("Problems Solved")

    # Add car emojis
    for i, value in enumerate(problems_solved):
        ax.text(value + 0.5, i, "🏎️", va='center', fontsize=16)

    # Capture the frame
    camera.snap()

# Save animation
animation = camera.animate(interval=200)
animation.save('leetcode_progress.gif', writer='pillow')
