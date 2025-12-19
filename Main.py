from cliente import cadastrar_cliente, listar_clientes

def mostrar_menu():
    print("\n=== SISTEMA DE CADASTRO DE CLIENTES ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Sair")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
