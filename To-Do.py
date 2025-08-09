# Pickle Time!!!! 
import pickle
import os

# Create a Class for To-Do List Functions
class ToDoList:
    '''Class to handle to-do list functions'''

    def __init__(self, filename="tasks.pkl"):
        # Initialize a Blank List for Storing Tasks
        self.filename = filename
        self.tasks = self.load_tasks()

# Load tasks from file (if it exists)
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "rb") as f:
                    return pickle.load(f)
            except (pickle.UnpicklingError, EOFError):
                print("Task file corrupted. Starting over")
        return []

# Save tasks to file
    def save_tasks(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.tasks, f)

# Display Menu to User
    def display_menu(self):
        '''Display options to user'''
        print("\n1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")

# Add Task
    def add_task(self):
        '''Add a new task'''
        task = input("Enter task: ")
        self.tasks.append(task)
        print("Task added")
        self.save_tasks()
        self.display_tasks()

# Edit Task
    def edit_task(self):
        '''Edit existing task'''
        if self.tasks:
            self.display_tasks()
            try:
                task_index = int(input("Enter task index to edit: ")) - 1
                if 0 <= task_index < len(self.tasks):
                    new_task = input("Enter new task: ")
                    self.tasks[task_index] = new_task
                    print("Task edited")
                    self.save_tasks()
                    self.display_tasks()
                else:
                    print("Invalid")
            except ValueError:
                print("Please enter a valid number")
        else:
            print("No tasks to edit")

# Delete Task
    def delete_task(self):
        '''Delete task'''
        if self.tasks:
            self.display_tasks()
            try:
                task_index = int(input("Enter task index to delete: ")) - 1
                if 0 <= task_index < len(self.tasks):
                    self.tasks.pop(task_index)
                    print("Task deleted")
                    self.save_tasks()
                    self.display_tasks()
                else:
                    print("Invalid")
            except ValueError:
                print("Please enter a valid number")
        else:
            print("No tasks to delete")

    def display_tasks(self):
        '''Display all tasks with their indices'''
        if not self.tasks:
            print("No tasks yet")
        else:
            print("\nTo-Do List: ")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

    def run(self):
        '''Run the application'''
        while True:
            self.display_menu()
            choice = input("Select an option: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.edit_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.display_tasks()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid")

# Create an Instance
todo_list = ToDoList()
todo_list.run()

            