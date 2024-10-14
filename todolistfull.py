import os

# File to store tasks
TODO_FILE = "todo_list.txt"

# Function to load tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to add a task
def add_task(tasks):
    new_task = input("Enter the new task: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task '{new_task}' added successfully!")
    else:
        print("Task cannot be empty!")

# Function to update a task
def update_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to update: "))
            if 1 <= task_number <= len(tasks):
                updated_task = input("Enter the updated task: ").strip()
                if updated_task:
                    tasks[task_number - 1] = updated_task
                    save_tasks(tasks)
                    print(f"Task {task_number} updated to '{updated_task}'!")
                else:
                    print("Task cannot be empty!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to clear all tasks
def clear_all_tasks(tasks):
    confirm = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
    if confirm == "yes":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared successfully!")
    else:
        print("Operation canceled.")

# Main menu display
def show_menu():
    print("\nTo-Do List Manager")
    print("-------------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Clear All Tasks")
    print("6. Exit")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            clear_all_tasks(tasks)
        elif choice == "6":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.")

# Entry point
if __name__ == "__main__":
    main()
