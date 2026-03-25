 Procrastination Tracker

Overview
Procrastination is a common problem among students that leads to missed deadlines and reduced productivity.  
This project is a **Python + MySQL based system** designed to track task delays and analyze procrastination behavior using a calculated score and insights.

Objectives
- Track daily tasks and deadlines  
- Monitor how often tasks are delayed  
- Calculate a **Procrastination Score**  
- Provide insights to improve productivity  

Features
- Add tasks with deadline and priority  
- Record delays for each task  
- Mark tasks as completed  
- Calculate procrastination score  
- View insights (most delayed task, priority-wise delays)  

Tech Stack
- **Python** (Core logic & CLI interface)  
- **MySQL** (Database management)
- Setup Instructions
Install MySQL and create the database using the above SQL

Install required package:

pip install mysql-connector-python
Update your MySQL password in main.py

Run the application:
python main.py

How It Works
Each time a task is delayed, the delay count increases
The system calculates:

Procrastination Score = (Total Delays / Total Tasks) × 100

Score Interpretation
0–20% → Excellent (Low procrastination)
20–50% → Moderate
50%+ → High procrastination

Key Highlights
Real-world problem solving
Data-driven productivity analysis
Simple and user-friendly interface
Clean integration of Python and MySQL

Challenges Faced
Database connectivity handling
Designing delay tracking logic
Implementing meaningful insights

Future Improvements
GUI interface (Tkinter)
Graphical analytics (charts)
Notifications/reminders
AI-based suggestions

Real-World Impact
This project helps users become aware of their procrastination habits and take steps toward better time management and productivity
