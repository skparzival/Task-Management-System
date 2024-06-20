'''Task Management System'''

import json, datetime

#Class Task to create tasks
class Task:
    #Initializing values of tasks
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    #Returning the tasks and data as string
    def __str__(self):
        return f"Title: {self.title} \t Description: {self.description} \t Due Date: {self.due_date} \t Status: {self.status}"

#Class TaskManager to do task management functions
class TaskManager:
    #Initializing list of tasks
    def __init__(self):
        self.tasks = []

    #Add new tasks to the list
    def add_task(self, task):
        self.tasks.append(task)

    #View all the tasks in the list
    def view_tasks(self):
        for task in self.tasks:
            print(task)

    #Update task details
    def update_task(self, task_id, **kwargs):
        try:
            task = self.tasks[task_id]
            for key, value in kwargs.items():
                setattr(task, key, value)
        except IndexError:
            print("Invalid task ID.")

    #Delete task from the list
    def delete_task(self, task_id):
        try:
            del self.tasks[task_id]
        except IndexError:
            print("Invalid task ID.")

    #Save the tasks in the list to a file
    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [vars(task) for task in self.tasks]
            json.dump(tasks_data, file)
        self.tasks=[]

    #Load all the tasks in the file to the list 
    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                for data in tasks_data:
                    task = Task(**data)
                    self.add_task(task)
        except FileNotFoundError:
            print("File not found.")

#Main function
def main():
    #Creating the object of class TaskManager
    task_manager = TaskManager()

    while True:
        #Task Management page
        print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("\n\tTask Management System\n")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save Tasks to File")
        print("6. Load Tasks from File")
        print("7. Exit\n")

        choice = input("Enter your choice: ")
        
        #Task management function according to the user's choice
        if choice == "1":
            try:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                date_str = input("Enter due date (DD-MM-YYYY): ")
                due_date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
                status = input("Enter task status: ")
                task = Task(title, description, due_date, status)
                task_manager.add_task(task)
            except ValueError as e:
                print(e)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            attr = input("Enter attribute to update (title/description/due_date/status): ")
            new_value = input(f"Enter new value for {attr}: ")
            task_manager.update_task(task_id-1, **{attr: new_value})
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id-1)
        elif choice == "5":
            filename = input("Enter filename to save tasks: ")
            task_manager.save_tasks(filename)
        elif choice == "6":
            filename = input("Enter filename to load tasks: ")
            task_manager.load_tasks(filename)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
