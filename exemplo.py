from arquivos import *

def adicionar_tarefa(lista_tarefas, tarefa):
    # lista_tarefas.append(tarefa)
    adicionar_arquivo("tarefas.txt", tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa(lista_tarefas, tarefa):
    if tarefa in lista_tarefas:
        lista_tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' removida com sucesso!")
    else:
        print("Tarefa não encontrada na lista!")

def verificar_tarefas(lista_tarefas):
    if lista_tarefas:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(lista_tarefas, start=1):
            print(f"{i}. {tarefa}")
        input("")
    else:
        print("A lista de tarefas está vazia.")

def menu_opcoes(lista_tarefas):
    while True:
        print("\n===== MENU DE OPÇÕES =====")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Verificar tarefas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tarefa = input("Digite a tarefa a ser adicionada: ")
            adicionar_tarefa(lista_tarefas, tarefa)
        elif opcao == '2':
            tarefa = input("Digite a tarefa a ser removida: ")
            remover_tarefa(lista_tarefas, tarefa)
        elif opcao == '3':
            verificar_tarefas(lista_tarefas)
        elif opcao == '0':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    lista_tarefas = []
    menu_opcoes(lista_tarefas)
