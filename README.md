POCRASTINATION TRACKER (Python Project)
1. Introduction
The Procrastination Tracker is a command-line based Python application that helps users manage their daily tasks and track procrastination behavior. In today’s fast-paced world, people often delay their work due to distractions, lack of motivation, or poor time management. This project is designed to address that issue by providing a simple and effective way to monitor tasks and deadlines.

This system allows users to:
✔️ Add tasks with deadlines
✔️ Track completion status
✔️ Identify delayed or late tasks
✔️ Analyze productivity habits
The project is especially useful for students who want to improve discipline and complete assignments on time.
2. Objectives
The main objectives of this project are:
➤ To develop a simple task management system
➤ To help users identify procrastination patterns
➤ To improve time management skills
➤ To provide a user-friendly interface using Python
➤ To encourage productivity and discipline
3. Key Features
🔹 Task Management
✔️ Add new tasks with deadlines
✔️ Store task details (name, deadline, status)
🔹 Task Completion
✔️ Mark tasks as completed
✔️ Automatically store completion date
🔹 Task Viewing
✔️ Display all tasks in an organized format
✔️ Show status: Pending / Completed
🔹 Procrastination Detection
 Identify tasks not completed before deadline
 Detect tasks completed after deadline
🔹 User-Friendly Interface
✔️ Simple menu-driven system
✔️ Easy navigation
4.System Requirements
✔️ Python 3.x installed
✔️ Basic knowledge of running Python programs
✔️ Any text editor (VS Code / Notepad / PyCharm)
5.Working of the Project
The project works using a simple list-based data structure:
➤ Step 1: Add Task
User enters:
Task name
Deadline (YYYY-MM-DD)
➤ Step 2: Store Data
The program stores task details in a list of dictionaries.
➤ Step 3: Complete Task
User selects a task and marks it as completed.
The system records the completion date.
➤ Step 4: Analyze Procrastination
 If task is not completed and deadline has passed → ❌ Procrastinated
 If task is completed after deadline → ⏰ Late
If task is completed on time → ✅ Good productivity
6. Example Output
=== Procrastination Tracker ===
1. Add Task
2. Complete Task
3. View Tasks
4. Check Procrastination
5. Exit
 Sample Tasks Display:
1. Complete Assignment | Deadline: 2026-03-20 | Status: Pending
2. Study Python        | Deadline: 2026-03-18 | Status: Done
7. Procrastination Report:
 You delayed: Complete Assignment (Deadline was 2026-03-20)
 Late completion: Study Python
8.. Project Structure
 Procrastination Tracker
  📄 procrastination_tracker.py   → Main program file
   📄 README.md                    → Documentation file
 9. Advantages
 Simple and easy to use
 Helps improve productivity
 Tracks deadlines effectively
 Useful for students and beginners
 Lightweight and fast
10. Limitations
 Data is not saved permanently (resets after program closes)
 No graphical user interface (GUI)
 No notifications or reminders
 11. Future Enhancements
 Add JSON/database storage
Add notification/reminder system
 Add charts and productivity analysis
 Develop GUI using Tkinter
 Convert into a web or mobile application
12. Conclusion
The Procrastination Tracker is a useful beginner-friendly Python project that demonstrates how programming can be used to solve real-life problems like time management and procrastination. It helps users become more aware of their habits and encourages them to complete tasks on time.
 
