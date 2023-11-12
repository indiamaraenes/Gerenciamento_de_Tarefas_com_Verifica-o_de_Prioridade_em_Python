# index.py

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority


def validate_priority(priority):
    # Função para validar a prioridade
    return 1 <= priority <= 5


class TaskController:
    tasks = []

    @classmethod
    def add_task(cls, task):
        cls.tasks.append(task)

    @classmethod
    def view_tasks(cls):
        # Função para visualizar as tarefas
        for task in cls.tasks:
            print(f"Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}")

    # Implemente as outras operações do CRUD conforme necessário


class ConsoleUI:
    @staticmethod
    def get_task_input():
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        priority = int(input("Enter priority (1-5): "))
        return Task(description, due_date, priority)


def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = ConsoleUI.get_task_input()
            if validate_priority(task.priority):
                TaskController.add_task(task)
            else:
                print("Invalid priority. Priority must be between 1 and 5.")
        elif choice == "2":
            TaskController.view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
