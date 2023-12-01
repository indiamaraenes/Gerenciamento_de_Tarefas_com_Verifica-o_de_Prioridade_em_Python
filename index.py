#inicialização do constructor para a classe Task
class Task:
    # O método __init__ é o construtor da classe Task
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority







# Abaixo está o controlador das tarefas, para funções de cadastrar tarefas e ver tarefas
class TaskController:
    # Lista/array para armazenar as tarefas
    tasks = []

    #Função para cadastro de tarefas na lista de tarefas
    @classmethod
    def add_task(cls, task):
        cls.tasks.append(task)

    # Função para visualizar as tarefas, depois de já cadastradas
    @classmethod
    def view_tasks(cls):
        # Aqui é criado uma nova lista, ordenando as tarefas por prioridade
        sorted_tasks = sorted(enumerate(cls.tasks), key=lambda x: x[1].priority, reverse=True)
        # Aqui iteramos sobre sorted_tasks, pegando o index e as tarefas, para exibir na tela as tarefas,
        #e seus respectivos numeros de index.
        for index, task in sorted_tasks:
            print(f"Descrição: {task.description}, Data de Vencimento: {task.due_date}, Prioridade: {task.priority}, INDICE DA TAREFA: {index + 1} ")
        
    # Função para atualizar tarefas, depois de já cadastradas
    def update_task(self, index, updated_task):
        adjusted_index = index - 1
        if 0 <= adjusted_index < len(self.tasks):
            self.tasks[adjusted_index] = updated_task
            print("Tarefa atualizada com suceso.")
        else:
            print("Índice inválido")

    # Função/método para excluir tarefas, depois de ja cadastradas        
    @classmethod
    def deleted_task(cls,index):
        adjusted_index = index - 1
        if 0 <= adjusted_index < len(cls.tasks):
            deleted_task = cls.tasks.pop(adjusted_index)
            print(f"Tarefa excluida: {deleted_task.description}")
        else:
            print("Índice inválido.")












# Abaixo é uma interface, um menu para criação das tarefas e prioridades
class ConsoleUI:
    # Método estático para obter entrada do usuário e criar uma nova tarefa
    @staticmethod
    def get_task_input():
        description = input("Digite a descrição da tarefa: ")
        due_date = input("Digite a Data: ")
        priority = int(input("Digite a Prioridade (de 1 a 5): "))
        return Task(description, due_date, priority)


# Abaixo está uma Função para validar a prioridade
def validate_priority(priority):
    # Retorna True se a prioridade estiver no intervalo de 1 a 5, caso contrário, retorna False
    return 1 <= priority <= 5














# Aqui é a inicialização principal do programa
def main():
    while True:
        # Exibe as opções do menu
        print("\n1. Adicionar tarefa\n2. Ver tarefas\n3. Atualizar tarefa\n4. Excluir tarefa\n5. Sair")
        # Obtém a escolha do usuário
        choice = input("Digite sua Escolha: ")

        if choice == "1":
            # Obtém informações da tarefa a ser adicionada
            task = ConsoleUI.get_task_input()
            # Verifica se a prioridade é válida antes de adicionar a tarefa
            if validate_priority(task.priority):
                TaskController.add_task(task)
            else:
                print("Priorização inválida, você deve escolher algo entre 1 e 5.")
        elif choice == "2":
            # Exibe todas as tarefas cadastradas
            TaskController.view_tasks()
        elif choice == "3":
            # Atualizar uma tarefa
            index = int(input("Digite o índice da tarefa a ser atualizada: "))
            updated_task = ConsoleUI.get_task_input()
            # if validate_priority(updated_task.priority):
            TaskController().update_task(index, updated_task)
            # print("Priorização inválida, você deve escolher algo entre 1 e 5.")
        elif choice == "4":
            #Excluir tarefa
            index = int(input("Digite o índice da tarefa a ser excluída: "))
            TaskController.deleted_task(index)
        elif choice == "5":
        # Encerra o loop e sai do programa
            break
        else:
            print("Escolha inválida. Tente Novamente.")
        
      


# Verifica se este script está sendo executado como o programa principal
if __name__ == "__main__":

# Chama a função principal (main) para iniciar o programa
    main()
