import base64
from io import BytesIO

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np


def plot(array: np.array, plot_type: str = 'plot', save: bool = False, step: int = 50):
    plt.figure(figsize=(25, 2), dpi=80, frameon=False)
    plt.axis('off')

    y = (array / 255)[::step]
    if plot_type == 'scatter':
        plt.scatter(x=range(0, len(array), step), y=y, c='green', s=0.001)
    else:
        plt.plot(y, c='green', linewidth=0.2)

    if save:
        image = BytesIO()
        plt.savefig(image, format='png', bbox_inches='tight')
        plt.close()
        return base64.b64encode(image.getvalue())
    else:
        plt.show()
        plt.close()

