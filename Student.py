from tkinter import *
from tkinter import messagebox
import os

# Create student_data directory
os.makedirs("student_data", exist_ok=True)

# Track current user
current_user = {"username": ""}

# --- FUNCTION TO SWITCH SCREENS ---
def show_screen(frame):
    for widget in project.winfo_children():
        widget.pack_forget()
    frame.pack(fill="both", expand=True)

# Main window
project = Tk()
project.title("Student Login System")
project.geometry("850x600")
project.configure(background="#1a1a2e")
project.option_add("*Font", ("Segoe UI", 11))

# --- LOGIN SCREEN ---
login_frame = Frame(project, bg="#1a1a2e")

Label(login_frame, text="Student Login System", fg="#00cccc", bg="#1a1a2e",
      font=("Helvetica", 28, "bold")).pack(pady=30)

Label(login_frame, text="Enter Username", fg="#ffffff", bg="#1a1a2e").pack(pady=10)
login_user = Entry(login_frame, width=35)
login_user.pack(pady=5)

Label(login_frame, text="Enter Password", fg="#ffffff", bg="#1a1a2e").pack(pady=10)
login_pass = Entry(login_frame, show="*", width=35)
login_pass.pack(pady=5)

def login():
    user = login_user.get().strip()
    pwd = login_pass.get().strip()

    try:
        with open("student_data/user.txt", "r") as u_file, open("student_data/password.txt", "r") as p_file:
            users = u_file.readlines()
            passwords = p_file.readlines()

        for i in range(len(users)):
            if users[i].strip() == user and passwords[i].strip() == pwd:
                current_user["username"] = user
                messagebox.showinfo("Success", "Login Successful")
                show_screen(main_menu_frame)
                return
        messagebox.showerror("Error", "Invalid Username or Password")
    except FileNotFoundError:
        messagebox.showerror("Error", "User database not found.")

Button(login_frame, text="Login", command=login, width=14, height=2, fg="#ffffff", bg="#4CAF50").pack(pady=20)
Button(login_frame, text="Register New User", command=lambda: show_screen(register_frame),
       width=20, height=2, fg="#ffffff", bg="#2196F3").pack(pady=10)

# --- REGISTER SCREEN ---
register_frame = Frame(project, bg="#1a1a2e")

Label(register_frame, text="Register New User", fg="#00cccc", bg="#1a1a2e",
      font=("Helvetica", 24, "bold")).pack(pady=30)

Label(register_frame, text="New Username", fg="#ffffff", bg="#1a1a2e").pack(pady=10)
reg_user = Entry(register_frame, width=35)
reg_user.pack(pady=5)

Label(register_frame, text="New Password", fg="#ffffff", bg="#1a1a2e").pack(pady=10)
reg_pass = Entry(register_frame, show="*", width=35)
reg_pass.pack(pady=5)

def register_user():
    user = reg_user.get().strip()
    pwd = reg_pass.get().strip()

    if not user or not pwd:
        messagebox.showerror("Error", "All fields required.")
        return

    # Check for duplicates
    if os.path.exists("student_data/user.txt"):
        with open("student_data/user.txt", "r") as f:
            if user + "\n" in f.readlines():
                messagebox.showerror("Error", "Username already exists.")
                return

    # Save credentials
    with open("student_data/user.txt", "a") as u, open("student_data/password.txt", "a") as p:
        u.write(f"{user}\n")
        p.write(f"{pwd}\n")

    # Create user-specific ECA and Grades files
    with open(f"student_data/eca_{user}.txt", "w") as eca_file:
        eca_file.write("No ECA data available.")

    with open(f"student_data/grades_{user}.txt", "w") as grades_file:
        grades_file.write("No Grades available.")

    messagebox.showinfo("Success", "User Registered Successfully!")
    reg_user.delete(0, END)
    reg_pass.delete(0, END)
    show_screen(login_frame)

Button(register_frame, text="Register", command=register_user, bg="#4CAF50", fg="white", width=12).pack(pady=20)
Button(register_frame, text="Back to Login", command=lambda: show_screen(login_frame),
       bg="#FF5722", fg="white", width=14).pack()

# --- MAIN MENU SCREEN ---
main_menu_frame = Frame(project, bg="#1a1a2e")

Label(main_menu_frame, text="Main Menu", fg="#00cccc", bg="#1a1a2e", font=("Helvetica", 26, "bold")).pack(pady=30)

Button(main_menu_frame, text="ECA", command=lambda: load_eca_data(),
       width=14, height=2, fg="white", bg="#008080").pack(pady=15)

Button(main_menu_frame, text="Grades", command=lambda: load_grades_data(),
       width=14, height=2, fg="white", bg="#008080").pack(pady=15)

Button(main_menu_frame, text="Logout", command=lambda: show_screen(login_frame),
       width=14, height=2, fg="white", bg="#f44336").pack(pady=25)

# --- ECA SCREEN ---
eca_frame = Frame(project, bg="#1a1a2e")

def load_eca_data():
    eca_frame.pack_forget()
    for widget in eca_frame.winfo_children():
        widget.destroy()

    Label(eca_frame, text="Extra Curricular Activities", fg="#00cccc", bg="#1a1a2e",
          font=("Helvetica", 20, "bold")).pack(pady=20)

    try:
        with open(f"student_data/eca_{current_user['username']}.txt", "r") as f:
            eca_data = f.read()
    except FileNotFoundError:
        eca_data = "No ECA data available."

    Label(eca_frame, text=eca_data, fg="white", bg="#1a1a2e", wraplength=700, justify="left").pack(pady=10)

    Button(eca_frame, text="Back", command=lambda: show_screen(main_menu_frame),
           bg="#FF5722", fg="white", width=12).pack(pady=20)

    show_screen(eca_frame)

# --- GRADES SCREEN ---
grades_frame = Frame(project, bg="#1a1a2e")

def load_grades_data():
    grades_frame.pack_forget()
    for widget in grades_frame.winfo_children():
        widget.destroy()

    Label(grades_frame, text="Grades", fg="#00cccc", bg="#1a1a2e",
          font=("Helvetica", 20, "bold")).pack(pady=20)

    try:
        with open(f"student_data/grades_{current_user['username']}.txt", "r") as f:
            grades_data = f.read()
    except FileNotFoundError:
        grades_data = "No Grades available."

    Label(grades_frame, text=grades_data, fg="white", bg="#1a1a2e", wraplength=700, justify="left").pack(pady=10)

    Button(grades_frame, text="Back", command=lambda: show_screen(main_menu_frame),
           bg="#FF5722", fg="white", width=12).pack(pady=20)

    show_screen(grades_frame)

# Start with login screen
show_screen(login_frame)
project.mainloop()
