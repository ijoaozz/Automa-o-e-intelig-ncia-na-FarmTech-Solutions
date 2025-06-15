# 🌿 FarmTech Solution - Fase 4  
## Monitoramento Inteligente de Irrigação com IoT e Machine Learning  

Bem-vindo à Fase 4 do projeto **FarmTech Solution**! Este repositório apresenta a evolução de um sistema inteligente para o monitoramento e sugestão de irrigação no agronegócio, integrando tecnologias modernas como **IoT, Machine Learning, banco de dados e dashboards interativos**.

---

## 🎯 Objetivo  

A Fase 4 teve como meta levar o projeto a um novo patamar, adicionando inteligência preditiva, persistência de dados e uma interface interativa para tomada de decisão. O foco foi unir eficiência hídrica com tecnologia de ponta, melhorando o desempenho das fases anteriores.

---

## ⚙️ Tecnologias Utilizadas

- **ESP32 (via Wokwi)** – Microcontrolador utilizado na simulação da leitura de sensores de umidade.
- **Display LCD I2C** – Exibição local da umidade e status da irrigação.
- **Arduino (C/C++)** – Programação do firmware do ESP32.
- **Python 3** – Processamento de dados, aprendizado de máquina e construção do dashboard.
- **Streamlit** – Interface web interativa.
- **SQLite** – Banco de dados local leve para persistência das leituras.
- **Scikit-learn** – Criação do modelo de machine learning.
- **Pandas & Matplotlib** – Manipulação e visualização de dados.
- **Graphviz** – Visualização da árvore de decisão do modelo preditivo.
- **Wokwi** – Simulador online para testes sem hardware físico.

---

## 📁 Estrutura do Projeto

FarmTech-Fase4/
├── ESP32_Wokwi_Code/
│ ├── main.cpp # Código do ESP32
│ └── diagram.json # Circuito Wokwi
├── Python_App/
│ ├── farmtech.db # Banco de dados SQLite
│ ├── setup_db.py # Script de criação do DB
│ ├── predict_irrigation.py # Modelo preditivo
│ ├── app.py # Dashboard Streamlit
│ └── arvore_decisao_farmtech.png # Árvore de decisão
├── .gitignore
└── README.md

yaml
Copy
Edit

---

## 🚀 Como Rodar o Projeto  

### 1. Configurar Ambiente Python  
Certifique-se de ter Python 3.8+ e pip instalados.

```bash
cd FarmTech-Fase4/Python_App
pip install pandas scikit-learn streamlit matplotlib graphviz
2. Instalar o Graphviz (Visualização da Árvore)
Windows: Download oficial

macOS: brew install graphviz

Linux (Debian/Ubuntu): sudo apt-get install graphviz

3. Criar Banco de Dados
bash
Copy
Edit
python setup_db.py
4. Treinar o Modelo de Machine Learning
bash
Copy
Edit
python predict_irrigation.py
5. Rodar o Dashboard
bash
Copy
Edit
streamlit run app.py
🧪 Demonstração
🔌 Simulação no Wokwi
Link do projeto Wokwi (insira o link aqui)
Ajuste o potenciômetro para simular a umidade. O LCD exibe a porcentagem e o status (“OK” ou “IRRIGAR”).

📈 Serial Plotter
Visualize em tempo real as variações de umidade no gráfico do Wokwi.

📊 Dashboard (Streamlit)
Visualização do histórico de leituras.

Gráfico da umidade.

Previsão de irrigação com base na umidade inserida.

Adição manual de novas leituras.

🌳 Árvore de Decisão
Geração automática da imagem da árvore de decisão após rodar o script do modelo.

🧠 Detalhes Técnicos
Otimização do Código ESP32 (C++)
Uso eficiente de memória com tipos como uint8_t, reduzindo consumo e melhorando a performance no microcontrolador.

Estrutura do Banco (SQLite)
Tabela leituras_sensores com colunas:

id (chave primária)

timestamp (data e hora)

umidade_percentual (0-100%)

status_irrigacao ('OK' ou 'IRRIGAR')

Modelo Preditivo (DecisionTreeClassifier)
Treinado com os dados armazenados em SQLite, alcançando 100% de acurácia com os dados de teste (valores sintéticos).

📹 Vídeo Demonstrativo
Confira o funcionamento completo:
📺 Link para o vídeo no YouTube (insira o link aqui)

🔮 Próximos Passos
Integração com sensores reais e módulo relé para automação da irrigação.

Comunicação Wi-Fi com servidor.

Aumento da base de dados e uso de algoritmos mais robustos.

Notificações inteligentes via e-mail ou Telegram.

Dashboard com múltiplas zonas e relatórios.

👨‍💻 Desenvolvido por
[Seu Nome Completo]
Curso: [Nome do Curso / Instituição]
Data: [Mês/Ano]
