import os

# Function to load tasks from the file
def load_tasks():
    if not os.path.exists('tasks.txt'):
        return []
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]


# Function to save tasks to the file
def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')


# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

# Function to update a task
def update_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_num] = new_task
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")


# Main function
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
