# IMPORTANDO BIBLIOTECAS NECESSÁRIAS
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import datetime

# IMPORTANDO FUNÇÕES DO SCRIPT (predict_irrigation.py)
from predict_irrigation import load_data_from_db, prepare_data, train_model, make_prediction, DB_NAME

# CONFIG PÁGINA STREAMLIT
st.set_page_config(
    page_title="FarmTech: Monitoramento de Irrigação",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 FarmTech: Monitoramento Inteligente de Irrigação")
st.markdown("Bem-vindo ao seu dashboard interativo de monitoramento de umidade do solo!")

# CARREGANDO E EXIBINDO DADOS HISTÓRICOS
st.header("Histórico de Leituras de Umidade")

# CARREGANDO DADOS USANDO FUNÇÃO DO SCRIPT
df_data = load_data_from_db(DB_NAME)

if not df_data.empty:
    # FACILITANDO A VISUALIZAÇÃO - Converte a coluna 'timestamp' para datetime
    df_data['timestamp'] = pd.to_datetime(df_data['timestamp'])
    
    # EXIBE TABELA DE DADOS
    st.dataframe(df_data.sort_values(by='timestamp', ascending=False), use_container_width=True)

    # GRÁFICO DE UMIDADE AO LONGO DO TEMPO
    st.subheader("Gráfico de Umidade ao Longo do Tempo")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_data['timestamp'], df_data['umidade_percentual'], marker='o', linestyle='-')
    ax.set_xlabel("Data e Hora")
    ax.set_ylabel("Umidade (%)")
    ax.set_title("Variação da Umidade do Solo")
    ax.grid(True)
    plt.xticks(rotation=45, ha='right') # ROTACIONANDO LABELS DO EIXO X PARA MELHORAR A VISUALIZAÇÃO 
    plt.tight_layout() # AJUSTA O LAYOUT
    st.pyplot(fig) # GRÁFICO DO STREAMLIT

else:
    st.warning("Nenhum dado histórico de umidade encontrado. Execute 'setup_db.py' para preencher com dados de exemplo.")

# PREVISÃO IRRIGAÇÃO
st.header("Previsão de Necessidade de Irrigação")

# SLIDER PARA O USUÁRIO INSERIR A UMIDADE
umidade_input = st.slider(
    "Insira a Umidade Atual do Solo (%)", 
    min_value=0, 
    max_value=100, 
    value=50, # VALOR INICIAL DO SLIDER
    step=1 
)

# BOTÃO PREVISÃO
if st.button("Fazer Previsão de Irrigação"):
    # CARREGAR E PREPARAR DADOS PARA TREINAR O MODELO
    X_train, X_test, y_train, y_test = prepare_data(df_data)
    
    if X_train is not None and not X_train.empty:
        # TREINAR MODELO 
        model = train_model(X_train, y_train)
        
        # PREVISÃO COM O VALOR DA UMIDADE FORNECIDA PELO USUÁRIO
        prediction = make_prediction(model, umidade_input)
        
        st.subheader(f"Resultado da Previsão para {umidade_input}% de Umidade:")
        if "IRRIGAR" in prediction.upper():
            st.error(f"💧 **ATENÇÃO: É NECESSÁRIO IRRIGAR!** ({prediction})")
        else:
            st.success(f"✅ **Umidade OK.** Não é necessária irrigação no momento. ({prediction})")
    else:
        st.warning("Não foi possível treinar o modelo para fazer previsões. Dados históricos insuficientes.")

st.markdown("---")
st.markdown("Desenvolvido para FarmTech por [Seu Nome/Empresa]")

# OPICIONAL: Adicionar a funcionalidade de registrar uma nova leitura
st.sidebar.header("Registrar Nova Leitura")
with st.sidebar.form("new_reading_form"):
    new_umidade = st.number_input("Umidade (%)", min_value=0, max_value=100, value=50, step=1)
    new_status = st.selectbox("Status de Irrigação (para treino do modelo)", ["OK", "IRRIGAR"])
    submit_button = st.form_submit_button("Adicionar Leitura")

    if submit_button:
        conn = None
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("INSERT INTO leituras_sensores (timestamp, umidade_percentual, status_irrigacao) VALUES (?, ?, ?)",
                           (timestamp, new_umidade, new_status))
            conn.commit()
            st.sidebar.success("Leitura adicionada com sucesso! Recarregue a página para ver o histórico atualizado.")
           
        except sqlite3.Error as e:
            st.sidebar.error(f"Erro ao adicionar leitura: {e}")
        finally:
            if conn:
                conn.close()

st.sidebar.markdown("---")
st.sidebar.info("Este dashboard utiliza dados históricos para prever a necessidade de irrigação.")
