from random import*
from itertools import count
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from datetime import datetime

plt.style.use("fivethirtyeight")
x_vals = []
y_vals = []

#plt.plot(x_vals, y_vals)
index=count()

def animate(frame):
    x_vals.append(next(index))
    y_vals.append(randint(0, 5))
    plt.cla()
    plt.plot(x_vals, y_vals)

animation = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()