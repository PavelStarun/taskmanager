class Task():
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Не выполнено"

    def task_status(self):
        self.status = "Выполнено"

    def __str__(self):
        return f"{self.deadline}  |  {self.description}  |  {self.status}"

def print_tasks(tasks):
    print("№ |  Дедлайн  |  Описание задачи  |  Статус")
    for i, task in enumerate(tasks):
        print(f"{i + 1} | {task}")

tasks = []

while True:
    description = input("Введите задачу или 'стоп' для завершения: ")
    if description.lower() == 'стоп':
        break
    deadline = input("Введите дедлайн задачи: ")
    tasks.append(Task(description, deadline))

print_tasks(tasks)

while True:
    mark_done = input("Введите номер задачи, чтобы отметить ее как выполненную, 'стоп' для завершения, или 'добавить' для добавления задачи в список: ")
    if mark_done.lower() == 'стоп':
        break
    elif mark_done.lower() == 'добавить':
        description = input("Введите новую задачу: ")
        deadline = input("Введите дедлайн новой задачи: ")
        tasks.append(Task(description, deadline))
        print_tasks(tasks)
    elif mark_done.isdigit() and 1 <= int(mark_done) <= len(tasks):
        tasks[int(mark_done) - 1].task_status()
        print_tasks(tasks)
    else:
        print("Пожалуйста, введите корректный номер задачи, 'добавить', или 'стоп'.")
