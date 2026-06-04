clientes = []

while True:
    print("\n==============================")
    print(" SISTEMA DE CADASTRO")
    print("==============================")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Excluir cliente")
    print("5 - Quantidade de clientes")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        clientes.append(nome)
        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        print("\n=== CLIENTES CADASTRADOS ===")

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for i, cliente in enumerate(clientes, start=1):
                print(f"{i} - {cliente}")

    elif opcao == "3":
        busca = input("Digite o nome do cliente: ")

        if busca in clientes:
            print("Cliente encontrado!")
        else:
            print("Cliente não encontrado!")

    elif opcao == "4":
        excluir = input("Digite o nome do cliente para excluir: ")

        if excluir in clientes:
            clientes.remove(excluir)
            print("Cliente removido com sucesso!")
        else:
            print("Cliente não encontrado!")

    elif opcao == "5":
        print("Total de clientes cadastrados:", len(clientes))

    elif opcao == "6":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")