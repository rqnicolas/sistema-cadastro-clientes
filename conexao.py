import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cadastro_clientes"
        )
        return conexao
    except mysql.connector.Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
        return None
