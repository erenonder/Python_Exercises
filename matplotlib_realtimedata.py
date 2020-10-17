from matplotlib import pyplot as plt
import random
import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


x_vals = []
y_vals = []


# plt.plot(x_vals, y_vals)

index = count()


def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    plt.cla()
    plt.plot(x_vals, y_vals)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.title('Real Time')

plt.xlabel('x axis')
plt.ylabel('y axis')


plt.tight_layout()

plt.show()
