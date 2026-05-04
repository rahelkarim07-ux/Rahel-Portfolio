print("Made by Rahel")

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    show_tasks()
    try:
        number = int(input("Enter task number to remove: "))
        removed = tasks.pop(number - 1)
        print(f"Removed: {removed}")
    except:
        print("Invalid number.")

while True:
    print("\nTo-Do App")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice")
