import matplotlib.pyplot as plt
import seaborn as sns

def change_width(ax, new_value, orient='v') :
    for patch in ax.patches :

        if orient == 'v':
            current_width = patch.get_height()
        else:
            current_width = patch.get_width()

        diff = current_width - new_value
        
        if orient == 'v':
            patch.set_height(new_value)
            patch.set_y(patch.get_y() + diff * .5)
        else:
            patch.set_width(new_value)
            patch.set_x(patch.get_x() + diff * .5)
        
def format_barplot(orient ='h', bar_width=1, title='TITLE', xlabel="X-LABEL", xticks=['A','B'], g=None):
    

    change_width(g, bar_width, orient)

    g.axes.yaxis.set_visible(False)

    g.set_title(title, pad=20, fontdict={'fontsize': 18})
    g.set_xlabel(xlabel, fontdict={'fontsize': 14})
    g.set_xticklabels(xticks, fontdict={'fontsize': 12})

    sns.despine(fig=None, ax=None, top=True, right=True, left=True, 
            bottom=False, offset=None, trim=False)

def annotate_bars(g, scale=1, unit=''):
    for p in g.patches:
            g.annotate('{}{}'.format(round(p.get_height()*scale,2), unit).replace('.',','),
                    xy=(p.get_x() + p.get_width() / 2, p.get_height()),
                    size=12,
                    xytext=(0, 4),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')