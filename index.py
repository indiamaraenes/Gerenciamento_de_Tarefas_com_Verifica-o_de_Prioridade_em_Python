#
class Task:
    # O método __init__ é o construtor da classe Task
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

# Abaixo está uma Função para validar a prioridade
def validate_priority(priority):
    return 1 <= priority <= 5


# Abaixo está o controlador das tarefas, para funções de cadastrar tarefas e ver tarefas
class TaskController:
    # Lista/array para armazenar as tarefas
    tasks = []
    #Função/método para cadastro de tarefas na lista de tarefas
    @classmethod
    def add_task(cls, task):
        cls.tasks.append(task)

    @classmethod
     # Função/método para visualizar as tarefas, depois de já cadastradas
    def view_tasks(cls):
        sorted_tasks = sorted(cls.tasks, key=lambda x: x.priority, reverse=True)
        for task in sorted_tasks:
            print(f"Descrição: {task.description}, Data de Vencimento: {task.due_date}, Prioridade: {task.priority}")

    @classmethod
    # Função/método para atualizar tarefas, depois de já cadastradas
    def update_task(cls, priority_index, new_task):
        sorted_tasks = sorted(cls.tasks, key=lambda x: x.priority, reverse=True)
        original_index = None
        for index, task in enumerate(cls.tasks):
            original_index = index
            break
        if original_index is not None:
            cls.tasks[original_index] = new_task
            print("Tarefa atualizada com sucesso.")
        else:
            print("Índice inválido.")
            
    @classmethod
    def delete_task(cls, priority_index):
        sorted_tasks = sorted(cls.tasks, key=lambda x: x.priority, reverse=True)
        if 0 <= priority_index < len(sorted_tasks):
            task_to_delete =sorted_tasks[priority_index]
            cls.tasks.remove(task_to_delete)
            print(f"Tarefa excluida com sucesso: {task_to_delete.description}")
        else:
            print("Índice inválido")

# Abaixo é uma interface, um menu para criação das tarefas e prioridades
class ConsoleUI:
    @staticmethod
    def get_task_input():
        description = input("Digite a descrição da tarefa: ")
        due_date = input("Digite a Data: ")
        priority = int(input("Digite a Prioridade (de 1 a 5): "))
        return Task(description, due_date, priority)

#aqui é a inicialização principal do programa
def main():
    while True:
        print("\n1. Adicionar tarefa\n2. Ver tarefas\n3. Atualizar tarefa\n4. Excluir tarefa\n5. Sair")
        choice = input("Digite sua Escolha: ")

        if choice == "1":
            task = ConsoleUI.get_task_input()
            if validate_priority(task.priority):
                TaskController.add_task(task)
            else:
                print("Priorização inválida, você deve escolher algo entre 1 e 5.")
        elif choice == "2":
            TaskController.view_tasks()
        elif choice == "3":
            index = int(input("Digite o índice da tarefa a ser atualizada: "))
            new_task = ConsoleUI.get_task_input()
            if validate_priority(new_task.priority):
                TaskController.update_task(index, new_task)
            else:
                print("Priorização inválida,você deve escolher algo entre 1 e 5.")
        elif choice == "4":
            index = int(input("Digite o índice da tarefa a ser excluída:"))
            TaskController.delete_task(index) 
        elif choice == "5":
            break
        else:
            print("Escolha inválida. Tente Novamente")

class Task:
    # O método __init__ é o construtor da classe Task
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

# Abaixo está uma Função para validar a prioridade
def validate_priority(priority):
    # Retorna True se a prioridade estiver no intervalo de 1 a 5, caso contrário, retorna False
    return 1 <= priority <= 5

# Abaixo está o controlador das tarefas, para funções de cadastrar tarefas e ver tarefas
class TaskController:
    # Lista para armazenar as tarefas
    tasks = []

    # Método de classe para adicionar uma tarefa à lista de tarefas
    @classmethod
    def add_task(cls, task):
        cls.tasks.append(task)

    # Método de classe para visualizar todas as tarefas
    @classmethod
    def view_tasks(cls):
        # Itera sobre a lista de tarefas e imprime informações sobre cada tarefa
        sorted_tasks = sorted(cls.tasks, key=lambda x: x.priority, reverse=True)
        for task in sorted_tasks:
            print(f"Descrição: {task.description}, Data de Vencimento: {task.due_date}, Prioridade: {task.priority}")
    
    @classmethod
    # Função/método para atualizar tarefas, depois de já cadastradas
    def update_task(cls, priority_index, new_task):
        sorted_tasks = sorted(cls.tasks, key=lambda x: x.priority, reverse=True)
        original_index = None
        for index, task in enumerate(cls.tasks):
            original_index = index
            break
        if original_index is not None:
            cls.tasks[original_index] = new_task
            print("Tarefa atualizada com sucesso.")
        else:
            print("Índice inválido.")
            
    @classmethod
    def delete_task(cls, priority_index):
        sorted_tasks = sorted(cls.tasks, key=lambda x: x.priority, reverse=True)
        if 0 <= priority_index < len(sorted_tasks):
            task_to_delete =sorted_tasks[priority_index]
            cls.tasks.remove(task_to_delete)
            print(f"Tarefa excluida com sucesso: {task_to_delete.description}")
        else:
            print("Índice inválido")
        
# Abaixo é uma interface, um menu para criação das tarefas e prioridades
class ConsoleUI:
    # Método estático para obter entrada do usuário e criar uma nova tarefa
    @staticmethod
    def get_task_input():
        description = input("Digite a descrição da tarefa: ")
        due_date = input("Digite a Data: ")
        priority = int(input("Digite a Prioridade (de 1 a 5): "))
        return Task(description, due_date, priority)

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
            new_task = ConsoleUI.get_task_input()
            if validate_priority(new_task.priority):
                TaskController.update_task(index, new_task)
            else:
                print("Priorização inválida, você deve escolher algo entre 1 e 5.")
        elif choice == "4":
            #Excluir tarefa
            index = int(input("Digite o índice da tarefa a ser excluída: "))
            TaskController.delete_task(index)
        elif choice == "5":
        # Encerra o loop e sai do programa
            break
        else:
            print("Escolha inválida. Tente Novamente.")
        
      

# Verifica se este script está sendo executado como o programa principal
if __name__ == "__main__":
    main()
     # Chama a função principal (main) para iniciar o programa
