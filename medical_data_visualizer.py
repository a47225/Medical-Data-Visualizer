import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = np.where((df['weight'] / ((df['height']/100)**2))>25,1,0)

# 3
df.loc[df['cholesterol']==1,'cholesterol']=0
df.loc[df['cholesterol']>1,'cholesterol']=1
df.loc[df['gluc']==1,'gluc']=0
df.loc[df['gluc']>1,'gluc']=1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df[['id','cardio','active','alco','cholesterol','gluc','overweight','smoke']],id_vars=['id','cardio'])
    df_cat['total'] = df_cat.loc[:, 'value']


    # 6
    df_cat = df_cat.pivot_table(index=['variable','cardio','value'],values='total',aggfunc = 'count')
    

    # 7



    # 8
    fig = sns.catplot(df_cat,x='variable',y='total',hue='value',kind="bar",col='cardio').fig
    

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.copy()
    df_heat['height'] = df_heat['height'] / 100
    df_heat.drop(df_heat.loc[df_heat['ap_lo'] > df_heat['ap_hi']].index, inplace=True)
    df_heat.drop(df_heat.loc[(df['height'] < df['height'].quantile(0.025))].index, inplace = True)
    df_heat.drop(df_heat.loc[(df['height'] > df['height'].quantile(0.975))].index, inplace = True)
    df_heat.drop(df_heat.loc[(df['weight'] < df['weight'].quantile(0.025))].index, inplace = True)
    df_heat.drop(df_heat.loc[(df['weight'] > df['weight'].quantile(0.975))].index, inplace = True)
    df_heat

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))



    # 14
    fig, ax = plt.subplots(1,1)
    ax = sns.heatmap(corr,annot=True,mask=mask,fmt="0.1f")

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
