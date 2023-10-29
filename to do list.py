todo_list=[]
def add_task(task):
    todo_list.append(task)
    print(f"Task'(task)' has been added to the to-do list.")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task'(task)' has been removed from the to-do list.")
    else:
        print(f"Task'(task)' not found in the to-do list.")

def display_list():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-do list:")
        for index,task in enumerate(todo_list,start=1):
            print(f"(index).(task)")
while True:
    print("\nChoose an option:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display the to-do list")
    print("4. Quit")

    choice=input("Enter the option number:")

    if choice=='1':
        task=input("Enter the task:")
        add_task(task)
    elif choice=='2':
        task=input("Enter the task to remove:")
        remove_task(task)
    elif choice=='3':
        display_list()
    elif choice=='4':
        print("Goodbye!")
        break
    else:
        print("Invalid option,Please choose a valid option.")