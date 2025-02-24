import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(palette='Set2')

def graph_results(data, save_graphs=False):
    df = data
    df = df.reset_index()
    df = df.melt(id_vars=['benchmark', 'length_log'], var_name='collection_type', value_name='runtime')
    
    # RAW RUNTIME
    g = sns.FacetGrid(df, col='benchmark', sharey=False, col_wrap=3, aspect=1.25)
    g.map_dataframe(sns.lineplot, x='length_log', y='runtime', hue='collection_type')
    g.add_legend(ncols=df['collection_type'].nunique(),
                bbox_to_anchor=(0.5, 1.0),
                loc='center',
                fontsize=14)
    g.set_ylabels('runtime (ms)')
    g.set_xlabels('log(length)')
    plt.tight_layout()
    plt.show()
    
    if(save_graphs == True):
        g.savefig('../results/python_runtime.png', dpi=200)

    # LOG(RUNTIME)
    df_log = df
    df_log['runtime'] = df_log['runtime'].map(np.log10)

    g = sns.FacetGrid(df_log, col='benchmark', sharey=False, col_wrap=3, aspect=1.25)
    g.map_dataframe(sns.lineplot, x='length_log', y='runtime', hue='collection_type')
    g.add_legend(ncols=df['collection_type'].nunique(),
                bbox_to_anchor=(0.5, 1.0),
                loc='center',
                fontsize=14)
    g.set_ylabels('log(runtime)')
    g.set_xlabels('log(length)')
    plt.tight_layout()
    plt.show()
    
    if(save_graphs == True):
        g.savefig('../results/python_runtime_log.png', dpi=200)
