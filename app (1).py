
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
    "Energia": np.random.randint(5, 10, size=7),
    "Jejum (h)": [16, 16, 18, 14, 16, 17, 16],
    "Refeições Planejadas": ["Low carb"] * 7,
    "Treino (min)": np.random.randint(30, 75, size=7),
    "Passos": np.random.randint(5000, 11000, size=7),
    "Calorias": np.random.randint(2200, 2900, size=7),
    "Batimento Médio": np.random.randint(60, 85, size=7),
    "HRV": np.random.randint(35, 70, size=7),
    "Peso (kg)": np.round(np.random.uniform(83.5, 84.5, size=7), 1),
    "Mounjaro": ["✔️", "", "", "", "", "", ""],
    "Venvanse": ["✔️"] * 7,
    "Donarem": ["✔️"] * 7,
    "Suplementos": ["✔️"] * 7,
    "Observações": ["Tudo ok"] * 7
}

df = pd.DataFrame(data)

# Layout Streamlit
st.set_page_config(layout="wide")
st.title("📊 Painel de Saúde Pessoal - Semana Atual")

with st.expander("🛌 Sono & Energia"):
    col1, col2 = st.columns(2)
    col1.line_chart(df.set_index("Data")["Sono (h)"])
    col2.bar_chart(df.set_index("Data")["Energia"])

with st.expander("🥗 Dieta & Jejum"):
    col1, col2 = st.columns(2)
    col1.line_chart(df.set_index("Data")["Jejum (h)"])
    col2.dataframe(df[["Data", "Refeições Planejadas"]].set_index("Data"))

with st.expander("🏃‍♂️ Treino & Movimento"):
    col1, col2 = st.columns(2)
    col1.bar_chart(df.set_index("Data")["Treino (min)"])
    col2.line_chart(df.set_index("Data")["Passos"])

with st.expander("❤️ Indicadores Vitais"):
    st.line_chart(df.set_index("Data")[["Batimento Médio", "HRV", "Peso (kg)"]])

with st.expander("💊 Medicamentos & Suplementos"):
    st.dataframe(df[["Data", "Mounjaro", "Venvanse", "Donarem", "Suplementos"]].set_index("Data"))

with st.expander("📝 Observações"):
    st.dataframe(df[["Data", "Observações"]].set_index("Data"))
