

def display_menu():

    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task add successfully!")

def view_task(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    view_task(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Task '{tasks[index]}' deleted.")
            del tasks[index]
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Please enter a valid number!")

def main():
    print("Welcome to the To-Do List App!")
    tasks = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))   
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_task(tasks)
            elif choice == 3:
                pass
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Thank you for using the To-Do List App!")
                break
            else:
                print("Invalid input! Please choose a number between 1 through 5!")
        except ValueError:
            print("Input error! Please choose a valid number between 1 through 5!")

main()





















































































































































































































