import pandas as pd
import streamlit as st #importando o streamlit

st.title('Classificação Saúde Fetal')

dados = pd.read_csv('fetal_health.csv',sep=';')
dados = dados.drop(columns=['id'])#apaga a coluna id
dados.head()
nomes_colunas = dados.columns.to_list()#coloca os nomes das colunas em uma lista
nomes_colunas = nomes_colunas[:len(nomes_colunas)-1]#retiro o 'stroke'
#separando as features das classes
features = dados[nomes_colunas]
classes = dados['stroke']

#componente para converter valores object para inteiro/float
from sklearn.preprocessing import OrdinalEncoder

#dividindo os dados entre treino e teste
from sklearn.model_selection import train_test_split

features_treino,features_teste,classes_treino,classes_teste = train_test_split(features,
                                                                               classes,
                                                                               test_size=0.4,
                                                                               random_state=2)

from sklearn.ensemble import RandomForestClassifier #importa o codigo para gerar florestas randomicas
#criando a floresta
floresta = RandomForestClassifier(n_estimators=1000) #constroi a floresta
#treinar a floresta
floresta.fit(features_treino,classes_treino)

#testar quanto a floresta acerta
predicoes = floresta.predict(features_teste)

st.write('Floresta construida')

f1 = st.number_input('Digite a f1')
f2 = st.number_input('Digite a f2')
f3 = st.number_input('Digite a f3')
f4 = st.number_input('Digite a f4')
f5 = st.number_input('Digite a f5')
f6 = st.number_input('Digite a f6')
f7 = st.number_input('Digite a f7')
f8 = st.number_input('Digite a f8')
f9 = st.number_input('Digite a f9')
f10 = st.number_input('Digite a f10')
f11 = st.number_input('Digite a f11')
f12 = st.number_input('Digite a f12')
f13 = st.number_input('Digite a f13')
f14 = st.number_input('Digite a f14')
f15 = st.number_input('Digite a f15')
f16 = st.number_input('Digite a f16')
f17 = st.number_input('Digite a f17')
f18 = st.number_input('Digite a f18')
f19 = st.number_input('Digite a f19')
f20 = st.number_input('Digite a f20')

if st.button('Qual Classificação de Saúde??'):
  resposta = floresta.predict([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20])#fara a predicao
  st.write(resposta)
