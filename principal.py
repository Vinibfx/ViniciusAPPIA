import pandas as pd

dados = pd.read_csv('/content/fetal_health.csv',sep=',')
dados.info()

dados.head()
nomes_colunas = dados.columns.to_list()#coloca os nomes das colunas em uma lista
nomes_colunas = nomes_colunas[:len(nomes_colunas)-1]#retiro o 'stroke'
#separando as features das classes
features = dados[nomes_colunas]
classes = dados['fetal_health']
classes
