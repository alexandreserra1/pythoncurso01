# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


todo = []
desfeitas = []


def adicionar_tarefa(tarefa):
    todo.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    # Limpa a lista de desfeitas porque uma nova tarefa foi adicionada
    desfeitas.clear()


def desfazer():
    if len(todo) > 0:
        tarefa = todo.pop()  # Remove a última tarefa de 'todo' e armazena em 'tarefa'
        desfeitas.append(tarefa)  # Adiciona a tarefa desfeita à lista 'desfeitas'
        print(f"Tarefa '{tarefa}' desfeita com sucesso!")
    else:
        print("Nenhuma tarefa para desfazer.")


def refazer():
    if len(desfeitas) > 0:
        tarefa = (
            desfeitas.pop()
        )  # Remove a última tarefa de 'desfeitas' e armazena em 'tarefa'

        todo.append(tarefa)  # Adiciona a tarefa refeita de volta à lista 'todo'
        print(f"Tarefa '{tarefa}' refeita com sucesso!")
    else:
        print("Nenhuma tarefa para refazer.")


def listar_tarefas():
    print("Tarefas atuais:", todo)
    print("Tarefas desfeitas:", desfeitas)


while True:
    print()
    print("Comandos disponíveis:")
    print("  1 - Adicionar tarefa")
    print("  2 - Desfazer")
    print("  3 - Refazer")
    print("  4 - Listar tarefas")
    print("  0 - Sair")
    print()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Qual a tarefa? ")
        adicionar_tarefa(tarefa)
    elif opcao == "2":
        desfazer()
    elif opcao == "3":
        refazer()
    elif opcao == "4":
        listar_tarefas()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
        print()

print("Saindo...")
print()
listar_tarefas()
