def load_task():
    try:
        with open('task.txt', 'r') as file:
            content = file.read().split('\n')
            return [task for task in content if task]  # remove empty lines
    except FileNotFoundError:
        return []


def save_task(task_list):
    with open('task.txt', 'w') as file:
        for task in task_list:
            file.write(task + '\n')


task_list = load_task()

while True:
    try:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Exit")

        user_input = int(input("> Enter your choice: "))

        # 🔹 ADD TASK
        if user_input == 1:
            new_task = input("Enter task: ")
            task_list.append("[ ] " + new_task)
            save_task(task_list)

        # 🔹 VIEW TASKS
        elif user_input == 2:
            for i, item in enumerate(task_list):
                print(f"{i+1}. {item}")

        # 🔹 DELETE TASK
        elif user_input == 3:
            delete_task = int(input("Enter task number to delete: "))
            if 0 < delete_task <= len(task_list):
                task_list.pop(delete_task - 1)
                save_task(task_list)
            else:
                print("Invalid index")

        # 🔹 COMPLETE TASK
        elif user_input == 4:
            complete_task = int(input("Enter task number to mark complete: "))
            if 0 < complete_task <= len(task_list):
                task_list[complete_task - 1] = task_list[complete_task - 1].replace("[ ]", "[x]")
                save_task(task_list)
            else:
                print("Invalid index")

        # 🔹 EXIT
        elif user_input == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")

    except Exception as e:
        print("Error:", e)