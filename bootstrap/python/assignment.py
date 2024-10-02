import tkinter as tk
from tkinter import messagebox, ttk
import re
import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect('college_management.db')
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        department TEXT,
        roll_number TEXT PRIMARY KEY
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        name TEXT,
        department TEXT,
        attendance TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        name TEXT,
        department TEXT,
        result TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tutors (
        name TEXT,
        qualification TEXT,
        contact TEXT
    )''')

    conn.commit()
    conn.close()

# Sample data to populate the database
def populate_sample_data():
    conn = sqlite3.connect('college_management.db')
    cursor = conn.cursor()
    
    # Sample students
    students = [
        ("Pema", "IT", "D2CSN"),
        ("Dorji", "IT", "BEPE"),
        ("Penjor", "IT", "D1CS"),
        ("Karma", "Civil", "C2CI"),
        ("Tshering", "Civil", "BECE"),
        ("Nima", "Civil", "C1CI"),
        ("Sangay", "Mechanical", "D2ME"),
        ("Phuntsho", "Mechanical", "D1ME"),
        ("Tashi", "Mechanical", "BEME"),
        ("Sonam", "Electrical", "D2EE"),
        ("Choden", "Electrical", "BEEL"),
        ("Karma", "Electrical", "D1EE"),
        ("Karma", "Others", "D2OT"),
        ("Tashi", "Others", "BEOT"),
        ("Lhamo", "Others", "D1OT"),
    ]
    cursor.executemany('INSERT OR IGNORE INTO students (name, department, roll_number) VALUES (?, ?, ?)', students)

    # Sample attendance
    attendance = [
        ("Pema", "IT", "90%"),
        ("Dorji", "IT", "50%"),
        ("Penjor", "IT", "75%"),
        ("Karma", "Civil", "80%"),
        ("Tshering", "Civil", "95%"),
        ("Nima", "Civil", "60%"),
        ("Sangay", "Mechanical", "85%"),
        ("Phuntsho", "Mechanical", "70%"),
        ("Tashi", "Mechanical", "65%"),
        ("Sonam", "Electrical", "90%"),
        ("Choden", "Electrical", "80%"),
        ("Karma", "Electrical", "100%"),
        ("Karma", "Others", "55%"),
        ("Tashi", "Others", "40%"),
        ("Lhamo", "Others", "75%"),
    ]
    cursor.executemany('INSERT OR IGNORE INTO attendance (name, department, attendance) VALUES (?, ?, ?)', attendance)

    # Sample results
    results = [
        ("Pema", "IT", "RA in Python Programming"),
        ("Dorji", "IT", "Passed"),
        ("Penjor", "IT", "Fail"),
        ("Karma", "Civil", "Passed"),
        ("Tshering", "Civil", "RA in Structural Analysis"),
        ("Nima", "Civil", "Fail"),
        ("Sangay", "Mechanical", "Passed"),
        ("Phuntsho", "Mechanical", "RA in Thermodynamics"),
        ("Tashi", "Mechanical", "Fail"),
        ("Sonam", "Electrical", "Passed"),
        ("Choden", "Electrical", "RA in Circuit Theory"),
        ("Karma", "Electrical", "Fail"),
        ("Karma", "Others", "Passed"),
        ("Tashi", "Others", "RA in Project Management"),
        ("Lhamo", "Others", "Fail"),
    ]
    cursor.executemany('INSERT OR IGNORE INTO results (name, department, result) VALUES (?, ?, ?)', results)

    # Sample tutors
    tutors = [
        ("Tashi", "Master in Computer Science", "77712842"),
        ("Dorji", "Degree in HTML", "17253609"),
        ("Wangchuk", "Bachelor in Mathematics", "88812345"),
    ]
    cursor.executemany('INSERT OR IGNORE INTO tutors (name, qualification, contact) VALUES (?, ?, ?)', tutors)

    conn.commit()
    conn.close()

# Fetch data from the database
def fetch_students_data():
    conn = sqlite3.connect('college_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, roll_number, department FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

def fetch_attendance_data(department):
    conn = sqlite3.connect('college_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, attendance FROM attendance WHERE department=?", (department,))
    attendance = cursor.fetchall()
    conn.close()
    return attendance

def fetch_results_data(department):
    conn = sqlite3.connect('college_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, result FROM results WHERE department=?", (department,))
    results = cursor.fetchall()
    conn.close()
    return results

def fetch_tutors_data():
    conn = sqlite3.connect('college_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, qualification, contact FROM tutors")
    tutors = cursor.fetchall()
    conn.close()
    return tutors

# Initialize database and populate data
init_db()
populate_sample_data()

# GUI Application
root = tk.Tk()
root.title("College Management System")
root.geometry("600x600")

def show_login_options():
    for widget in root.winfo_children():
        widget.destroy()

    title_label = tk.Label(root, text="Select Login Option", font=("Arial", 20, "bold"), bg="#87CEFA", fg="black")
    title_label.pack(pady=20)

    student_button = tk.Button(root, text="Login as Student", bg="#FFB6C1", fg="black", font=("Arial", 16), command=show_login_button)
    student_button.pack(pady=10)

    admin_button = tk.Button(root, text="Login as Admin", bg="#FFB6C1", fg="black", font=("Arial", 16), command=show_admin_login)
    admin_button.pack(pady=10)

    back_button = tk.Button(root, text="Back", bg="#FFB6C1", fg="black", font=("Arial", 16), command=show_start_button)
    back_button.pack(pady=10)
    back_button.place(relx=0.01, rely=0.85)  # Positioned at the left bottom

def show_start_button():
    for widget in root.winfo_children():
        widget.destroy()

    welcome_label = tk.Label(root, text="Welcome to College Management System", font=("Arial", 20, "bold"), pady=20, bg="#87CEFA", fg="black")
    welcome_label.pack()

    start_button = tk.Button(root, text="Start", font=("Arial", 16, "bold"), width=15, bg="#FFB6C1", fg="black", command=show_login_options)
    start_button.pack(pady=20)

    exit_button = tk.Button(root, text="Exit", font=("Arial", 16, "bold"), width=15, bg="#FFB6C1", fg="black", command=root.quit)
    exit_button.pack(pady=20)

def show_login_button():
    for widget in root.winfo_children():
        widget.destroy()

    email_label = tk.Label(root, text="Enter your College Email:", bg="#87CEFA", fg="black", font=("Arial", 14))
    email_label.pack(pady=5)
    email_entry = tk.Entry(root, width=30, bd=2, relief="groove", font=("Arial", 14))
    email_entry.pack(pady=5)

    password_label = tk.Label(root, text="Enter your Password:", bg="#87CEFA", fg="black", font=("Arial", 14))
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, width=30, show="*", bd=2, relief="groove", font=("Arial", 14))
    password_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Login", bg="#FFB6C1", fg="black", font=("Arial", 16), command=lambda: validate_login(email_entry.get(), password_entry.get()))
    submit_button.pack(pady=20)

    root.bind('<Return>', lambda event: validate_login(email_entry.get(), password_entry.get()))

    back_button = tk.Button(root, text="Back", bg="#FFB6C1", fg="black", font=("Arial", 16),
                            command=show_login_options)
    back_button.place(relx=0.01, rely=0.85)

def validate_login(email, password):
    if re.match(r'^\d{8}\.jnec@rub\.edu\.bt$', email) and len(password) == 6:
        show_student_dashboard()
    else:
        messagebox.showerror("Login Error", "Invalid email or password format.")

def show_student_dashboard():
    for widget in root.winfo_children():
        widget.destroy()

    dashboard_label = tk.Label(root, text="Student Dashboard", font=("Arial", 20, "bold"), bg="#87CEFA", fg="black")
    dashboard_label.pack(pady=20)

    # Fetch and display students
    students_data = fetch_students_data()
    students_treeview = ttk.Treeview(root, columns=("Name", "Roll Number", "Department"), show="headings")
    students_treeview.heading("Name", text="Name")
    students_treeview.heading("Roll Number", text="Roll Number")
    students_treeview.heading("Department", text="Department")
    students_treeview.pack(pady=10)

    for student in students_data:
        students_treeview.insert("", "end", values=student)

    attendance_button = tk.Button(root, text="View Attendance", command=lambda: show_attendance("IT"), bg="#FFB6C1", fg="black", font=("Arial", 14))
    attendance_button.pack(pady=5)

    results_button = tk.Button(root, text="View Results", command=lambda: show_results("IT"), bg="#FFB6C1", fg="black", font=("Arial", 14))
    results_button.pack(pady=5)

    feedback_button = tk.Button(root, text="Give Feedback", command=show_feedback_form, bg="#FFB6C1", fg="black", font=("Arial", 14))
    feedback_button.pack(pady=5)

    back_button = tk.Button(root, text="Logout", command=show_start_button, bg="#FFB6C1", fg="black", font=("Arial", 16))
    back_button.place(relx=0.01, rely=0.85)

def show_attendance(department):
    for widget in root.winfo_children():
        widget.destroy()

    attendance_label = tk.Label(root, text="Attendance for " + department, font=("Arial", 20, "bold"), bg="#87CEFA", fg="black")
    attendance_label.pack(pady=20)

    attendance_data = fetch_attendance_data(department)
    attendance_treeview = ttk.Treeview(root, columns=("Name", "Attendance"), show="headings")
    attendance_treeview.heading("Name", text="Name")
    attendance_treeview.heading("Attendance", text="Attendance")
    attendance_treeview.pack(pady=10)

    for record in attendance_data:
        attendance_treeview.insert("", "end", values=record)

    back_button = tk.Button(root, text="Back", command=lambda: show_student_dashboard(), bg="#FFB6C1", fg="black", font=("Arial", 16))
    back_button.place(relx=0.01, rely=0.85)

def show_results(department):
    for widget in root.winfo_children():
        widget.destroy()

    results_label = tk.Label(root, text="Results for " + department, font=("Arial", 20, "bold"), bg="#87CEFA", fg="black")
    results_label.pack(pady=20)

    results_data = fetch_results_data(department)
    results_treeview = ttk.Treeview(root, columns=("Name", "Result"), show="headings")
    results_treeview.heading("Name", text="Name")
    results_treeview.heading("Result", text="Result")
    results_treeview.pack(pady=10)

    for record in results_data:
        results_treeview.insert("", "end", values=record)

    back_button = tk.Button(root, text="Back", command=lambda: show_student_dashboard(), bg="#FFB6C1", fg="black", font=("Arial", 16))
    back_button.place(relx=0.01, rely=0.85)

def show_feedback_form():
    for widget in root.winfo_children():
        widget.destroy()

    feedback_label = tk.Label(root, text="Give Feedback", font=("Arial", 20, "bold"), bg="#87CEFA", fg="black")
    feedback_label.pack(pady=20)

    feedback_text = tk.Text(root, height=10, width=40, font=("Arial", 14))
    feedback_text.pack(pady=10)

    submit_button = tk.Button(root, text="Submit Feedback", command=lambda: submit_feedback(feedback_text.get("1.0", tk.END)), bg="#FFB6C1", fg="black", font=("Arial", 14))
    submit_button.pack(pady=10)

    back_button = tk.Button(root, text="Back", command=show_student_dashboard, bg="#FFB6C1", fg="black", font=("Arial", 16))
    back_button.place(relx=0.01, rely=0.85)

def submit_feedback(content):
    conn = sqlite3.connect('college_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Feedback", "Feedback submitted successfully!")
    show_student_dashboard()

def show_admin_login():
    for widget in root.winfo_children():
        widget.destroy()

    email_label = tk.Label(root, text="Enter Admin Email:", bg="#87CEFA", fg="black", font=("Arial", 14))
    email_label.pack(pady=5)
    email_entry = tk.Entry(root, width=30, bd=2, relief="groove", font=("Arial", 14))
    email_entry.pack(pady=5)

    password_label = tk.Label(root, text="Enter Admin Password:", bg="#87CEFA", fg="black", font=("Arial", 14))
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, width=30, show="*", bd=2, relief="groove", font=("Arial", 14))
    password_entry.pack(pady=5)

    submit_button = tk.Button(root, text="Login", bg="#FFB6C1", fg="black", font=("Arial", 16), command=lambda: validate_admin_login(email_entry.get(), password_entry.get()))
    submit_button.pack(pady=20)

    back_button = tk.Button(root, text="Back", bg="#FFB6C1", fg="black", font=("Arial", 16), command=show_login_options)
    back_button.place(relx=0.01, rely=0.85)

def validate_admin_login(email, password):
    if email == "admin@example.com" and password == "admin":
        show_admin_dashboard()
    else:
        messagebox.showerror("Login Error", "Invalid admin credentials.")

def show_admin_dashboard():
    for widget in root.winfo_children():
        widget.destroy()

    admin_dashboard_label = tk.Label(root, text="Admin Dashboard", font=("Arial", 20, "bold"), bg="#87CEFA", fg="black")
    admin_dashboard_label.pack(pady=20)

    # Fetch and display tutors
    tutors_data = fetch_tutors_data()
    tutors_treeview = ttk.Treeview(root, columns=("Name", "Qualification", "Contact"), show="headings")
    tutors_treeview.heading("Name", text="Name")
    tutors_treeview.heading("Qualification", text="Qualification")
    tutors_treeview.heading("Contact", text="Contact")
    tutors_treeview.pack(pady=10)

    for tutor in tutors_data:
        tutors_treeview.insert("", "end", values=tutor)

    back_button = tk.Button(root, text="Logout", command=show_start_button, bg="#FFB6C1", fg="black", font=("Arial", 16))
    back_button.place(relx=0.01, rely=0.85)

show_start_button()
root.mainloop()
