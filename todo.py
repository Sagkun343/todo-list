from todolibrary import *

file_path = "task.txt"


def tasks():
    flag = True
    mylist = Todolist("My list")
    while flag:
        prompt = (
            input("Hi user. Do you want to [1]add/[2]remove/[3]modify/[4]view/[5]mark a task as complete/[6]exit :"))
        try:
            prompt = int(prompt)
            if prompt < 1 or prompt > 6:
                print("please input a number between 1-6.")
                continue
        except ValueError:
            print("please input a number between 1-6.")
        if prompt == 6:
            with open('task.txt', 'a+')
            print("Thanks for using our application.")
            break
        elif prompt == 1:
            user_task = str(input("Enter the task name:"))
            mylist.add_task(user_task)
            print(f"task {user_task} added successfully.")
            continue
        elif prompt == 2:
            if mylist.check_empty():
                print("List items cant be removed when list is already empty.")
            else:
                user_index = int(input(f"Enter the number of task you want removed: \n{mylist.show_tasks()}"))
                task = mylist.remove_task(user_index - 1)
                print(f"task {user_index} removed successfully.")
                continue
        elif prompt == 3:
            user_index = int(input(f"Enter the number of task you want modified: \n{mylist.show_tasks()}"))
            user_modified_task = str(input("Enter the modified task :"))
            mylist.modify_task(user_index - 1, user_modified_task)
            print(f"task {user_index} modified successfully.")
        elif prompt == 4:
            print(mylist.show_tasks())
            continue
        elif prompt == 5:
            user_index = int(input(f"Enter the number of task you want completed: \n{mylist.show_tasks()}"))
            mylist.complete_task(user_index - 1)
            print(f"task {user_index} completed successfully.")


if __name__ == "__main__":
    tasks()
