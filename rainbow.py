import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from rainbow_plot import RainbowPlot


if __name__ == "__main__":
    sample_0 = [(1,10), (2, 10), (3, 30), (4, 50)]
    sample_1 = [(1,20), (2, 10), (3, 10), (4, 60)]
    sample_2 = [(1,15), (2, 5), (3, 40), (4, 40)]
    sample_3 = [(1,10), (2, 5), (3, 5), (4, 80)]
    sample_4 = [(1,10), (2, 15), (3, 5), (4, 70)]
    sample_5 = [(1,0), (2, 5), (3, 5), (4, 90)]

    legend_labels = [1, 2, 3, 4, 5]

    data = [sample_0, sample_1, sample_2, sample_3, sample_4, sample_5]

    yellow_cmap = LinearSegmentedColormap.from_list(
        "yellow_seq", ["#FFFFE0", "#FFFF00"]
    )
    yellow_palette = [yellow_cmap(i) for i in np.linspace(0, 1, 4)]


    palette = []
    for c in ["Reds", "Oranges", "Yellows", "Greens", "Blues", "RdPu"]:
        if c == "Yellows":
            palette.append(yellow_palette)
        else:
            palette.append(sns.color_palette(c, n_colors=4))


    colors = [palette[i*4:(i+1)*4] for i, val in enumerate(data)] 

    rb = RainbowPlot()

    fig, ax = rb.plot(data, palette, group_by=None, legend=False)

    fig.savefig("rainbow.png")
    plt.close(fig)
