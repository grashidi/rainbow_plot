import matplotlib.pyplot as plt




class RainbowPlot():
    def __init__(self):
        self.radius = 1.5

    def plot(self, data, colors, group_by=None, annot=None, legend=True):
        fig, ax = plt.subplots(sharey=True, figsize=(10,6.5))
        n = len(data)
        r = self.radius
        w = r / n 

        for i, d in enumerate(data):
            w_inner = w
            r = self.radius
            if group_by:
                r, w_inner = self.adjust_rings(i, group_by)

            outer_radius = r
            inner_radius = r - w
            innerring = ax.pie([v[1] for v in d] + [sum(v[1] for v in d)],
                               labels=None,
                               colors=colors[i] + ["white"],
                               autopct=self.autopct_format if annot else None,
                               pctdistance=(inner_radius + outer_radius) / 2 / outer_radius,
                               startangle=0,
                               radius = r,
                               textprops={'fontsize': 14},
                               wedgeprops=dict(width=w, edgecolor='w'))
            self.radius -= w

            plt.setp(innerring[0], width = w_inner)

        if legend:
            legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c, markersize=10) for c in label_colors.values()]

            fig.legend(handles=legend_handles, labels=legend_labels, loc='upper right', fontsize=16)

        plt.subplots_adjust(left=0.1, bottom=-0.5, right=0.9, top=0.9)

        return fig, ax

    def autopct_format(self, pct):
        if pct > 10 and pct != 50:
            return '{:.1f}%'.format(2*pct)
        else:
            return ''

    def adjust_rings(self, i, group_by):
        if i % group_by == 0:
            r = self.radius  * 0.99
            w_inner = w
        elif (i + 1) % group_by == 0:
            r = self.radius
            w_inner = w * 0.95
        else:
            r = self.radius  * 0.99
            w_inner = w - 0.0

        return r, w_inner
