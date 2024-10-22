import os
import sys
import time

FILE_PATH = "tasks.txt"

def load_tasks():
    """Loads all tasks from the file"""
    tasks = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            for line in file:
                tasks.append(line.strip())
        return tasks
    
def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks(tasks):
    '''View tasks currently in a list'''

    if not tasks:
        print("Empty list")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
            
def add_tasks(tasks):
    """Add new task to the list"""
    print(f"{'ADD NEW TASKS':*^30}")
    print(f"{'press Q to go back':^30}\n")

    while True:
        new_task = input("Task name: ").title()
        if new_task == 'Q':
            break
        else:
            tasks.append(new_task)
    clear_screen()

def remove_tasks(tasks):
    '''Allow user to remove any listed task from the list'''
    print(f"{'REMOVE TASKS':*^30}\n")
    view_tasks(tasks)

    try:
        if not tasks:
            pause_and_reutrn()
        else:
            task_num = int(input("\nEnter task number to remove: "))
            tasks.pop(task_num - 1)
            print(f"Task {task_num} removed succefully")
    except (ValueError, IndexError):
        print("Invalid task number")

    clear_screen()

def mark_task_completed(tasks):
    """Allow user to mark task as completed."""
    print(f"{'MARK COMPLETED TASKS':*^30}\n")
    view_tasks(tasks)

    try:
        if not tasks:
            pause_and_reutrn()
        else:
            task_num = int(input("\nEnter task number to mark as Completed: "))
            tasks[task_num - 1] += F"{'[COMPLETED]':>20}"
            print(f"\nTask {task_num} marked as completed..")
    except (ValueError, IndexError):
        print("Invalid task number")
    clear_screen()

def exit_app(tasks):
    '''Allow user to exit the application.'''
    clear_screen()
    print("Saving tasks...")
    save_tasks(tasks)
    time.sleep(1)
    clear_screen()
    print("Goodbye...")
    time.sleep(0.5)
    quit()

def show_menu():
    """Show main menu"""
    print("1. View tasks.")
    print("2. Add Tasks.")
    print("3. Remove Tasks.")
    print("4. Mark Task as completed.")
    print("5. Exit")

def pause_and_reutrn():
    """wait user to press enter to return to home screen"""
    input("\nPress Enter to main menu..")
    clear_screen()

def clear_screen():
    """Use ANSI character codes to clear terminal screen"""
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()


def main():
    clear_screen()
    tasks = load_tasks()

    while True:
        show_menu()
        try:
            choice = int(input("\nSelect a choice: "))
            
            if choice == 1:
                clear_screen()
                view_tasks(tasks)
                pause_and_reutrn()
            elif choice == 2:
                clear_screen()
                add_tasks(tasks)
            elif choice == 3:
                clear_screen()
                remove_tasks(tasks)
            elif choice == 4:
                clear_screen()
                mark_task_completed(tasks)
            elif choice == 5:
                exit_app(tasks)
            else:
                clear_screen()
                print("Invalid option!, Enter a number")
                time.sleep(2)
                clear_screen()
        except (ValueError):
            clear_screen()
            print("Invalid Value, Please Enter a number..")
            time.sleep(2)
            clear_screen()

if __name__ == '__main__':
    main()