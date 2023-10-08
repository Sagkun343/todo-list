class Task:
    def __init__(self, statement: str, tickbox: bool = False):
        self.statement = statement
        self.tickbox = tickbox

    def __repr__(self):
        return f"Task: {self.statement}\nCompleted: {self.tickbox}\n"


class Subtask(Task):
    pass


class Todolist:
    def __init__(self, name: str):
        self.task_list = []
        self.name = name

    def add_task(self, taskname: str) -> object:
        task = Task(taskname)
        self.task_list.append(task)
        return None

    def show_tasks(self):
        for index, element in enumerate(self.task_list):
            print(f"{index + 1}.{element}")
        return None

    def remove_task(self, index: int):
        self.task_list.pop(index)
        return None

    def complete_task(self, index: int):
        task = self.task_list[index].tickbox = True
        return None

    def modify_task(self, index: int, new_statement: str):
        task = self.task_list[index]
        task.statement = new_statement
        return f"task {task} modified successfully."

    def check_empty(self) -> bool:
        if len(self.task_list) == 0:
            return True
        else:
            return False
