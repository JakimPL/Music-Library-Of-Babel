import matplotlib.pyplot as plt
import numpy as np


def plot(array: np.array, plot_type: str = 'plot'):
    plt.figure(figsize=(2 ** 4 - 1, 2), dpi=160, frameon=False)
    plt.axis('off')

    if plot_type == 'scatter':
        plt.scatter(x=range(len(array)), y=array / 255, c='green', s=0.001)
    else:
        plt.plot(array / 255, c='green', linewidth=0.1)

    plt.show()
