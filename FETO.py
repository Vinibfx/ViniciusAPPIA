import streamlit as st
st.title('Classificador de saúde fetal')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
dados = pd.read_csv('fetal_health')

st.title('Classificador de saúde fetal\n')
st.write('Nesse projeto vamos Classificador de saúde fetal,como normal, suspeita e patologica')

