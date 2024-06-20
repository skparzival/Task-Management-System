Task Management System Documentation

Overview
The Task Management System is a console-based application designed to help users manage their tasks efficiently. It allows users to add, view, update, delete, save, and load tasks. The system is implemented using two primary classes, `Task` and `TaskManager`, and includes a `main` function to provide an interactive user interface.

Classes and Methods

1. Task Class
    - Purpose: Represents a single task with a title, description, due date, and status.
    - Attributes:
        - `title` (str): The title of the task.
        - `description` (str): A brief description of the task.
        - `due_date` (str): The due date of the task in DD-MM-YYYY format.
        - `status` (str): The current status of the task.
    - Methods:
        - `__init__(self, title, description, due_date, status)`: Initializes a new task with the given attributes.
        - `__str__(self)`: Returns a string representation of the task, formatted for easy viewing.

2. TaskManager Class
    - Purpose: Manages a list of tasks, providing methods to perform various operations on the tasks.
    - Attributes:
        - `tasks` (list): A list to store the task objects.
    - Methods:
        - `__init__(self)`: Initializes the TaskManager with an empty task list.
        - `add_task(self, task)`: Adds a new task to the task list.
        - `view_tasks(self)`: Prints all the tasks in the task list.
        - `update_task(self, task_id, **kwargs)`: Updates the attributes of a task specified by its ID.
        - `delete_task(self, task_id)`: Deletes a task from the task list based on its ID.
        - `save_tasks(self, filename)`: Saves all tasks to a specified file in JSON format and clears the task list.
        - `load_tasks(self, filename)`: Loads tasks from a specified file and adds them to the task list.

Main Function
The `main` function provides a command-line interface for users to interact with the Task Management System. It displays a menu with options and performs actions based on user input. The available options are:

1. Add Task: Prompts the user to enter task details and adds a new task to the list.
2. View Tasks: Displays all the tasks in the list.
3. Update Task: Allows the user to update the details of a specific task by entering its ID and the new values.
4. Delete Task: Deletes a specific task from the list based on its ID.
5. Save Tasks to File: Saves all tasks to a specified file in JSON format.
6. Load Tasks from File: Loads tasks from a specified file and adds them to the list.
7. Exit: Exits the application.

Usage Instructions

1. Run the Program: Execute the script to start the Task Management System.
2. Choose an Option: Select an option from the menu by entering the corresponding number.
3. Follow Prompts: Follow the prompts to add, view, update, delete, save, or load tasks.
4. Exit: Choose the "Exit" option to close the application.

This documentation provides a comprehensive overview of the design and usage of the Task Management System, enabling users to effectively manage their tasks using the provided interface.

