import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from datetime import datetime

# Initialize data storage
x_data = []
y_data = []

# Create the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o', linestyle='-', color='b', label='Random Data')
ax.set_title('Dynamic Random Data Plot')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Random Value')
ax.set_ylim(0, 100)  # Set Y-axis limits
ax.legend()
ax.grid(True)


# Function to initialize the plot
def init():
    ax.set_xlim(0, 10)  # Set initial x-axis limits
    return line,


# Function to update the plot
def update(frame):
    # Extend x-axis and add a new random value
    x_data.append(len(x_data))  # Use the current length as the x value
    y_data.append(np.random.randint(0, 100))  # Random value between 0 and 100

    # Update the line with new data
    line.set_data(x_data, y_data)

    # Update x-axis limits to show all data points
    ax.set_xlim(0, len(x_data) - 1)  # Update x-axis to show all data points
    return line,


# Create the animation that updates every 2 seconds (2000 ms)
animation = FuncAnimation(fig, update, init_func=init, interval=2000, blit=True, save_count=100)

# Show the plot
plt.show()
