import matplotlib
import matplotlib.pyplot as plt
import numpy as np



labels = ['Episode 1', 'Episode 2', 'Episode 3', 'Episode 4', 'Episode 5', 'Episode 6', 'Episode 7', 'Episode 8', 'Episode 9', 'Episode 10']
men_means = [20, 34, 30, 35, 27, 41, 42, 44, 46, 48]
women_means = [25, 32, 34, 20, 25, 32, 34, 36, 38, 40]



x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means, width, label='Men')
rects2 = ax.bar(x + width / 2, women_means, width, label='Women')
rects3 = ax.bar(x - width / 2, men_means, width, label='Men')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
