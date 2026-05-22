import os 

def add_task():
    task = input("Enter new task: ")

    with open("tasks.text", "a") as file:
        file.write(task + "\n")

    print("Task added successfully\n")

def view_tasks():
    if not os.path.exists("tasks.text"):
        print("No tasks found.\n")
        return
    
    with open("tasks.text", "r") as file:
        tasks = file.readlines()

    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        print("\n Your tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def delete_task():
    with open("tasks.text", "r") as file:
        tasks = file.readlines()

    view_tasks()

    task_num = int(input("\n Enter task number to delete: "))

    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)

        with open("tasks.text", "w") as file:
            file.writelines(tasks)

            print("Tasks deleted successfully\n")
    else:
         print("Invalid tasks number\n")

def main():
    while True:
        print("\n---TO DO LIST---")
        print("1.Add tasks")
        print("2.View tasks")
        print("3.Deleted tasks")
        print("4.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("Exiting program")
            break

        else:
            print("Invalid choice.Try again.")

main()
