from conexao import conectar
from datetime import date

def cadastrar_cliente():
    conexao = conectar()

    if conexao is None:
        print("Erro na conexão com o banco.")
        return

    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cidade = input("Cidade: ")

    cursor = conexao.cursor()

    
    sql = """
        INSERT INTO clientes (nome, cpf, email, telefone, cidade, data_cadastro)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    dados = (nome, cpf, email, telefone, cidade, date.today())

    cursor.execute(sql, dados)
    conexao.commit()

    cursor.close()
    conexao.close()

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    conexao = conectar()

    if conexao is None:
        print("Erro na conexão com o banco.")
        return

    cursor = conexao.cursor()

    sql = "SELECT id, nome, cpf, email, telefone, cidade, data_cadastro FROM clientes"
    cursor.execute(sql)

    clientes = cursor.fetchall()

    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("\n=== LISTA DE CLIENTES ===")
        for cliente in clientes:
            print(f"""
ID: {cliente[0]}
Nome: {cliente[1]}
CPF: {cliente[2]}
Email: {cliente[3]}
Telefone: {cliente[4]}
Cidade: {cliente[5]}
Data: {cliente[6]}
---------------------------
""")

    cursor.close()
    conexao.close()
