import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(palette='Set2')

def graph_results(data, is_log=False, save_graphs=False):
    df = data
    df = df.reset_index()
    df = df.melt(id_vars=['benchmark', 'length_log'], var_name='collection_type', value_name='runtime')
    
    if is_log:
        ylabel = "log(runtime)"
        filename = "python_runtime_log"
    else:
        ylabel = "runtime (ms)"
        filename = "python_runtime"
    
    g = sns.FacetGrid(df, col='benchmark', sharey=False, col_wrap=3, aspect=1.25)
    g.map_dataframe(sns.lineplot, x='length_log', y='runtime', hue='collection_type')
    g.add_legend(ncols=df['collection_type'].nunique(),
                bbox_to_anchor=(0.5, 1.0),
                loc='center',
                fontsize=14)
    g.set_ylabels(ylabel)
    g.set_xlabels('log(length)')
    plt.tight_layout()
    plt.show()
    
    if(save_graphs):
        g.savefig(f'../results/{filename}.png', dpi=200)
