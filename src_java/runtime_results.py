import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(palette='Set2')

df = pd.DataFrame(columns = ['power', 'array', 'vector', 'linked_list'])

# runtime values manually copied from java output
df.loc[0] = [1, 0.000, 0.001, 0.000]
df.loc[1] = [2, 0.000, 0.001, 0.000]
df.loc[2] = [3, 0.001, 0.001, 0.001]
df.loc[3] = [4, 0.001, 0.001, 0.001]
df.loc[4] = [5, 0.003, 0.005, 0.004]
df.loc[5] = [6, 0.030, 0.020, 0.072]
df.loc[6] = [7, 0.454, 0.266, 0.555]
df.loc[7] = [8, 1.038, 3.041, 7.086]
df.loc[8] = [9, 9.546, np.nan, np.nan]

# log(runtime)
df_log = np.log(df[['array', 'vector', 'linked_list']])
df_log = pd.concat([df['power'], df_log], axis=1)
df_log.replace([np.inf, -np.inf], np.nan, inplace=True)

# runtime graph
fig = plt.figure(dpi=200)
sns.lineplot(data=df, x='power', y='array', label='array', alpha=0.7, linewidth=2)
sns.lineplot(data=df, x='power', y='vector', label='vector', alpha=0.7, linewidth=2)
sns.lineplot(data=df, x='power', y='linked_list', label='linked list', alpha=0.7, linewidth=2)
plt.xlabel('10^x numbers')
plt.ylabel('runtime')
plt.show()
fig.savefig('../results/java_runtime.png')

# log(runtime) graph
fig = plt.figure(dpi=200)
sns.lineplot(data=df_log, x='power', y='array', label='array', alpha=0.7, linewidth=2)
sns.lineplot(data=df, x='power', y='vector', label='vector', alpha=0.7, linewidth=2)
sns.lineplot(data=df, x='power', y='linked_list', label='linked list', alpha=0.7, linewidth=2)
plt.xlabel('10^x numbers')
plt.ylabel('log(runtime)')
plt.show()
fig.savefig('../results/java_runtime_log.png')

# copy dataframes to spreadsheet
with pd.ExcelWriter('../results/runtime.xlsx') as writer:
    df.to_excel(writer, sheet_name='java')
    df_log.to_excel(writer, sheet_name='java_log')