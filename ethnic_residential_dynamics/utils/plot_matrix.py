"""Function to plot a matrix of 1 and -1."""
from argparse import Namespace

from matplotlib import colors
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

COLORS_LABEL = {
    "blue": "Population A",
    "white": "Vacant houses",
    "red": "Population B",
    "black": "Edges",
}
FIGURE_NAME = "neighborhood"
PLOT_LENGTH = 12
PLOT_WIDTH = 6


def plot_citizen_matrix(args: Namespace, matrix: np.ndarray, index: int) -> None:
    """Plot a matrix replacing 1 and -1 by different colors."""
    fig = plt.figure(figsize=(PLOT_LENGTH, PLOT_WIDTH))
    cmap = colors.ListedColormap(colors=COLORS_LABEL.keys())
    plt.imshow(matrix, cmap=cmap)
    labels = [
        mpatches.Patch(color=color, label=label)
        for label, color in sorted({v: k for k, v in COLORS_LABEL.items()}.items())
    ]
    plt.legend(handles=labels)

    fig.savefig(
        ".".join(["/".join([args.plots_path, f"{FIGURE_NAME}_{index}"]), "png"])
    )
