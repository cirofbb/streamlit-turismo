# streamlit-turismo
### Dashboard de Análise de Dados de Turismo
Este projeto é um dashboard interativo desenvolvido em Streamlit para análise e visualização de dados de turismo, com foco na taxa de ocupação hoteleira no Rio de Janeiro entre 1997-2017.

### Visão Geral
O dashboard oferece 12 funcionalidades distintas organizadas em um menu lateral, permitindo desde o carregamento de dados até análises avançadas com visualizações gráficas.

## Funcionalidades Principais
1. Objetivo e Motivação
- Explicação do propósito do dashboard

- Foco na análise da taxa de ocupação hoteleira no Rio de Janeiro (1997-2017)

2. Upload de Arquivo CSV
- Carregamento de arquivos CSV

- Visualização inicial dos dados

3. Filtro de Dados e Seleção
- Seleção de colunas específicas

- Filtragem por intervalo de linhas

- Visualização de dados filtrados

4. Serviço de Download
- Exportação dos dados filtrados em formato CSV

5. Barra de Progresso e Spinners
- Feedback visual durante o carregamento de dados

- Barra de progresso animada

6. Color Picker
- Personalização das cores do painel

- Seleção de cor de fundo e fonte

7. Funcionalidade de Cache
- Otimização de performance com cache de dados

- Carregamento mais rápido em acessos subsequentes

8. Session State
- Manutenção do estado da aplicação

- Armazenamento de filtros e seleções entre interações

9-11. Visualização de Dados
- Tabelas interativas

Gráficos simples:

- Barras

- Linhas

- Pizza

Gráficos avançados:

- Histogramas

- Dispersão

12. Métricas Básicas
- Estatísticas descritivas

- Contagem de registros

- Médias e somatórios

### Como Executar
Certifique-se de ter Python instalado (versão 3.7 ou superior)

Instale as dependências:

pip install streamlit pandas matplotlib seaborn

Execute o aplicativo:

streamlit run TP3.1.py

### Estrutura do Projeto
```

.
├── TP3.1.py                       # Aplicativo principal Streamlit
└── README.md                      # Este arquivo
└── ocupação_média.csv             # Base de dados
└── requirements.txt

```
### Dependências
- Python 3.7+

- streamlit

- pandas

- matplotlib

- seaborn

### Dados Recomendados
O dashboard foi desenvolvido para analisar dados de:

- Taxa de ocupação hoteleira

- Dados de turismo do Rio de Janeiro

- Período: 1997-2017

### Personalização
O painel permite:

- Alteração de cores (fundo e texto)

- Seleção de tipos de gráficos

- Filtragem personalizada dos dados

- Exportação dos resultados

### Observações
Todos os filtros e seleções são mantidos durante a navegação (Session State)

Os dados carregados são cacheados para melhor performance

Interface totalmente responsiva e interativa
