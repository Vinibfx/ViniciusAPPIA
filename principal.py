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

f1 = st.number_input('Digite Frequência cardíaca fetal basal (FCF)',min_value=106,max_value=160)
f2 = st.number_input('Digite Número de acelerações por segundo',min_value=0, max_value=0.019)
f3 = st.number_input('Digite Número de movimentos fetais por segundo',min_value=0,max_value=0.48)
f4 = st.number_input('Digite Número de contrações uterinas por segundo'min_value=0, max_value=0.15))
f5 = st.number_input('Digite Número de LDs por segundo'min_value=0, max_value=0.15))
f6 = st.number_input('Digite Número de SDs por segundo'min_value=0, max_value=0.001))
f7 = st.number_input('Digite Número de DPs por segundo'min_value=0, max_value=0.005))
f8 = st.number_input('Digite Porcentagem de tempo com variabilidade anormal de curto prazo'min_value=12, max_value=87))
f9 = st.number_input('Digite Valor médio da variabilidade de curto prazo'min_value=0.20, max_value=7))
f10 = st.number_input('Digite Porcentagem de tempo com variabilidade anormal de longo prazo'min_value=0, max_value=91))'
f11 = st.number_input('Digite Valor médio da variabilidade de longo prazo'min_value=
f12 = st.number_input(
f13 = st.number_input(
f14 = st.number_input(
f15 = st.number_input(
f16 = st.number_input(
f17 = st.number_input(
f18 = st.number_input(
f19 = st.number_input(
f20 = st.number_input(
f21 = st.number_input(

if st.button('O sujeito tera AVC?'):
  resposta = floresta.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]])#fara a predicao
  if resposta == 0:
    st.write('O sujeito nao tera AVC!')
  else:
    st.write('O sujeito tera AVC!')
