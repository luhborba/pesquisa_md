import streamlit as st
from conect import conexao_db

def main():
    st.set_page_config('Pesquisa Teste',page_icon='🔎',layout='wide')
    st.title('Bem vindo a Pesquisa Teste')

    # Cria uma variável de sessão para armazenar o estado do questionário
    st.write('Olá! Esta pesquisa visa identificar o nível de maturidade de dados da sua empresa. As respostas serão utilizadas para avaliar a maturidade da sua organização em relação à governança, cultura, qualidade e uso de dados. A pesquisa é composta por 20 perguntas, divididas em 5 seções:')

    st.markdown('---')
    st.subheader('Seção 1 - Governança de Dados (5 Perguntas)')
    p1 = st.radio('1. A sua empresa possui um programa formal de governança de dados?', ['Sim', 'Nao','Em Desenvolvimento'])
    p2 = st.radio('2. A sua empresa possui um conselho de governança de dados?', ['Sim', 'Nao','Em Desenvolvimento'])
    p3 = st.radio('3. A sua empresa possui um diretor de dados (CDO)?', ['Sim', 'Nao','Em Desenvolvimento'])
    p4 = st.radio('4. A sua empresa possui políticas e procedimentos documentados para gerenciar seus dados?', ['Sim', 'Nao','Em Desenvolvimento'])
    p5 = st.radio('5. A sua empresa possui um processo para avaliar a qualidade dos seus dados?', ['Sim', 'Nao','Em Desenvolvimento'])
    
    st.markdown('---')
    st.subheader('Seção 2 - Cultura de Dados (5 Perguntas)')
    p6 = st.radio('6. A sua empresa possui uma cultura que valoriza o uso de dados para tomar decisões?', ['Sim', 'Nao','Parcialmente'])
    p7 = st.radio('7. Os funcionários da sua empresa são treinados para usar dados de forma eficaz?', ['Sim', 'Nao','Parcialmente'])
    p8 = st.radio('8. A sua empresa possui um processo para incentivar o compartilhamento de dados entre diferentes departamentos?', ['Sim', 'Nao','Parcialmente'])
    p9 = st.radio('9. A sua empresa possui um processo para identificar e corrigir vieses nos dados?', ['Sim', 'Nao','Parcialmente'])
    p10 = st.radio('10.	A sua empresa possui um processo para garantir a privacidade e segurança dos dados?', ['Sim', 'Nao','Parcialmente'])
    
    # Se o botão "Enviar" for clicado
    if st.button("Enviar"):
        # Envia os dados para o banco de dados
        conexao_db(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)


if __name__ == "__main__":
    main()