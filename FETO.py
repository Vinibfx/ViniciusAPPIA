import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title('Classificador de saúde fetal')

dados = pd.read_csv('fetal_health')

st.title('Classificador de saúde fetal\n')
st.write('Nesse projeto vamos Classificador de saúde fetal,como normal, suspeita e patologica')

