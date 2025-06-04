# Lista para armazenar os contatos
contatos = []

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Buscar Contato")
    print("4. Visualizar Contatos")
    print("5. Sair")

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contato = {"nome": nome, "telefone": telefone}
    contatos.append(contato)
    print(f"Contato '{nome}' adicionado com sucesso!")

def remover_contato():
    nome = input("Digite o nome do contato a ser removido: ")
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)
            print(f"Contato '{nome}' removido com sucesso!")
            return
    print(f"Contato '{nome}' não encontrado!")

def buscar_contato():
    nome = input("Digite o nome do contato a ser buscado: ")
    for contato in contatos:
        if contato["nome"] == nome:
            print(f"Contato encontrado: Nome: {contato['nome']}, Telefone: {contato['telefone']}")
            return
    print(f"Contato '{nome}' não encontrado!")

def visualizar_contatos():
    if contatos:
        print("\nLista de Contatos:")
        for idx, contato in enumerate(contatos, 1):
            print(f"{idx}. Nome: {contato['nome']}, Telefone: {contato['telefone']}")
    else:
        print("Nenhum contato na lista.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            remover_contato()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            visualizar_contatos()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

# Executar o programa principal
if __name__ == "__main__":
    main()
