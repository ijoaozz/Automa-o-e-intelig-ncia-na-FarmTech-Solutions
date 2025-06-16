# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🌿 Projeto Cap 1 - Automação e inteligência na FarmTech Solutions  
## Monitoramento Inteligente de Irrigação com IoT e Machine Learning

---

## 👨‍🎓 Integrantes e Responsabilidades:

| Nome Completo                     | RM        |
|----------------------------------|-----------|
| Daniele Antonieta Garisto Dias  | RM565106  |
| Leandro Augusto Jardim da Cunha | RM561395  |
| Luiz Eduardo da Silva           | RM561701  |
| João Victor Viana de Sousa      | RM565136  |

---

## 👩‍🏫 Professores:
### Tutor(a) 
- <a>Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a>Andre Godoi Chiovato</a>

---

## 🎯 Introdução e Objetivo

Bem-vindo à Fase 4 do projeto **FarmTech Solution**! Este repositório apresenta a evolução de um sistema inteligente para o monitoramento e sugestão de irrigação no agronegócio, integrando tecnologias modernas como **IoT, Machine Learning, banco de dados e dashboards interativos**.
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

# 🧪 Demonstração Completa do FarmTech Solution

## 🔌 Simulação Detalhada no Wokwi
O simulador online Wokwi serve como nosso laboratório virtual para o hardware. Aqui, você pode interagir diretamente com o potenciômetro (que emula com precisão um sensor de umidade de solo real) e observar as respostas do sistema em tempo real. O display LCD I2C conectado ao ESP32 exibirá as principais métricas: a porcentagem de umidade e o status atual da irrigação (indicando se é "OK" ou "IRRIGAR"). Esta é a sua janela para ver como o sistema se comportaria no campo.

<br>

Link Direto para o Projeto Wokwi: (https://wokwi.com/projects/433860973697108993)

<br>

<img src="assets/SerialPlotter.png" alt="SerialPlotter" width="500"/>

<br>

<img src="assets/SerialPlotter.png" alt="SerialPlotter2" width="500"/>

<br>

<img src="assets/SerialPlotter.png" alt="SerialPlotter3" width="500"/>
 
---


