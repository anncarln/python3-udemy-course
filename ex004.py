def add(todo_list):
    n = int(input("Quantas tarefas você quer adicionar? "))
    for _ in range(n):
        todo_list.append(input("Tarefa: "))


def show_up(todo_list):
    if not todo_list:
        print('Nada para listar. A lista está vazia.')
    else:
        print('Lista de Tarefas: ')
        for assignment in todo_list:
            print(assignment)


def undo(undo_list, todo_list):
    if not todo_list:
        print('Nada a desfazer.')
    else:
        undo_list.append(todo_list[-1])
        todo_list.pop()


def redo(undo_list, todo_list):
    if not undo_list:
        print('Nada a refazer.')
    else:
        todo_list.append(undo_list[-1])
        undo_list.pop()


if __name__ == '__main__':

    list_of_assignments = []
    temporary_undo_list = []

    while True:
        print()
        menu = input("Adicionar tarefas [add]\n"
                     "Listar todas as tarefas [ls]\n"
                     "Desfazer [undo]\n"
                     "Refazer [redo]\n"
                     "Sair [exit]\n"
                     "->  ").lower()
        print()

        if menu == 'add':
            add(list_of_assignments)
        elif menu == 'ls':
            show_up(list_of_assignments)
        elif menu == 'undo':
            undo(temporary_undo_list, list_of_assignments)
        elif menu == 'redo':
            redo(temporary_undo_list, list_of_assignments)
        elif menu == 'exit':
            break
