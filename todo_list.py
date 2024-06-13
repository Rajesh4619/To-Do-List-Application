tasks = []

#for displaying tasks
def display_tasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['task']} ({status})")

#for adding tasks
def add_task(task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' added to the list.")

#foe marking task completed or not
def mark_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

#for removing a task
def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' has been removed.")
    else:
        print("Invalid task number. Please enter a valid task number.")
 

if __name__ == "__main__":
  print("Welcome to the to do list app :")
#  creating a loop to run the app
while True:
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task_name = input("Enter the task : ")
        add_task(task_name)
    elif choice == '3':
        display_tasks()
        task_number = int(input("Enter the task number to mark as completed "))
        mark_completed(task_number)
    elif choice == '4':
        display_tasks()
        task_number = int(input("Enter the task number to delete: "))
        delete_task(task_number)
    elif choice == '5':
        break
    else: 
        print("Invalid choice. Please enter a valid option.")
print("Goodbye")