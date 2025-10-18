import csv
import uuid
import datetime

all_tasks = []

def add_task():
    t = input("Task Title please: ")
    d = input("Task Description: ")
    new_task = {
        'Task ID': str(uuid.uuid4()),
        'Title': t,
        'Description': d,
        'Created On': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Status': 'Pending'
    }
    all_tasks.append(new_task)
    print("Yay! Task got added.\n")
    print("Task ID : ", new_task['Task ID'])
    print("Created On : ", new_task['Created On'])
    print("Status : ", new_task['Status'])

def show_tasks():
    print("All tasks you created:")
    for task in all_tasks:
        print(f"ID: {task['Task ID']}")
        print(f"Title: {task['Title']}")
        print(f"Description: {task['Description']}")
        print(f"Status: {task['Status']}")
        print(f"Created: {task['Created On']}")
        print("------------")

def complete_task():
    find_id = input("Enter Task ID to mark COMPLETE: ")
    for t in all_tasks:
        if t['Task ID'].startswith(find_id):
            t['Status'] = 'Completed'
            print("Well done! Task marked complete.")
            print('Motivation: "Keep pushing forward, you got this!"')
            return
    print("Sorry, no such task found.")

def show_done_tasks():
    print("Completed tasks:")
    for t in all_tasks:
        if t['Status'] == 'Completed':
            print(f"ID: {t['Task ID']}")
            print(f"Title: {t['Title']}")
            print(f"Completed at: {t['Created On']}")
            print(f"Status: {t['Status']}")
            print("-----")

def save_all():
    with open('tasks.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Task ID','Title','Description','Created On','Status'])
        writer.writeheader()
        writer.writerows(all_tasks)
    print("Tasks saved! File path: ./tasks.csv")

def main():
    while True:
        print("\n=== WELCOME TO MINI TASK SCHEDULER ===")
        print("1. Add  NEW Task")
        print("2. view All Tasks")
        print("3. Mark Task as Complete")
        print("4. View Completed Tasks")
        print("5. Exit ")
        choice = input("Pick (1-5): ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            show_done_tasks()
        elif choice == '5':
            save_all()
            print("Thanks for hanging out with Mini Task Scheduler. Bye!")
            break
        else:
            print("Oops, that wasn't right. Try again.")

if __name__ == '__main__':
    main()