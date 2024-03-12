import psycopg2
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

def conexao_db(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    try:
        con = psycopg2.connect(
            dbname=os.getenv('DBNAME'),
            user=os.getenv('DBUSER'),
            password=os.getenv('DBPASSWORD'),
            host=os.getenv('DBHOST'),
            port=os.getenv('DBPORT')
        )
        cur = con.cursor()
        
        cur.execute("""
            INSERT INTO pesquisa (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10))
        
        con.commit()
        cur.close()
        con.close()
        st.success('Respostas salvas com sucesso!!!')
        
    except Exception as e:
        st.error(f"Ocorreu um erro ao conectar ao banco de dados: {e}")

