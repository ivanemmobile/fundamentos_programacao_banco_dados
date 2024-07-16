# Lista para armazenar as tarefas
tarefas = []

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Visualizar Tarefas")
    print("4. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefas():
    tarefa = input("Digite a tarefa a ser removida: ")
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' removida com sucesso!")
    else:
        print(f"Tarefa '{tarefa}' não encontrada!")

def visualizar_tarefas():
    if tarefas:
        print("\nLista de Tarefas:")
        for idx, tarefa in enumerate(tarefas, 1):
            print(f"{idx}. {tarefa}")
    else:
        print("Nenhuma tarefa na lista.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            remover_tarefas()
        elif opcao == "3":
            visualizar_tarefas()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

# Executar o programa principal
if __name__ == "__main__":
    main()
