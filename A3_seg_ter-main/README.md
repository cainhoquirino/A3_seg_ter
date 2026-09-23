# 📊 IBM HR Analytics: Atrito de Empregados e Performance

## 📝 Sobre o Projeto
Este projeto tem como objetivo analisar os dados de Recursos Humanos da IBM para entender os principais fatores que influenciam o **atrito de empregados (turnover)** e a **performance** da equipe. Para trazer mais contexto ao cenário real, o projeto enriquece a análise interna cruzando as informações com dados do mercado de trabalho brasileiro, permitindo comparações precisas de cargos, salários e custos.

## 🗂️ Fontes de Dados
O projeto utiliza uma combinação estruturada de dados do Kaggle e dados públicos do governo:
- **Base de Dados IBM HR Analytics:** Dados originais focados em métricas de RH, retenção de talentos e avaliação de performance (extraídos via Kaggle).
- **API do IBGE:** Consumo de dados públicos abertos para extrair o panorama do mercado de trabalho no Brasil.
- **Tabelas de Ranking - CUSTO DO TRABALHO:** Utilizadas para analisar o impacto financeiro, tributário e o custo real dos profissionais.
- **Tabelas de Ranking - SALÁRIO:** Base de comparação entre a remuneração do dataset da IBM e a média praticada no mercado brasileiro.

## 🛠️ Tecnologias e Ferramentas Utilizadas
Até o momento, a base do pipeline de dados foi construída com:
- **Python** 🐍 (Linguagem principal)
- **Pandas** 🐼 (Limpeza, estruturação e manipulação avançada dos dados)
- **Kaggle API/Platform** (Fonte primária de extração dos dados da IBM)

## 🚀 Status do Projeto
- [x] **Extração de Dados:** Coleta do dataset do Kaggle e requisições na API do IBGE.
- [x] **Tratamento de Dados (ETL):** Limpeza de inconsistências, padronização de tipos de dados, tratamento de valores nulos e cruzamento das bases com Pandas.
- [ ] **Construção de sistema de Autenticação e Hierarquia:** Sistema para que o usuario possa logar e haja distinção entre os cargos do que cada um pode ver e fazer 
- [ ] **Visualização de Dados:** Construção de gráficos e dashboards para facilitar a tomada de decisão em RH.


## ⚙️ Como Executar o Projeto
1. Clone este repositório em sua máquina local:
   ```bash
   git clone gh repo clone cainhoquirino/A3_seg_ter
   ```
2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas requests kaggle
   ```

## 🤝 Autores
- **Andressa, Bruno, Caio, Pedro Henrique e Pedro Guedes** - Extração, tratamento e análise de dados.
