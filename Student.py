from tkinter import *
from tkinter import messagebox
import os

# Create student_data directory
os.makedirs("student_data", exist_ok=True)

# Default credentials (for initial testing)
with open("student_data/id.txt", "w") as f:
    f.write("nirajannami@gmail.com")

with open("student_data/password.txt", "w") as f:
    f.write("Nirajan")

# Main window
project = Tk()
project.title("Student Login System")
project.geometry("850x600")
project.resizable(False, False)
project.configure(background="#1a1a2e")
project.option_add("*Font", ("Segoe UI", 11))

# Header
head = Label(project, text="Student Login System", fg="#00cccc", bg="#121212", font=("Helvetica", 28, "bold"))
head.pack(pady=30)

# Username input
username_label = Label(project, text="Enter Username", fg="#ffffff", bg="#121212", font=("Helvetica", 14))
username_label.pack(pady=10)

form = Entry(project, width=35, font=("Helvetica", 12))
form.pack(pady=10)

# Password input
password_label = Label(project, text="Enter Password", fg="#ffffff", bg="#121212", font=("Helvetica", 14))
password_label.pack(pady=10)

form_ii = Entry(project, show="*", width=35, font=("Helvetica", 12))
form_ii.pack(pady=10)

# --- LOGIN FUNCTION ---
def trigger():
    f1 = form.get()
    f2 = form_ii.get()

    try:
        with open("student_data/users.txt", "r") as user_file:
            lines = user_file.readlines()
            for line in lines:
                stored_user, stored_pass = line.strip().split(",")
                if f1 == stored_user and f2 == stored_pass:
                    messagebox.showinfo("Success", "Login Successful")
                    new_window()
                    return
            messagebox.showerror("Error", "Invalid Username or Password")
    except FileNotFoundError:
        messagebox.showerror("Error", "No users found. Please register first.")

# --- REGISTER FUNCTION ---
def open_register_window():
    reg_win = Toplevel()
    reg_win.title("Register New User")
    reg_win.geometry("400x300")
    reg_win.configure(background="#2e2e2e")

    Label(reg_win, text="New Username:", fg="white", bg="#2e2e2e", font=("Helvetica", 12)).pack(pady=10)
    new_user_entry = Entry(reg_win, font=("Helvetica", 12))
    new_user_entry.pack(pady=5)

    Label(reg_win, text="New Password:", fg="white", bg="#2e2e2e", font=("Helvetica", 12)).pack(pady=10)
    new_pass_entry = Entry(reg_win, show="*", font=("Helvetica", 12))
    new_pass_entry.pack(pady=5)

    def register_user():
        new_user = new_user_entry.get().strip()
        new_pass = new_pass_entry.get().strip()

        if not new_user or not new_pass:
            messagebox.showerror("Error", "Please fill in both fields.")
            return

        with open("student_data/users.txt", "a") as user_file:
            user_file.write(f"{new_user},{new_pass}\n")

        messagebox.showinfo("Success", "User Registered Successfully!")
        reg_win.destroy()

    Button(reg_win, text="Register", command=register_user, bg="#4CAF50", fg="white",
           font=("Helvetica", 12, "bold"), width=12).pack(pady=20)

    # --- MAIN MENU AFTER LOGIN ---
def new_window():
    win = Toplevel()
    win.minsize(300, 200)
    win.maxsize(300, 200)
    win.configure(background="#1e1e1e")

    btn_eca = Button(win, width=12, height=2, text="ECA", fg="#ffffff", bg="#008080",
                     font=("Helvetica", 12, "bold"), command=trigger_eca)
    btn_eca.pack(pady=15)

    btn_grades = Button(win, width=12, height=2, text="Grades", fg="#ffffff", bg="#008080",
                        font=("Helvetica", 12, "bold"), command=trigger_grades)
    btn_grades.pack(pady=15)

    # --- ECA DISPLAY ---
def trigger_eca():
    eca = Toplevel()
    eca.minsize(300, 200)
    eca.maxsize(300, 200)
    eca.configure(background="#1e1e1e")

    try:
        with open("student_data/eca.txt", "r") as eca_data:
            std_eca = eca_data.read()
    except FileNotFoundError:
        std_eca = "No ECA data found."

    eca_label = Label(eca, text=std_eca, fg="#ffffff", bg="#1e1e1e", font=("Helvetica", 12))
    eca_label.pack(pady=20)

# --- GRADES DISPLAY ---
def trigger_grades():
    grades = Toplevel()
    grades.title("Grades")
    grades.minsize(350, 250)
    grades.maxsize(400, 300)
    grades.configure(background="#1e1e1e")

    try:
        with open("student_data/grades.txt", "r") as grades_data:
            grades_content = grades_data.read()
    except FileNotFoundError:
        grades_content = "⚠️ No Grades data found."

    grades_label = Label(
        grades,
        text=grades_content,
        fg="#f0f0f0",
        bg="#1e1e1e",
        font=("Segoe UI", 12, "bold"),
        justify="left",
        wraplength=320
    )
    grades_label.pack(padx=20, pady=25, anchor="w")

# --- BUTTONS ---
submit_button = Button(
    project,
    text="Login",
    width=14,
    height=2,
    fg="#ffffff",
    bg="#4CAF50",
    activebackground="#45a049",
    activeforeground="#ffffff",
    font=("Segoe UI", 13, "bold"),
    borderwidth=0,
    relief="flat",
    command=trigger
)
submit_button.pack(pady=20)

register_button = Button(
    project,
    text="Register New User",
    width=20,
    height=2,
    fg="#ffffff",
    bg="#2196F3",
    activebackground="#1976D2",
    activeforeground="#ffffff",
    font=("Segoe UI", 12, "bold"),
    command=open_register_window
)
register_button.pack(pady=10)

project.mainloop()