tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the list.")

def show_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

while True:
    print("\n1. Add Task\n2. Remove Task\n3. Show Tasks\n4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
