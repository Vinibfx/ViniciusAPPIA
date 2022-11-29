
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("/content/fetal_health.csv")

df.head()

df.tail()

df.shape

df.isnull().sum()

df.describe()

df.info()

df['fetal_health'].value_counts()

sns.set(font_scale=1.5)
plt.figure(figsize=(20,12))
g = sns.boxenplot(x='fetal_health', y='baseline value', data=df,
             saturation=1.5)
g.set_xlabel('Fetal Health')
g.set_ylabel('Baseline Fetal Heartrate Value')
g.set_title('Frequência cardíaca basal por classificação de saúde fetal', fontsize=20)
plt.show()

sns.set(font_scale=1.5)
plt.figure(figsize=(20,12))
g = sns.boxenplot(x='fetal_health', y='fetal_movement', data=df,
             saturation=1.5)
g.set_xlabel('Fetal Health')
g.set_ylabel('Fetal Movement')
g.set_title('Movimentos Fetais/segundo por Classificação de Saúde', fontsize=20)
plt.show()

sns.set(font_scale=1.5)
plt.figure(figsize=(20,12))
g = sns.boxenplot(x='fetal_health', y='uterine_contractions', data=df,
             saturation=1.5)
g.set_xlabel('Fetal Health')
g.set_ylabel('Uterine Contractions')
g.set_title('Contrações uterinas por classificação de saúde', fontsize=20)
plt.show()

dec_cols = ['light_decelerations', 'severe_decelerations', 'prolongued_decelerations'] #there may be a typo in the last column here

for col in dec_cols:
    sns.set(font_scale=1.5)
    plt.figure(figsize=(16,8))
    g = sns.boxenplot(x='fetal_health', y=col, data=df,
             saturation=1.5)
    g.set_xlabel('Fetal Health')
    g.set_ylabel(col)
    g.set_title('{} & Health Classification'.format(col), fontsize=20)
    plt.show()

pair_cols = ['baseline value', 'accelerations', 'fetal_movement', 'uterine_contractions', 'light_decelerations', 'severe_decelerations', 'prolongued_decelerations', 'fetal_health']

sns.pairplot(df[pair_cols], hue="fetal_health", height=3, aspect=1, palette='magma')
g.fig.subplots_adjust(top=0.95)
g.fig.suptitle('Pairplot for Various Attributes', fontsize=26)
plt.show()

var_cols = ['abnormal_short_term_variability', 'mean_value_of_short_term_variability', 'percentage_of_time_with_abnormal_long_term_variability', 'mean_value_of_long_term_variability']

for col in var_cols:
    sns.set(font_scale=1.5)
    plt.figure(figsize=(16,8))
    g = sns.boxenplot(x='fetal_health', y=col, data=df,
             saturation=1.5)
    g.set_xlabel('Fetal Health')
    g.set_ylabel(col)
    g.set_title('{} '.format(col), fontsize=20)
    plt.show()

var_cols.append('fetal_health')

sns.set(font_scale=1.5)
g = sns.pairplot(df[var_cols], hue="fetal_health", height=5, aspect=1.5, palette='magma')
g.fig.subplots_adjust(top=0.95)
g.fig.suptitle('Pairplot for Abnormal Variability', fontsize=26)
plt.show()

g = sns.relplot(
    data=df,
    x="prolongued_decelerations", y="uterine_contractions",
    hue="fetal_health", height=8, aspect=1.5, palette='plasma')
g.set(title='Contrações Uterinas vs. Desacelerações Prolongadas')
plt.show()

hist_cols = df.columns.tolist()[11:21]

df[hist_cols].hist(bins=15, figsize=(18, 30), layout=(5, 2));
plt.suptitle('Distribuições de Valores de Cardiotocografia')

hist_cols.append('fetal_health')

new_hist_cols = hist_cols[-6:]
sns.set(font_scale=1.5)
g = sns.pairplot(df[new_hist_cols], hue="fetal_health", height=3, aspect=1.0, palette='magma')
g.fig.subplots_adjust(top=0.95)
g.fig.suptitle('Pairplot para gráficos de cardiotocografia', fontsize=26)
plt.show()

g = sns.catplot(x="baseline value", y="prolongued_decelerations", hue="fetal_health",
                palette="plasma", height=6, aspect=2.0,
                data=df)
g.set_xticklabels(rotation=90)
g.set(title='Desacelerações prolongadas e linha de base da frequência cardíaca')
g.despine(left=True)

base_comp_cols = pair_cols[1:-1]
base_comp_cols

f, ax = plt.subplots(figsize=(16,10))
sns.despine(bottom=True, left=True)

sns.stripplot(x="prolongued_decelerations", y="light_decelerations", hue="fetal_health",
              data=df, dodge=True)
ax.set_title('Desacelerações leves vs prolongadas')
plt.show()

sns.set(font_scale=1.0)
plt.figure(figsize=(20, 12)) 
plt.title('Mapa de Calor de Classificação de Saúde Fetal', fontsize=16)
heatmap = sns.heatmap(df.corr(), annot=True)
