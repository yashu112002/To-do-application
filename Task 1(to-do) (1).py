1# Initialize an empty list to store tasks
tasks = []

def add_task(task):
  """Adds a new task to the list."""
  tasks.append(task)
  print(f"{task} added to the list!")

def list_tasks():
  """Prints all tasks in the list."""
  if tasks:
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")
  else:
    print("No tasks in the list yet!")

def remove_task(index):
  """Removes a task from the list by index."""
  if index > 0 and index <= len(tasks):
    removed_task = tasks.pop(index-1)
    print(f"{removed_task} removed from the list!")
  else:
    print("Invalid task index!")

def mark_done(index):
  """Marks a task as done by index."""
  if index > 0 and index <= len(tasks):
    tasks[index-1] = f"[DONE] {tasks[index-1]}"
    print(f"Task marked as done!")
  else:
    print("Invalid task index!")

print("Welcome to your To-Do List!")

while True:
  print("\nMenu:")
  print("1. Add a task")
  print("2. List all tasks")
  print("3. Remove a task")
  print("4. Mark a task as done")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    task = input("Enter the task: ")
    add_task(task)
  elif choice == '2':
    list_tasks()
  elif choice == '3':
    index = int(input("Enter the task number to remove: "))
    remove_task(index)
  elif choice == '4':
    index = int(input("Enter the task number to mark as done: "))
    mark_done(index)
  elif choice == '5':
    print("Goodbye!")
    break
  else:
    print("Invalid choice!")
