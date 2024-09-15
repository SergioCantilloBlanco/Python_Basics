import csv

def read_document():
    try:
        with open(r'C:\Users\34684\Desktop\Personal P\Basic_python\files\tasks_file.csv', 'r') as file:
            reader = csv.reader(file)
            tasks = [tuple(row) for row in reader]
            if len(tasks) == 0:
                return []
            else:
                return tasks
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def add(tasks):
    try:
        task = (input("Task to be added:"), "Incomplete")
        tasks.append(task)
        save(tasks)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def save(tasks):
    with open(r'C:\Users\34684\Desktop\Personal P\Basic_python\files\tasks_file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

def show(tasks):
    print("\n"*10)
    for task in tasks:
        print(f"{(tasks.index(task))+1}. {task[0]} --> Status: {task[1]}")
    print("\n")
    while True:
        if input("Do you wish to continue(yes/no)?").lower() in ["yes","y"]:
            break

    


def delete(tasks):
    try:    
        task_no = int(input("Enter the task number to delete: "))
        if 1 <= task_no <= len(tasks):
            deleted_task = tasks.pop(task_no - 1)
            print(f"Task '{deleted_task[0]}' deleted.")
            save(tasks)
        else:
            print("Invalid task number.")
    except:
        print("Something went wrong")



def complete(tasks):
    try:    
        task_no = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no-1] = (tasks[task_no-1][0],"Complete")
            save(tasks)
        else:
            print("Invalid task number.")
    except:
        print("Something went wrong")


def ask_user(prompt):
    tasks = {"1": add, "2": show, "3":delete, "4": complete}
    task_list = read_document()
    while True:
        print("\n"*5)
        print("TO-DO List")
        print("Please Select Action")
        print("1.Add task.")
        print("2.Show tasks.")
        print("3.Delete task.")
        print("4.Complete task.")
        print("5.Exit")
        user_input = input(prompt)
        if user_input == '5':
            print("Thanks for using our services, see you soon.")
            break
        elif user_input in tasks:
            tasks[user_input](task_list)
        else:
            print("Please select a valid action.")
    

def main():
        ask_user("Action(1-5):")
        print("\n")


    



if __name__ == "__main__":
    main()