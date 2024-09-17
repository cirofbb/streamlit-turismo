import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

def item1():
    st.title("Objetivo e Motivação")
    st.write("""
        ### Objetivo:
        O objetivo deste dashboard é permitir a análise e visualização de dados a partir de arquivos CSV da sessão de turismo do site Data.Rio.
        Os usuários poderão carregar seus dados, aplicar filtros e selecionar colunas ou linhas para visualização.
        
        *A motivação da escolha dos dados é analisar a variação da taxa de ocupação média anual e mensal dos hotéis no Município do Rio de Janeiro entre 1997-2017 .*
    """)

def item2():
    st.title("Upload de Arquivo CSV")
    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=["csv"])
    if uploaded_file is not None:
        # Carrega o CSV e armazenar no estado da sessão
        df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df  # Armazena o DataFrame no session_state
        st.write("Dados carregados com sucesso!")
        st.dataframe(df)
    else:
        st.warning("Por favor, faça o upload de um arquivo CSV.")

def item3():
    if 'df' in st.session_state:  # Verifica se o DataFrame está no estado da sessão
        df = st.session_state['df']
        st.title("Filtro de Dados e Seleção")
        
        # Selecionar colunas
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Selecione as colunas para visualizar", all_columns, default=all_columns)
        
        # Selecionar linhas
        row_selection = st.radio("Deseja visualizar todas as linhas ou selecionar um intervalo?", ("Todas", "Selecionar intervalo"))

        if row_selection == "Selecionar intervalo":
            start_row = st.number_input("Linha inicial", min_value=0, max_value=len(df)-1, value=0)
            end_row = st.number_input("Linha final", min_value=0, max_value=len(df)-1, value=len(df)-1)
            df_filtered = df[selected_columns].iloc[start_row:end_row]
        else:
            df_filtered = df[selected_columns]

        st.write("Dados filtrados:")
        st.dataframe(df_filtered)
    else:
        st.warning("Por favor, faça o upload de um arquivo CSV no item 2.")

def item4():
    st.title("Serviço de Download de arquivos")
    
    if 'df' in st.session_state:  # Verifica se os dados estão disponíveis
        df_filtered = st.session_state['df_filtered']  # Recupera os dados filtrados armazenados
        
        # Permite que o usuário baixe os dados filtrados
        csv = df_filtered.to_csv(index=False).encode('utf-8')  # Converte o DataFrame filtrado para CSV
        
        st.download_button(
            label="Baixar dados filtrados como CSV",
            data=csv,
            file_name='dados_filtrados.csv',
            mime='text/csv'
        )
    else:
        st.warning("Nenhum dado disponível para download. Por favor, carregue e filtre os dados nos itens anteriores.")

def item5():
    st.title("Barra de Progresso e Spinners")
    
    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        # Exibe o spinner durante o carregamento dos dados
        with st.spinner('Carregando os dados...'):
            time.sleep(1)  # Simula um tempo de carregamento
            df = pd.read_csv(uploaded_file)
            st.session_state['df'] = df
        
        # Exibe a barra de progresso
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)  # Simula o processamento de dados
            progress_bar.progress(percent_complete + 1)
        
        st.success("Dados carregados com sucesso!")
        st.dataframe(df)

def item6():
    st.title("Color Picker")

    # Definindo as cores padrão para fundo e fonte
    if 'bg_color' not in st.session_state:
        st.session_state['bg_color'] = "#ffffff"  # Cor de fundo padrão: branco
    if 'font_color' not in st.session_state:
        st.session_state['font_color'] = "#000000"  # Cor da fonte padrão: preto

    # Color picker para a cor de fundo
    bg_color = st.color_picker("Escolha a cor de fundo", st.session_state['bg_color'])
    st.session_state['bg_color'] = bg_color
    
    # Color picker para a cor da fonte
    font_color = st.color_picker("Escolha a cor das fontes", st.session_state['font_color'])
    st.session_state['font_color'] = font_color

    # Verificação para garantir que a cor de fundo e da fonte não sejam iguais
    if bg_color == font_color:
        st.warning("A cor de fundo e a cor da fonte são iguais. Por favor, escolha cores diferentes para evitar problemas de visualização.")

    # Aplicando o estilo CSS para alterar as cores de fundo e da fonte
    st.markdown(
        f"""
        <style>
        .css-1e2o7p2, .css-1x8jbt0 {{
            background-color: {bg_color} !important;
        }}
        .css-1d391kg, .css-1cpxqw2 {{
            color: {font_color} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("Personalize as cores do painel usando as opções acima.")

# Função para carregar e armazenar em cache os dados CSV
@st.cache_data
def load_csv(file):
    df = pd.read_csv(file)
    return df

def item7():
    st.title("Funcionalidade de Cache")
    
    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        # Carrega os dados usando a função de cache
        df = load_csv(uploaded_file)
        st.session_state['df'] = df

        st.write("Dados carregados com sucesso!")
        st.dataframe(df)

def item8():
    st.title("Session State")
    
    # Inicializa o session_state para filtros e seleções
    if 'filters' not in st.session_state:
        st.session_state['filters'] = {}
    
    if 'selected_columns' not in st.session_state:
        st.session_state['selected_columns'] = []
    
    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        st.session_state['df'] = df

        # Filtros
        st.write("Filtros")
        filter_column = st.selectbox("Selecione a coluna para filtrar", df.columns)
        filter_value = st.text_input("Digite o valor para o filtro", "")
        
        if filter_column and filter_value:
            st.session_state['filters'][filter_column] = filter_value
        else:
            if filter_column in st.session_state['filters']:
                del st.session_state['filters'][filter_column]
        
        # Aplica filtros
        df_filtered = df.copy()
        for column, value in st.session_state['filters'].items():
            df_filtered = df_filtered[df_filtered[column].astype(str).str.contains(value, na=False)]

        # Seleção de colunas
        st.write("Seleção de Colunas")
        columns = df.columns.tolist()
        selected_columns = st.multiselect("Selecione as colunas para exibir", columns, default=st.session_state.get('selected_columns', []))
        st.session_state['selected_columns'] = selected_columns
        
        if selected_columns:
            df_filtered = df_filtered[selected_columns]
        
        st.write("Dados filtrados e selecionados")
        st.dataframe(df_filtered)

        # Mostra filtros aplicados
        st.write("Filtros Aplicados:")
        st.write(st.session_state['filters'])
        st.write("Colunas Selecionadas:")
        st.write(st.session_state['selected_columns'])

def item9():
    st.title("Visualização de dados - Tabelas")

    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=["csv"])

    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        st.session_state['df'] = df

        st.write("Tabela Interativa com Dados")
        
        # Exibe a tabela interativa
        st.dataframe(df, use_container_width=True)

def item10():
    st.title("Visualização de dados - Gráficos simples")

    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=["csv"])

    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        st.session_state['df'] = df
        
        st.write("Escolha o tipo de gráfico para visualizar os dados")

        # Seletor de tipo de gráfico
        chart_type = st.selectbox("Selecione o tipo de gráfico", ["Gráfico de Barras", "Gráfico de Linhas", "Gráfico de Pizza"])

        if chart_type == "Gráfico de Barras":
            st.write("Gráfico de Barras")
            column = st.selectbox("Selecione a coluna para o gráfico de barras", df.columns)
            if column:
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.barplot(x=df.index, y=df[column], ax=ax)
                ax.set_title(f'Gráfico de Barras - {column}')
                st.pyplot(fig)

        elif chart_type == "Gráfico de Linhas":
            st.write("Gráfico de Linhas")
            column = st.selectbox("Selecione a coluna para o gráfico de linhas", df.columns)
            if column:
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.plot(df[column])
                ax.set_title(f'Gráfico de Linhas - {column}')
                st.pyplot(fig)

        elif chart_type == "Gráfico de Pizza":
            st.write("Gráfico de Pizza")
            column = st.selectbox("Selecione a coluna para o gráfico de pizza", df.columns)
            if column:
                fig, ax = plt.subplots(figsize=(7, 7))
                df[column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
                ax.set_title(f'Gráfico de Pizza - {column}')
                st.pyplot(fig)

def item11():
    st.title("Visualização de dados - Gráficos avançados")

    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=["csv"])

    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        st.session_state['df'] = df
        
        st.write("Escolha o tipo de gráfico avançado para visualizar os dados")

        # Seletor de tipo de gráfico
        chart_type = st.selectbox("Selecione o tipo de gráfico avançado", ["Histograma", "Gráfico de Dispersão"])

        if chart_type == "Histograma":
            st.write("Histograma")
            column = st.selectbox("Selecione a coluna para o histograma", df.columns)
            if column:
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.hist(df[column].dropna(), bins=30, edgecolor='black')
                ax.set_title(f'Histograma - {column}')
                ax.set_xlabel(column)
                ax.set_ylabel('Frequência')
                st.pyplot(fig)

        elif chart_type == "Gráfico de Dispersão":
            st.write("Gráfico de Dispersão")
            x_col = st.selectbox("Selecione a coluna para o eixo X", df.columns)
            y_col = st.selectbox("Selecione a coluna para o eixo Y", df.columns)
            if x_col and y_col:
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.scatter(df[x_col], df[y_col], alpha=0.7)
                ax.set_title(f'Gráfico de Dispersão - {x_col} vs {y_col}')
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                st.pyplot(fig)

def item12():
    st.title("Métricas básicas")

    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=["csv"])

    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        st.session_state['df'] = df

        st.write("Resumo das Métricas Básicas dos Dados")

        # Contagem de registros
        num_records = df.shape[0]
        st.metric(label="Número de Registros", value=num_records)

        # Médias
        st.write("Médias das Colunas Numéricas")
        means = df.mean(numeric_only=True)
        for column, mean in means.items():
            st.metric(label=f"Média de {column}", value=f"{mean:.2f}")

        # Somatórios
        st.write("Somatórios das Colunas Numéricas")
        sums = df.sum(numeric_only=True)
        for column, total in sums.items():
            st.metric(label=f"Soma de {column}", value=f"{total:.2f}")

# Dicionário para associar os itens a funções
menu_itens = {
    "1. Objetivo e Motivação": item1,
    "2. Upload de Arquivo CSV": item2,
    "3. Filtro de Dados e Seleção": item3,
    "4. Serviço de Download de arquivos": item4,
    "5. Barra de Progresso e Spinners": item5,
    "6. Color Picker": item6,
    "7. Funcionalidade de Cache": item7,
    "8. Session State": item8,
    "9. Visualização de dados - Tabelas": item9,
    "10. Visualização de dados - Gráficos simples": item10,
    "11. Visualização de dados - Gráficos avançados": item11,
    "12. Métricas básicas": item12
}

# Menu lateral
st.sidebar.title("Menu de Itens")
item_escolhido = st.sidebar.selectbox("Escolha um item", list(menu_itens.keys()))

# Executa a função correspondente ao item escolhido
if item_escolhido in ["2. Realizar Upload de Arquivo CSV", "3. Filtro de Dados e Seleção"]:
    menu_itens[item_escolhido]()
else:
    menu_itens[item_escolhido]()

