import sqlite3
from datetime import datetime

# Define o nome do arquivo do banco de dados
DB_NAME = 'farmtech.db'

def setup_database():
    """Cria o banco de dados e a tabela de leituras de sensores se não existirem."""
    conn = None
    try:
        # Conecta ao banco de dados (cria o arquivo se não existir)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Cria a tabela leituras_sensores
        # INTEGER PRIMARY KEY AUTOINCREMENT: ID único que aumenta automaticamente
        # TEXT: para strings de texto (como data/hora ou status)
        # INTEGER: para números inteiros (como umidade_percentual)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leituras_sensores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                umidade_percentual INTEGER NOT NULL,
                status_irrigacao TEXT NOT NULL
            )
        ''')
        conn.commit() # Salva as mudanças no banco de dados
        print(f"Banco de dados '{DB_NAME}' e tabela 'leituras_sensores' configurados com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro ao configurar o banco de dados: {e}")
    finally:
        if conn:
            conn.close() # Fecha a conexão com o banco de dados

def insert_sample_data():
    """Insere alguns dados de exemplo para testar."""
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Dados de exemplo para inserir
        # NOTA: No projeto real, esses dados viriam do ESP32!
        sample_data = [
            (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 65, 'OK'),
            (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 20, 'IRRIGAR'),
            (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 70, 'OK'),
            (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 45, 'OK'),
            (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 25, 'IRRIGAR')
        ]

        # Insere os dados na tabela
        cursor.executemany("INSERT INTO leituras_sensores (timestamp, umidade_percentual, status_irrigacao) VALUES (?, ?, ?)", sample_data)
        conn.commit()
        print(f"{len(sample_data)} dados de exemplo inseridos com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro ao inserir dados de exemplo: {e}")
    finally:
        if conn:
            conn.close()

def fetch_all_data():
    """Busca e exibe todos os dados da tabela."""
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leituras_sensores ORDER BY timestamp ASC")
        rows = cursor.fetchall()

        if not rows:
            print("Nenhum dado encontrado na tabela 'leituras_sensores'.")
            return

        print("\nDados no Banco de Dados:")
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"Erro ao buscar dados: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_database()
    insert_sample_data()
    fetch_all_data()