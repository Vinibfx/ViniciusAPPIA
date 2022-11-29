
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
st.sidebar.header('Parametro de entrada')

def user_input_features():


normal = (df[df.fetal_health == 0].shape[0])/(df.shape[0])*100
suspeito = (df[df.fetal_health == 1].shape[0])/(df.shape[0])*100
patologico = (df[df.fetal_health == 2].shape[0])/(df.shape[0])*100

print('Porcentagem de fetos considerados normais: {:.1f} %'.format(normal))
print('Porcentagem de fetos considerados suspeitos: {:.1f} %'.format(suspeito))
print('Porcentagem de fetos considerados patológicos: {:.1f} %'.format(patologico))


def melhorando_layout(numero_do_grafico):
  ax[numero_do_grafico].grid(linestyle='--',lw=0.25,aa=True)
  ax[numero_do_grafico].set_frame_on(False)
  ax[numero_do_grafico].tick_params(axis='both',length=0,colors='grey')
  ax[numero_do_grafico].set_xticklabels(['Normal','Suspeito','Patológico'],fontdict={'fontsize':12},color='#6a6a6f',rotation=0)
  return features

df = user_input_features()

st.subheader('User input parameters')
st.write(df)

feto=datesets.fetal_health()

X = fetal_health.data()
Y = fetal_health.tagert()


clf = GaussianNB()  
clf.fit(X,Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.write('Rotulo de classes e numero de indice correspondente')
st.write(fetal_health.target_names)

st.subheader('Predição')
st.write(fetal_health.target_names[prediction])

st.subheader('Probabilidade')
st.write(prediction_proba)

if resultado == ('feto normal')
st.write('normal')

if resultado == ('feto suspeito')
st.write('suspeito')

if resultado == ('feto patologico')
st.write('patologico')
