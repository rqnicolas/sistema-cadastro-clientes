# Sistema de Cadastro de Clientes

Este projeto é um sistema simples para cadastrar e listar clientes usando **Python** e **MySQL**.

## Funcionalidades
- Cadastrar clientes
- Listar clientes

## Tecnologias
- Python
- MySQL / MariaDB
- Biblioteca: `mysql-connector-python`

## Estrutura do Projeto

sistema-cadastro-clientes/
│
├─ main.py # Menu e execução do sistema
├─ cliente.py # Funções de cadastro e listagem
├─ conexao.py # Conexão com o banco MySQL
├─ requirements.txt # Bibliotecas necessárias
├─ README.md # Este arquivo
└─ .gitignore # Arquivos ignorados pelo Git

## Como usar
1. Criar o banco `Cadastros_Clientes` no MySQL
2. Criar tabela `clientes` com o seguinte SQL:

# Sistema de Cadastro de Clientes

Este projeto é um sistema simples para cadastrar e listar clientes usando **Python** e **MySQL**.

## Funcionalidades
- Cadastrar clientes
- Listar clientes

## Tecnologias
- Python
- MySQL / MariaDB
- Biblioteca: `mysql-connector-python`

## Estrutura do Projeto

sistema-cadastro-clientes/
│
├─ main.py # Menu e execução do sistema
├─ cliente.py # Funções de cadastro e listagem
├─ conexao.py # Conexão com o banco MySQL
├─ requirements.txt # Bibliotecas necessárias
├─ README.md # Este arquivo
└─ .gitignore # Arquivos ignorados pelo Git

## Como usar
1. Criar o banco `Cadastros_Clientes` no MySQL
2. Criar tabela `clientes` com o seguinte SQL:

```sql
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(14),
    email VARCHAR(100),
    telefone VARCHAR(20),
    cidade VARCHAR(50),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
Ajustar o arquivo conexao.py com seu usuário, senha e nome do banco

Rodar o programa:

python main.py

Ajustar o arquivo conexao.py com seu usuário, senha e nome do banco

Rodar o programa:

python main.py
