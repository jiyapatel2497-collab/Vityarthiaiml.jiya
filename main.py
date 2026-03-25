import mysql.connector
from datetime import date

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="procrastination_tracker"
)

cursor = db.cursor()

def add_task():
    title = input("Enter task title: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    priority = input("Enter priority (Low/Medium/High): ")

    query = """INSERT INTO tasks 
               (title, deadline, priority, status, delay_count, created_date)
               VALUES (%s, %s, %s, 'Pending', 0, %s)"""
    
    cursor.execute(query, (title, deadline, priority, date.today()))
    db.commit()
    print("Task Added Successfully!\n")


def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    print("\n--- TASK LIST ---")
    for t in tasks:
        print(f"ID: {t[0]}, Title: {t[1]}, Deadline: {t[2]}, Priority: {t[3]}, Status: {t[4]}, Delays: {t[5]}")
    print()


def mark_delay():
    task_id = int(input("Enter Task ID to mark delay: "))
    query = "UPDATE tasks SET delay_count = delay_count + 1 WHERE id=%s"
    cursor.execute(query, (task_id,))
    db.commit()
    print("Delay Recorded!\n")


def complete_task():
    task_id = int(input("Enter Task ID to complete: "))
    query = "UPDATE tasks SET status='Completed', completed_date=%s WHERE id=%s"
    cursor.execute(query, (date.today(), task_id))
    db.commit()
    print("Task Completed!\n")


def show_score():
    cursor.execute("SELECT COUNT(*), IFNULL(SUM(delay_count),0) FROM tasks")
    total_tasks, total_delays = cursor.fetchone()

    if total_tasks == 0:
        print("No tasks available.\n")
        return

    score = (total_delays / total_tasks) * 100

    print(f"\n📊 Procrastination Score: {score:.2f}%")

    if score < 20:
        print("Excellent! You rarely procrastinate.")
    elif score < 50:
        print("Moderate procrastination. Try to improve.")
    else:
        print("High procrastination! Take action.\n")


def insights():
    print("\n--- INSIGHTS ---")

    # Most delayed task
    cursor.execute("SELECT title, delay_count FROM tasks ORDER BY delay_count DESC LIMIT 1")
    result = cursor.fetchone()
    if result:
        print(f"Most delayed task: {result[0]} ({result[1]} delays)")

    # Priority analysis
    cursor.execute("SELECT priority, SUM(delay_count) FROM tasks GROUP BY priority")
    data = cursor.fetchall()
    print("\nDelay by Priority:")
    for d in data:
        print(f"{d[0]}: {d[1]} delays")

    print()

def menu():
    while True:
        print("====== PROCRASTINATION TRACKER ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Delay")
        print("4. Complete Task")
        print("5. Show Procrastination Score")
        print("6. View Insights")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_delay()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            show_score()
        elif choice == '6':
            insights()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")


menu()
