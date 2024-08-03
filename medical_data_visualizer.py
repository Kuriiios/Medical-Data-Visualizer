import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / (df['height']/100)**2) > 25
df['overweight'] = df['overweight'].astype(int)

# 3
df['cholesterol'] = df['cholesterol'].replace([1, 2, 3], [0, 1, 1])
df['gluc'] = df['gluc'].replace([1, 2, 3], [0, 1, 1])

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], var_name='variable', value_name='value' )



    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7

    sns.set_theme(style='ticks')

    # 8
    graph = sns.catplot(x='variable', y='total', hue='value', kind='bar', col='cardio', data=df_cat)
    graph.set_axis_labels('Variable', 'Total')
    graph.set_titles('Cardio: {col_name}')


    # 9
    plt.savefig('catplot.png')
    plt.show()
    #return fig
draw_cat_plot()

# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
