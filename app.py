
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Gerando dados simulados para 7 dias
np.random.seed(42)
dates = [datetime.now().date() - timedelta(days=i) for i in range(6, -1, -1)]

data = {
    "Data": dates,
    "Sono (h)": np.random.uniform(6, 8.5, size=7),
    "Treino (min)": np.random.randint(30, 75, size=7),
    "Calorias Gastas": np.random.randint(2200, 2900, size=7),
    "Batimento Médio": np.random.randint(60, 85, size=7),
    "HRV (ms)": np.random.randint(30, 60, size=7),
    "Jejum (h)": [16, 16, 18, 14, 16, 17, 16],
    "Suplementos Tomados": ["Sim"] * 7,
    "Mounjaro Aplicado": ["Sim", "", "", "", "", "", ""]
}

df = pd.DataFrame(data)

# Layout Streamlit
st.set_page_config(layout="centered")
st.title("📊 Painel Semanal de Saúde")

st.subheader("Sono e Treino")
st.line_chart(df.set_index("Data")["Sono (h)"])
st.bar_chart(df.set_index("Data")["Treino (min)"])

st.subheader("Calorias e Batimentos")
st.line_chart(df.set_index("Data")["Calorias Gastas"])
st.line_chart(df.set_index("Data")["Batimento Médio"])

st.subheader("HRV e Jejum Intermitente")
st.line_chart(df.set_index("Data")["HRV (ms)"])
st.bar_chart(df.set_index("Data")["Jejum (h)"])

st.subheader("Controle Diário")
st.dataframe(df[["Data", "Suplementos Tomados", "Mounjaro Aplicado"]].set_index("Data"))
