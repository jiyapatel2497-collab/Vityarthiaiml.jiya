import datetime

tasks = []

# Function to add a task
def add_task():
    name = input("Enter task name: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    
    task = {
        "name": name,
        "deadline": deadline,
        "completed": False,
        "completed_date": None
    }
    
    tasks.append(task)
    print("✅ Task added successfully!\n")

# Function to mark task as completed
def complete_task():
    view_tasks()
    index = int(input("Enter task number to mark as completed: ")) - 1
    
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        tasks[index]["completed_date"] = str(datetime.date.today())
        print("🎉 Task marked as completed!\n")
    else:
        print("❌ Invalid task number.\n")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("📭 No tasks available.\n")
        return
    
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} | Deadline: {task['deadline']} | Status: {status}")
    print()

# Function to check procrastinated tasks
def check_procrastination():
    today = datetime.date.today()
    
    print("\n⚠️ Procrastination Report:")
    found = False
    
    for task in tasks:
        deadline = datetime.datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        
        if not task["completed"] and deadline < today:
            print(f"❌ You delayed: {task['name']} (Deadline was {task['deadline']})")
            found = True
        
        elif task["completed"]:
            completed_date = datetime.datetime.strptime(task["completed_date"], "%Y-%m-%d").date()
            if completed_date > deadline:
                print(f"⏰ Late completion: {task['name']}")
                found = True
    
    if not found:
        print("✅ No procrastination detected. Great job!\n")

# Main menu
def main():
    while True:
        print("=== Procrastination Tracker ===")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Check Procrastination")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            complete_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            check_procrastination()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.\n")

# Run the program
main()
