# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🌿 Projeto Cap 1 - Automação e inteligência na FarmTech Solutions  

---

## 🚀 Visão Geral do Projeto

Este repositório apresenta a **concretização da Fase 4** do **FarmTech Solutions**, um sistema avançado de **automação e inteligência preditiva** concebido para transformar a **gestão hídrica no agronegócio**. Distinguindo-se por sua abordagem inovadora, o projeto integra de forma sinérgica **Internet das Coisas (IoT)**, **Machine Learning (ML)** e **persistência de dados geoespaciais**, culminando em uma plataforma que vai além do monitoramento, promovendo a **predição e otimização autônoma** do uso de recursos hídricos. Nesta fase, nosso foco primordial foi a transição de um *protótipo conceitual* para uma *solução com inteligência embarcada proativa*, redefinindo os paradigmas de **eficiência hídrica** e **produtividade agrícola**.

Por meio da **emulação de sensores de campo**, da **modelagem preditiva avançada** e de uma **interface interativa de alto desempenho**, o FarmTech Solutions estabelece um pipeline completo e distintivo para a **tomada de decisões estratégicas baseadas em dados**, impulsionando o ecossistema da **agricultura inteligente**.

---

## 👨‍🎓 Integrantes e Responsabilidades:

 Nome Completo                           | RM       | Responsabilidades Principais |
|-----------------------------------------|----------|------------------------------|
| **Daniele Antonieta Garisto Dias**      | RM565106 | **Data Engineering & ML Ops**<br>- Estruturação do pipeline de dados em Python/SQLite<br>- Versionamento e retraining do modelo no Scikit-learn |
| **Leandro Augusto Jardim da Cunha**     | RM561395 | **Firmware & Hardware**<br>- Programação do ESP32 em C/C++<br>- Otimizações de memória e testes no simulador Wokwi |
| **Luiz Eduardo da Silva**               | RM561701 | **Modelagem Preditiva & Dashboard**<br>- Criação e validação dos modelos de ML<br>- Construção da interface Streamlit e documentação técnica |
| **João Victor Viana de Sousa**          | RM565136 | **Gestão de Projeto & Banco de Dados**<br>- Coordenação do cronograma (Scrum Sprints)<br>- Design do esquema relacional e consultas SQL |

---

## 👩‍🏫 Professores:
### Tutor(a) 
- <a>Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a>Andre Godoi Chiovato</a>

---

## 🎯 Introdução e Objetivo

Bem-vindo à **Fase 4** do **FarmTech Solutions**, um projeto que transcende a mera automação para embarcar na era da **agricultura inteligente e autossustentável**. Este repositório documenta a evolução crítica de um sistema inicialmente concebido para monitoramento para uma solução proativa de **sugestão e otimização de irrigação** no agronegócio. Integrando **tecnologias disruptivas** como IoT para aquisição de dados em tempo real, Machine Learning para inferência preditiva, bancos de dados robustos para persistência informacional e dashboards interativos para visualização e controle, o FarmTech Solutions se posiciona na vanguarda da inovação agrícola.

A meta primordial da Fase 4 foi impulsionar o projeto a um patamar de **inteligência operacional e persistência de dados sem precedentes**. Isso incluiu a incorporação de **modelos preditivos** capazes de antecipar a demanda hídrica, a implementação de um sistema de **persistência de dados leve e eficiente** para garantir a rastreabilidade e a análise histórica, e o desenvolvimento de uma **interface interativa intuitiva** que capacita o agricultor com informações em tempo real para tomada de decisão estratégica. O foco central reside na simbiose entre **eficiência hídrica e tecnologia de ponta**, visando aprimorar substancialmente o desempenho das fases anteriores e consolidar o FarmTech Solutions como uma **referência em inovação tecnológica para o agronegócio**.

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

## 🌿 Herança Fase 3: Máquina Agrícola Inteligente

Este projeto incorpora princípios e abordagens metodológicas semelhantes, servindo como uma extensão conceitual da proposta anterior realizada na Fase 3.

<p>

Entre as principais funcionalidades estavam:
 
<p>

- Dashboard interativo com dados ambientais e alertas;

- Automação de irrigação baseada em previsão do tempo via API Open-Meteo;

- Cadastro, edição, exclusão e importação de dados sensoriais via CSV;

- Consultas SQL para análises técnicas, como controle de água aplicada e variação do pH do solo;

- Modelagem relacional robusta, com MER detalhado e tabelas normalizadas.

Esses fundamentos, mesmo que em outro contexto tecnológico, serviram como inspiração para o desenvolvimento do FarmTech Solutions, que agora avança ao incorporar:

- Machine Learning com Scikit-learn;

- Interface interativa com Streamlit;

- Persistência local com SQLite;

- Simulação embarcada com ESP32.

A partir dessa base sólida, o novo projeto visa expandir o uso de modelos preditivos, painéis operacionais e automação inteligente, aplicando conceitos avançados de análise de dados e integração com sistemas externos.

---

# 🧪 Demonstração Completa do FarmTech Solution

## 🔌 Simulação Detalhada no Wokwi
O simulador online Wokwi serve como nosso laboratório virtual para o hardware. Aqui, você pode interagir diretamente com o **potenciômetro** (que emula com precisão um sensor de umidade de solo real) e observar as respostas do sistema em tempo real. O **display LCD I2C** conectado ao **ESP32** exibirá as principais métricas: **a porcentagem de umidade** e o **status atual da irrigação** (indicando se é "OK" ou "IRRIGAR"). Esta é a sua janela para ver como o sistema se comportaria no campo.

<br>

**Link Direto para o Projeto Wokwi: (https://wokwi.com/projects/433860973697108993)**

<br>

<img src="assets/SerialPlotter.png" alt="OK" width="500"/>

<br>

<img src="assets/SerialPlotter2.png" alt="OK" width="500"/>

<br>

<img src="assets/SerialPlotter3.png" alt="IRRIGAR" width="500"/>
 
---

## 📈 Análise Dinâmica com o Serial Plotter
O Serial Plotter do Wokwi é uma ferramenta diagnóstica incrivelmente poderosa e visualmente intuitiva. Ele transforma os dados brutos de umidade, que o ESP32 está coletando, em um gráfico em tempo real. Isso permite que você observe as flutuações e tendências da umidade de forma dinâmica e imediata, auxiliando na análise do comportamento do sensor e do sistema.

<img src="assets/GRAFICOSerialPlotter.png" alt="SERIALPLOTTER" width="500"/>

---

## 📊 Dashboard Interativo com Streamlit
Este é o seu centro de comando centralizado! O dashboard interativo, construído com Streamlit, é a sua principal interface para visualizar o histórico de dados do sensor, interagir com o modelo preditivo de Machine Learning e tomar decisões informadas sobre a irrigação do solo.

- **Visualização do Histórico de Leituras:** O dashboard apresenta uma tabela detalhada e organizada de todas as medições de umidade que foram armazenadas no seu banco de dados. Complementando a tabela, um gráfico intuitivo de linha exibe a variação da umidade ao longo do tempo, permitindo uma rápida compreensão das tendências.

- **Previsão de Irrigação Instantânea:** Esta é a funcionalidade estrela do FarmTech! Utilize um slider interativo para simular um nível de umidade atual do solo. Com um simples clique no botão "Fazer Previsão de Irrigação", o modelo de Machine Learning do FarmTech fornecerá uma previsão instantânea sobre a necessidade de irrigação para aquela umidade específica.

- **Adição Manual de Novas Leituras:** Na barra lateral (sidebar) do dashboard, você encontrará uma funcionalidade útil para adicionar manualmente novas medições de umidade e seus respectivos status. Isso é fundamental para expandir seu conjunto de dados de treino, simulando a coleta contínua de informações do sensor para futuras análises e o aprimoramento contínuo do modelo.

<br>

<img src="assets/Streamlit.png" alt="Streamlit" width="500">

<br>

<img src="assets/Streamlit2.png" alt="Streamlit" width="500">

---

## 🧠 Detalhes Técnicos e Otimizações Profundas
Cada linha de código foi pensada para garantir performance e eficiência, demonstrando um domínio aprofundado das tecnologias.

<br>

**Código C/C++ Otimizado (ESP32)**
<br>
No arquivo `sketch.ino` (localizado dentro da pasta `esp32/`), você encontrará o código cuidadosamente otimizado para o ESP32. A otimização de memória foi uma prioridade crucial, garantindo a máxima eficiência em um microcontrolador com recursos limitados.
<p>
 
**Exemplo Prático e Impactante de Otimização de Memória:**
 
```cpp
// Antes: const int SENSOR_UMIDADE_PIN = 34; // Um 'int' padrão pode consumir 4 bytes no ESP32.
// Agora: const uint8_t SENSOR_UMIDADE_PIN = 34; // Um 'uint8_t' utiliza APENAS 1 byte!
```
**Justificativa da otimização:** Para armazenar números de pinos GPIO (que variam de 0 a 255),
```cpp
// o tipo de dado `uint8_t` (inteiro sem sinal de 8 bits) é o mais adequado e incrivelmente econômico.
// Essa escolha estratégica resulta em uma otimização de 3 bytes por variável, uma economia significativa em microcontroladores.
```
```cpp
// Antes: int umidadePercentual = map(valor, 0, 4095, 0, 100); // Usando 'int' para a porcentagem.
// Agora: uint8_t umidadePercentual = map(valor, 0, 4095, 0, 100); // 'uint8_t' para a porcentagem.
```
**Justificativa da otimização:** A porcentagem de umidade varia de forma natural de 0 a 100%.
```cpp
// Este intervalo se encaixa perfeitamente dentro dos limites de um `uint8_t`.
// Esta otimização proporciona mais 3 bytes de economia e garante máxima eficiência e clareza no código.
```
Essas otimizações, embora pareçam pequenas individualmente, somam-se para garantir que o sistema não apenas economize memória, mas também contribua para um código mais robusto, mais rápido e incrivelmente mais eficiente em termos de consumo de recursos.

---

**Banco de Dados Estruturado (SQLite)**

<br>

O coração de dados do FarmTech é o arquivo `farmtech.db`, gerenciado pelo eficiente sistema de banco de dados SQLite. Ele armazena as leituras de forma estruturada e acessível na tabela `leituras_sensores`, com as seguintes colunas essenciais:

`id`: `INTEGER PRIMARY KEY AUTOINCREMENT` - Um identificador único e sequencial, garantindo a integridade e rastreabilidade de cada leitura.

`timestamp`: `TEXT NOT NULL` - Armazena a data e hora exatas da coleta da leitura (no formato legível `YYYY-MM-DD HH:MM:SS`), crucial para análises temporais.

`umidade_percentual`: `INTEGER NOT NULL` - O valor da umidade do solo, já convenientemente convertido para uma porcentagem de 0 a 100.

`status_irrigacao`: `TEXT NOT NULL` - O status de irrigação registrado naquele momento, indicando claramente se foi 'OK' (sem necessidade) ou 'IRRIGAR' (necessário).

Este modelo de dados simples, mas altamente eficiente, fornece a base sólida para todas as análises de Machine Learning e as previsões inteligentes do sistema.

---

**Modelo Preditivo Robusto com Scikit-learn**

<br>

O script `predict_irrigation.py` é a alma inteligente do FarmTech. Ele emprega a poderosa biblioteca `scikit-learn` para treinar um modelo de Árvore de Decisão (`DecisionTreeClassifier`). Este modelo aprende a complexa correlação entre a `umidade_percentual` (nossa principal característica ou "feature") e o `status_irrigacao` (nosso objetivo de previsão ou "target").

Mesmo com um conjunto de dados de exemplo inicialmente pequeno, o modelo demonstra uma impressionante **acurácia de 1.00**, validando a lógica de decisão para os cenários sintéticos simulados. Isso mostra o potencial incrível do FarmTech para escalar e aprender com dados reais no futuro.

---

## 📽️ Demonstração

**Assista ao vídeo de demonstração no YouTube:**  
👉 [Clique aqui para assistir](https://www.youtube.com/watch?v=lnG2PRT62W0)


---

## 💡 Olhando para o Horizonte: Roadmap Estratégico e Evolução Tecnológica do **FarmTech Solutions**

Este protótipo da **Fase 4** estabelece uma fundação robusta, validando a premissa de um sistema preditivo para gestão hídrica. Para solidificar o FarmTech Solutions como uma solução de ponta e escalar sua aplicabilidade no cenário do agronegócio real, delineamos um **roadmap estratégico** focado em aprimoramentos técnicos e integração sistêmica.

---

### 📦 Implantação e Edge Computing com Resiliência Operacional
A transição do **Wokwi** para unidades de sensoriamento e atuação baseadas em **ESP32** de grau industrial exigirá otimização do firmware para *edge computing* e processamento embarcado de baixo consumo, utilizando técnicas como **filtragem Kalman** (redução de ruído de sensor) e **compressão de dados** para telemetria.  
- **Redundância:** múltiplos sensores, fontes híbridas (solar + bateria) com gerenciamento de carga.  
- **Proteção ambiental:** encapsulamento **IP67** visando MTBF elevado em ambientes agrícolas hostis.  
- **Controle local crítico:** desligamento de bomba em excesso de umidade, garantindo operação mesmo sem conectividade.

---

### 🌐 Arquitetura de Comunicação Distribuída e Tolerante a Falhas
Estabeleceremos uma **malha heterogênea** de comunicação:  
- **LoRaWAN** para telemetria de longa distância onde Wi-Fi é inviável.  
- **MQTT sobre TLS** para transmissão de dados securitizada.  
- **Gateway de campo** (Raspberry Pi + Node-RED/Mosquitto) atuando como *store-and-forward*, preservando a integridade temporal da série histórica.  
- **Comandos bidirecionais** via **JSON/Protobuf**, permitindo orquestração remota de múltiplas zonas de irrigação com sincronização de estado distribuída.

---

### 🧠 Machine Learning Híbrido: do Edge ao Cloud com Aprendizado por Reforço
A inteligência preditiva evoluirá para um **modelo híbrido**:  
- **Edge:** modelos quantizados e otimizados (*TinyML*) para inferência em tempo real.  
- **Cloud:** pipeline robusto de **MLOps** para coleta contínua, *feature engineering* avançada (Fourier Transforms) e **retrain** automatizado com **TimeSeriesSplit**.  
- **Reinforcement Learning:** agente aprende a maximizar a eficiência hídrica (recompensas: crescimento da cultura, economia de água) a partir dos estados de umidade, temperatura e histórico de irrigação.

---

### 🔔 Sistema de Alerta Contextual e Ações Proativas Orquestradas
O módulo de notificações torna-se um sistema de **alerta e remediação proativa**:  
- Integração via APIs multicanal (**Webhooks** → ERP/CRM).  
- **Complex Event Processing (CEP)** para detectar padrões anômalos (ex.: queda abrupta de umidade, leituras inconsistentes).  
- **Ações corretivas automatizadas:** auto-irrigação condicionada, alertas instantâneos para equipes de campo – transformando o sistema em agente ativo na mitigação de riscos.

---

### 📊 Plataforma de Business Intelligence Agrícola e Gêmeos Digitais
O **dashboard Streamlit** evoluirá para uma plataforma de **BI agrícola modular**:  
- Integração de dados **geoespaciais (GIS)** para visualizar saúde da cultura e zonas de estresse hídrico.  
- **Gêmeos Digitais (Digital Twins)** para simulação de cenários de irrigação e otimização *what-if* antes da aplicação real.  
- Relatórios personalizáveis com métricas de **ROI hídrico** e projeções de produtividade, consolidando o FarmTech como ferramenta estratégica e financeira indispensável.

---

> Este roadmap delineia não apenas melhorias incrementais, mas uma **visão disruptiva** que posiciona o FarmTech Solutions como catalisador da **Agricultura 4.0**, habilitando decisões *data-driven* e operações autônomas rumo a um futuro agrícola resiliente e altamente produtivo.
