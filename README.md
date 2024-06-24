# Rainbow Plot
<img src=doc/img/rainbow.png width="600px">
A semi-circle pie chart for Python supporting bar grouping and percentage annotation.

## Installation
```
cd rainbow_plot && pip install -e . 
```

## Usage
Example for creating a grouped rainbow plot with with 3 groups each containing 2 semi-circles including annotation.

```python
import seaborn as sns
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

    palette = []
    for c in ["Blues"] * len(data):
        palette.append(sns.color_palette(c, n_colors=len(sample_0)))

    rb = RainbowPlot()

    fig, ax = rb.plot(data, palette, group_by=2, legend=False, annot=True)

    ax.set_title("Example", fontsize=20, y=1.1)

    ax.text(-1.35, -0.1, "1", ha="center", va="center", fontsize=18, fontweight='bold')
    ax.text(-1.15, -0.1, "2", ha="center", va="center", fontsize=18, fontweight='bold')
    ax.text(-0.85, -0.1, "3", ha="center", va="center", fontsize=18, fontweight='bold')
    ax.text(-0.65, -0.1, "4", ha="center", va="center", fontsize=18, fontweight='bold')
    ax.text(-0.35, -0.1, "5", ha="center", va="center", fontsize=18, fontweight='bold')
    ax.text(-0.15, -0.1, "6", ha="center", va="center", fontsize=18, fontweight='bold')
    
    ax.text(-1.25, -0.22, "Group\n1", ha="center", va="center", fontsize=16, fontweight='bold', color="lightgrey")
    ax.text(-0.75, -0.22, "Group\n2", ha="center", va="center", fontsize=16, fontweight='bold', color="lightgrey")
    ax.text(-0.25, -0.22, "Group\n3", ha="center", va="center", fontsize=16, fontweight='bold', color="lightgrey")


    fig.savefig("example.png")
    plt.close(fig)
```
<img src=doc/img/example.png width="450px">
