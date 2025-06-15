import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, classification_report
import graphviz # Para visualizar a árvore de decisão

# --- Configurações do Banco de Dados ---
DB_NAME = 'farmtech.db'

# --- 1. Carregar os Dados do Banco de Dados ---
def load_data_from_db(db_name):
    """Carrega os dados da tabela 'leituras_sensores' do SQLite para um DataFrame Pandas."""
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        # Consulta SQL para selecionar as colunas de interesse
        # 'timestamp' para contexto, 'umidade_percentual' como nossa 'feature' (característica)
        # e 'status_irrigacao' como nosso 'target' (o que queremos prever)
        query = "SELECT timestamp, umidade_percentual, status_irrigacao FROM leituras_sensores"
        
        # Lê os dados diretamente para um DataFrame do Pandas
        df = pd.read_sql_query(query, conn)
        print(f"Dados carregados do banco de dados:\n{df.head()}") # Mostra as 5 primeiras linhas
        return df
    except sqlite3.Error as e:
        print(f"Erro ao carregar dados do banco de dados: {e}")
        return pd.DataFrame() # Retorna um DataFrame vazio em caso de erro
    finally:
        if conn:
            conn.close()

# --- 2. Preparar os Dados para o Machine Learning ---
def prepare_data(df):
    """Prepara o DataFrame para o treinamento do modelo."""
    if df.empty:
        print("DataFrame vazio, impossível preparar dados.")
        return None, None, None, None

    # As 'features' (X) são as colunas que o modelo vai usar para aprender.
    # Neste caso, a umidade percentual.
    X = df[['umidade_percentual']]
    
    # O 'target' (y) é a coluna que o modelo vai tentar prever.
    # Queremos prever o 'status_irrigacao'.
    y = df['status_irrigacao']

    # Converter o 'status_irrigacao' de texto para números, porque modelos de ML
    # geralmente trabalham melhor com números.
    # 'OK' = 0, 'IRRIGAR' = 1
    # Isso é chamado de 'codificação de rótulos' ou 'Label Encoding'.
    y = y.map({'OK': 0, 'IRRIGAR': 1})

    # Dividir os dados em conjuntos de treinamento e teste.
    # train_size=0.8 significa que 80% dos dados serão para treinar o modelo
    # e 20% para testar se ele aprendeu bem.
    # random_state é para garantir que a divisão seja sempre a mesma cada vez que você rodar o código.
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)
    
    print("\nDados preparados:")
    print(f"X_train (treinamento de features):\n{X_train.head()}")
    print(f"y_train (treinamento de target):\n{y_train.head()}")
    print(f"X_test (teste de features):\n{X_test.head()}")
    print(f"y_test (teste de target):\n{y_test.head()}")

    return X_train, X_test, y_train, y_test

# --- 3. Criar e Treinar o Modelo de Machine Learning ---
def train_model(X_train, y_train):
    """Treina um modelo de Árvore de Decisão."""
    # Criar o modelo. max_depth limita o tamanho da árvore para evitar 'overfitting'.
    # Overfitting é quando o modelo decora os dados de treino e não generaliza bem para novos dados.
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    
    # Treinar o modelo com os dados de treinamento
    model.fit(X_train, y_train)
    print("\nModelo de Árvore de Decisão treinado com sucesso.")
    return model

# --- 4. Avaliar o Modelo (Opcional, mas Importante!) ---
def evaluate_model(model, X_test, y_test):
    """Avalia o desempenho do modelo nos dados de teste."""
    if X_test is None or y_test is None or X_test.empty or y_test.empty:
        print("Dados de teste vazios, impossível avaliar o modelo.")
        return

    y_pred = model.predict(X_test) # Fazer previsões nos dados de teste
    
    # Calcular a acurácia (precisão) do modelo
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAcurácia do modelo nos dados de teste: {accuracy:.2f}") # .2f formata para 2 casas decimais

    # Relatório de classificação (mostra precisão, recall, f1-score para cada classe)
    # Target_names ajuda a entender qual classe é 0 e qual é 1
    report = classification_report(y_test, y_pred, target_names=['OK', 'IRRIGAR'])
    print("\nRelatório de Classificação:\n", report)

# --- 5. Fazer Previsões com o Modelo ---
def make_prediction(model, umidade_atual):
    """Faz uma previsão para um novo valor de umidade."""
    # A entrada para o modelo precisa ser no formato que ele foi treinado (DataFrame)
    new_data = pd.DataFrame([[umidade_atual]], columns=['umidade_percentual'])
    
    # Fazer a previsão
    prediction_numeric = model.predict(new_data)
    
    # Converter a previsão numérica de volta para texto
    prediction_text = 'IRRIGAR' if prediction_numeric[0] == 1 else 'OK'
    
    print(f"\nPrevisão para Umidade {umidade_atual}%: {prediction_text}")
    return prediction_text

# --- Visualizar a Árvore de Decisão (Opcional, mas muito legal!) ---
def visualize_tree(model, feature_names, class_names):
    """Gera uma visualização da árvore de decisão."""
    dot_data = export_graphviz(
        model, 
        out_file=None, 
        feature_names=feature_names, 
        class_names=class_names,
        filled=True, 
        rounded=True, 
        special_characters=True
    )
    graph = graphviz.Source(dot_data)
    graph.render("arvore_decisao_farmtech", format="png", view=True) # Salva como PNG e abre
    print("\nÁrvore de Decisão gerada e salva como 'arvore_decisao_farmtech.png'.")
    print("Verifique a pasta do seu projeto.")

# --- Execução Principal do Script ---
if __name__ == "__main__":
    # Carregar os dados
    data_df = load_data_from_db(DB_NAME)

    # Preparar os dados para o ML
    X_train, X_test, y_train, y_test = prepare_data(data_df)

    if X_train is not None:
        # Treinar o modelo
        farmtech_model = train_model(X_train, y_train)

        # Avaliar o modelo (se houver dados de teste)
        evaluate_model(farmtech_model, X_test, y_test)

        # Exemplo de Previsão:
        # Vamos prever o que o sistema faria com 15% de umidade e com 80%
        make_prediction(farmtech_model, 15) # Exemplo: umidade baixa
        make_prediction(farmtech_model, 80) # Exemplo: umidade alta

        # Visualizar a árvore (requer Graphviz instalado no sistema, mas o código já tenta abrir)
        # Se você tiver problemas para abrir a imagem, a parte importante é que o arquivo .png será gerado.
        visualize_tree(farmtech_model, ['umidade_percentual'], ['OK', 'IRRIGAR'])

    else:
        print("Não foi possível treinar o modelo devido à falta de dados.")