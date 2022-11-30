import pandas as pd
import streamlit as st #importando o streamlit

st.title('Classificador de Saúde Fetal')


dados = pd.read_csv('fetal_health.csv',sep=',')
dados.head()
nomes_colunas = dados.columns.to_list()#coloca os nomes das colunas em uma lista
nomes_colunas = nomes_colunas[:len(nomes_colunas)-2]#retiro o 'stroke'
#separando as features das classes
features = dados[nomes_colunas]
classes = dados['fetal_health']

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

st.write('Classificação Iniciada')

f1 = st.number_input('Digite Frequência cardíaca fetal basal',min_value=106,max_value=160)
f2 = st.number_input('Digite Número de acelerações por segundo',min_value=0.0,max_value=0.019)
f3 = st.number_input('Digite Número de movimentos fetais por segundo',min_value=0.0,max_value=0.48)
f4 = st.number_input('Digite Número de Contrações uterinas por segundo',min_value=0.0,max_value=0.15)
f5 = st.number_input('Digite Número de LDs por segundo',min_value=0.0,max_value=0.15)
f6 = st.number_input('Digite Número de SDs por segundo',min_value=0.0,max_value=0.001)
f7 = st.number_input('Digite Número de DPs por segundo',min_value=0.0,max_value=0.005)
f8 = st.number_input('Digite Porcentagem de tempo com variabilidade anormal de curto prazo',min_value=12,max_value=87)
f9 = st.number_input('Digite Valor médio da variabilidade de curto prazo',min_value=0.20, max_value=7.0)
f10 = st.number_input('Digite Porcentagem de tempo com variabilidade anormal de longo prazo',min_value=0, max_value=91)
f11 = st.number_input('Digite Valor médio da variabilidade de longo prazo',min_value=50,max_value=159)
f12 = st.number_input('Digite Valor mínimo do histograma',min_value=50,max_value=159)
f13 = st.number_input('Digite Valor máximo do histograma',min_value=152,max_value=238)
f14 = st.number_input('Digite Número de picos no histograma do exame',min_value=0,max_value=18)
f15 = st.number_input('Digite Número de zeros no histograma do exame',min_value=0,max_value=10)
f16 = st.number_input('Digite modo hist',min_value=60,max_value=187)
f17 = st.number_input('Digite Hist significa',min_value=73,max_value=187)
f18 = st.number_input('Digite Hist mediana',min_value=77,max_value=186)
f19 = st.number_input('Digite variância histórica',min_value=0,max_value=269)
f20 = st.number_input('Digite tendência do histogramao',min_value=-1,max_value=1)

if st.button('Qual a classificação do seu feto?'):
  resposta = floresta.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20]])#fara a predicao
  
  st.write('testes:',resposta)
  if resposta == 1:
    st.write('Normal')
 if resposta == 2:
    st.write('Suspeito')
 if resposta == 3:
    st.write('Patológico')
 
