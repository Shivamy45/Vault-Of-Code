"""
Develop a basic to-do list application using functions and data structures

Project Overview:
Objective: Develop a simple to-do list application using Python with an emphasis on
functions and data structures.

Key Components:
1. Functions: You'll be implementing various functions to handle different aspects of the
to-do list application. Functions are modular blocks of code that perform specific tasks,
making your code more organized and easier to understand.
Function to add a task
Function to delete a task
Function to display the list of tasks
Function to mark a task as complete

2. Data Structures: Utilize appropriate data structures to store and manage the to-do list.
A common choice would be a list or a dictionary, but you can explore other options based
on your creativity and understanding.
"""

def add_task(task_list, task):
  """Adds a task to the task list."""
  task_list.append(task)
  print(f"Task '{task}' added to the list.")

def delete_task(task_list, index):
  """Removes a task from the task list based on its index."""
  if 1 <= index <= len(task_list):
    removed_task = task_list.pop(index - 1)
    print(f"Task '{removed_task}' removed from the list.")
  else:
    print("Invalid task index.")

def display_tasks(task_list):
  """Displays the current tasks in the list."""
  if not task_list:
    print("Your to-do list is empty.")
  else:
    print("Your to-do list:")
    for index, task in enumerate(task_list, start=1):
      print(f"{index}. {task}")

def mark_complete(task_list, index):
  """Marks a task as complete."""
  if 1 <= index <= len(task_list):
    task_list[index - 1] = f"✓ {task_list[index - 1]}"
    print(f"Task marked as complete.")
  else:
    print("Invalid task index.")

def main():
  task_list = []

  while True:
    print("\nTo-Do List App")
    print("1. Add task")
    print("2. Delete task")
    print("3. Display tasks")
    print("4. Mark task as complete")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
      task = input("Enter the task: ")
      add_task(task_list, task)
    elif choice == '2':
      task_index = int(input("Enter the task index to delete: "))
      delete_task(task_list, task_index)
    elif choice == '3':
      display_tasks(task_list)
    elif choice == '4':
      task_index = int(input("Enter the task index to mark as complete: "))
      mark_complete(task_list, task_index)
    elif choice == '5':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
