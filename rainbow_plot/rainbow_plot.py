import matplotlib.pyplot as plt




class RainbowPlot():
    def __init__(self):
        self.radius = 1.5
        self.w = 0

    def plot(self, data, colors, group_by=None, annot=None, legend=True):
        fig, ax = plt.subplots(sharey=True, figsize=(10,6.5))
        n = len(data)

        if group_by:
            assert n % group_by == 0 or group_by == 1
        else:
            group_by = 1

        self.w = self.radius / n 

        r = self.compute_radii(n, group_by)

        for i, d in enumerate(data):
            w_inner = self.w

            if (i + 1) % group_by == 0:
                w_inner = self.w - 0.05

            outer_radius = r[i]
            inner_radius = r[i] - (r[0] - r[1]) if len(r) > 2 else r[i] - r[0]

            innerring = ax.pie([v[1] for v in d] + [sum(v[1] for v in d)],
                               labels=None,
                               colors=colors[i] + ["white"],
                               autopct=self.autopct_format if annot else None,
                               pctdistance=(inner_radius + outer_radius) / 2 / outer_radius,
                               startangle=0,
                               radius = r[i],
                               textprops={'fontsize': 14},
                               wedgeprops=dict(width=w_inner, edgecolor='w'))

            self.radius -= self.w

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

    def compute_radii(self, n, group_by): 
        num_groups = n // group_by
        
        # distance of radii within each group
        in_group_dist = round((self.radius - self.w) / n, 1)

        # distance of radii between each group
        # radius - distance taken up radii within each group - width offset / number of group - 1
        gap = round((self.radius - (in_group_dist * num_groups * (group_by - 1)) - self.w) / (num_groups - 1 if group_by > 1 else 1), 1)

        print(in_group_dist, gap, num_groups)
        
        r = [self.w]
        tmp = self.w
        for i in range(n - 1):
            tmp += in_group_dist if (i + 1) % group_by != 0 else gap
            r.append(tmp)

        r = r[::-1]

        return r
