import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import datetime

# Importar as funções do seu script de ML (predict_irrigation.py)
# Isso permite reutilizar a lógica de carregamento, preparação e previsão.
from predict_irrigation import load_data_from_db, prepare_data, train_model, make_prediction, DB_NAME

# --- 1. Configurações da Página Streamlit ---
st.set_page_config(
    page_title="FarmTech: Monitoramento de Irrigação",
    page_icon="🌿",
    layout="wide" # Usa a largura total da tela
)

st.title("🌿 FarmTech: Monitoramento Inteligente de Irrigação")
st.markdown("Bem-vindo ao seu dashboard interativo de monitoramento de umidade do solo!")

# --- 2. Carregar e Exibir Dados Históricos ---
st.header("Histórico de Leituras de Umidade")

# Carrega os dados usando a função do seu script de ML
df_data = load_data_from_db(DB_NAME)

if not df_data.empty:
    # Converte a coluna 'timestamp' para datetime para facilitar a visualização
    df_data['timestamp'] = pd.to_datetime(df_data['timestamp'])
    
    # Exibe a tabela de dados
    st.dataframe(df_data.sort_values(by='timestamp', ascending=False), use_container_width=True)

    # Cria um gráfico da umidade ao longo do tempo
    st.subheader("Gráfico de Umidade ao Longo do Tempo")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_data['timestamp'], df_data['umidade_percentual'], marker='o', linestyle='-')
    ax.set_xlabel("Data e Hora")
    ax.set_ylabel("Umidade (%)")
    ax.set_title("Variação da Umidade do Solo")
    ax.grid(True)
    plt.xticks(rotation=45, ha='right') # Rotaciona os labels do eixo X para melhor visualização
    plt.tight_layout() # Ajusta o layout para evitar sobreposição
    st.pyplot(fig) # Exibe o gráfico no Streamlit

else:
    st.warning("Nenhum dado histórico de umidade encontrado. Execute 'setup_db.py' para preencher com dados de exemplo.")

# --- 3. Seção de Previsão de Irrigação ---
st.header("Previsão de Necessidade de Irrigação")

# Criar um slider para o usuário inserir a umidade atual
umidade_input = st.slider(
    "Insira a Umidade Atual do Solo (%)", 
    min_value=0, 
    max_value=100, 
    value=50, # Valor inicial do slider
    step=1 # Passo do slider
)

# Botão para fazer a previsão
if st.button("Fazer Previsão de Irrigação"):
    # Carregar e preparar os dados para treinar o modelo
    # Isso precisa ser feito toda vez que a página é atualizada, mas Streamlit otimiza
    # usando cache, então não é tão pesado.
    X_train, X_test, y_train, y_test = prepare_data(df_data)
    
    if X_train is not None and not X_train.empty:
        # Treinar o modelo
        model = train_model(X_train, y_train)
        
        # Fazer a previsão com o valor de umidade fornecido pelo usuário
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

# --- Opcional: Adicionar a funcionalidade de registrar uma nova leitura ---
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
            # st.experimental_rerun() # Descomente para recarregar automaticamente a página
        except sqlite3.Error as e:
            st.sidebar.error(f"Erro ao adicionar leitura: {e}")
        finally:
            if conn:
                conn.close()

st.sidebar.markdown("---")
st.sidebar.info("Este dashboard utiliza dados históricos para prever a necessidade de irrigação.")