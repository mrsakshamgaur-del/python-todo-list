task = []
def load_tasks():
    try:
        with open("tasks_txt.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []
task = load_tasks()   
def save_tasks():
    with open("tasks_txt.txt", "w") as file:
        for i in task: file.write(i + "\n")
def add_task(task_name):
    task.append(task_name)
    save_tasks()
    print(f'Task added successfully!')
def view_tasks():
        if len(task) == 0:
            print("No tasks found.")
        else:    
            print(f'========= Tasks =========')
            for index, i in enumerate(task, start=1):
                print(f'{index}. {i}')
def delete_task():
    if not task:
        print("No tasks to delete.")
        return
    n = int(input("Enter task number: "))  
    index = n - 1
    if 0 <= index < len(task):
        deleted_task = task.pop(index)
        save_tasks()
        print(f'Task "{deleted_task}" deleted successfully!')
    else:
        print("Invalid task number.")  
def count_tasks():
    if len(task) == 0:
        print("No tasks found.")
    else:
        print(f'Total tasks: {len(task)}')
while True:
    print(f'========= TO-DO LIST =========')
    print(f'1. Add Task')
    print(f'2. View Tasks')
    print(f'3. Delete Task ')
    print(f'4. Count Task')
    print(f'5. Exit')
    choice = input("Enter your choice: ")
    if choice == '1':
        task_name = input("Enter the task name: ")
        add_task(task_name)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task() 
    elif choice == '5':
        print("Exiting...")
        break
    elif choice == '4':
        count_tasks()
    else:
        print("Invalid choice. Please try again.")
        
        
