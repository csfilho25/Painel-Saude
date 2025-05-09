
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("📊 Painel de Saúde Pessoal - Integrado com Apple Health")

st.markdown("""Este painel aceita arquivos CSV exportados do Apple Health (via Health Auto Export, HealthFit ou similar).
Você pode fazer o upload abaixo para atualizar seus dados reais.""")

# Upload do CSV
uploaded_file = st.file_uploader("📥 Faça upload do seu arquivo CSV de saúde", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Arquivo importado com sucesso!")

        # Tentativa de normalização de datas
        if "Date" in df.columns:
            df["Data"] = pd.to_datetime(df["Date"]).dt.date
            df.set_index("Data", inplace=True)
        elif "Data" in df.columns:
            df["Data"] = pd.to_datetime(df["Data"]).dt.date
            df.set_index("Data", inplace=True)
        else:
            st.warning("Coluna de data não identificada no CSV.")

        # Exibição de gráficos básicos
        st.subheader("🛌 Sono (em horas)")
        cols_sono = [col for col in df.columns if "sleep" in col.lower() or "sono" in col.lower()]
        if cols_sono:
            st.line_chart(df[cols_sono[0]])
        else:
            st.info("Nenhuma coluna de sono detectada.")

        st.subheader("❤️ Batimento Médio")
        cols_bpm = [col for col in df.columns if "bpm" in col.lower() or "batimento" in col.lower()]
        if cols_bpm:
            st.line_chart(df[cols_bpm[0]])

        st.subheader("⚖️ Peso (kg)")
        cols_peso = [col for col in df.columns if "peso" in col.lower() or "weight" in col.lower()]
        if cols_peso:
            st.line_chart(df[cols_peso[0]])

        st.subheader("📄 Pré-visualização dos dados")
        st.dataframe(df.head())

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
else:
    st.info("Aguardando upload de arquivo CSV para exibir dados reais.")
