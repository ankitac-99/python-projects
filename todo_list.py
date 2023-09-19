# Define an empty list to store tasks
tasks = []

# Function to display the main menu
def show_menu():
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Quit")

# Function to add tasks
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

# Function to remove tasks
def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to view tasks
def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
