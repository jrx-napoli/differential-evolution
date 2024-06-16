from typing import Callable

from matplotlib import pyplot as plt
import numpy as np


def visualize(y_func: Callable):
    x_1_axis = np.arange(-100, 100, 1)
    x_2_axis = np.arange(-100, 100, 1)
    x_1, x_2 = np.meshgrid(x_1_axis, x_2_axis)
    y = np.zeros_like(x_1)
    for i in range(200):
        for j in range(200):
            x_1_value = x_1[i, j]
            x_2_value = x_2[i, j]
            y[i, j] = y_func(np.array([[x_1_value, x_2_value]]))
    figure = plt.figure()
    axis = figure.add_subplot(projection='3d')
    axis.plot_surface(x_1, x_2, y, cmap='jet')
    axis.set_xlabel("x_1")
    axis.set_ylabel("x_2")
    axis.set_zlabel("y")
    plt.title(f"cec2017 {y_func.__name__}")
    plt.show()
