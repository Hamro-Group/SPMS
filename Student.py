from tkinter import *
from tkinter import messagebox
import os

# Create student_data directory
os.makedirs("student_data", exist_ok=True)

# Write default test credentials into users.txt
with open("student_data/users.txt", "w") as f:
    f.write("nirajannami@gmail.com,Nirajan\n")

# Main window
project = Tk()
project.title("Student Login System")
project.geometry("850x600")
project.configure(background="#1a1a2e")
project.option_add("*Font", ("Segoe UI", 11))

# --- FUNCTION TO SWITCH SCREENS ---
def show_screen(frame):
    for widget in project.winfo_children():
        widget.pack_forget()
    frame.pack(fill="both", expand=True)

# --- LOGIN SCREEN ---
login_frame = Frame(project, bg="#1a1a2e")

Label(login_frame, text="Student Login System", fg="#00cccc", bg="#1a1a2e",
      font=("Helvetica", 28, "bold")).pack(pady=30)

Label(login_frame, text="Enter Username", fg="#ffffff", bg="#1a1a2e", font=("Helvetica", 14)).pack(pady=10)
login_user = Entry(login_frame, width=35, font=("Helvetica", 12))
login_user.pack(pady=5)

Label(login_frame, text="Enter Password", fg="#ffffff", bg="#1a1a2e", font=("Helvetica", 14)).pack(pady=10)
login_pass = Entry(login_frame, show="*", width=35, font=("Helvetica", 12))
login_pass.pack(pady=5)

def login():
    user = login_user.get().strip()
    pwd = login_pass.get().strip()

    try:
        with open("student_data/users.txt", "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                if user == u and pwd == p:
                    messagebox.showinfo("Success", "Login Successful")
                    show_screen(main_menu_frame)
                    return
            messagebox.showerror("Error", "Invalid Username or Password")
    except FileNotFoundError:
        messagebox.showerror("Error", "User database not found.")

Button(login_frame, text="Login", command=login, width=14, height=2, fg="#ffffff", bg="#4CAF50",
       font=("Segoe UI", 13, "bold")).pack(pady=20)

Button(login_frame, text="Register New User", command=lambda: show_screen(register_frame),
       width=20, height=2, fg="#ffffff", bg="#2196F3", font=("Segoe UI", 12, "bold")).pack(pady=10)

# --- REGISTER SCREEN ---
register_frame = Frame(project, bg="#1a1a2e")

Label(register_frame, text="Register New User", fg="#00cccc", bg="#1a1a2e",
      font=("Helvetica", 24, "bold")).pack(pady=30)

Label(register_frame, text="New Username", fg="#ffffff", bg="#1a1a2e", font=("Helvetica", 14)).pack(pady=10)
reg_user = Entry(register_frame, width=35, font=("Helvetica", 12))
reg_user.pack(pady=5)

Label(register_frame, text="New Password", fg="#ffffff", bg="#1a1a2e", font=("Helvetica", 14)).pack(pady=10)
reg_pass = Entry(register_frame, show="*", width=35, font=("Helvetica", 12))
reg_pass.pack(pady=5)

def register_user():
    user = reg_user.get().strip()
    pwd = reg_pass.get().strip()

    if not user or not pwd:
        messagebox.showerror("Error", "All fields required.")
        return

    with open("student_data/users.txt", "a") as f:
        f.write(f"{user},{pwd}\n")

    messagebox.showinfo("Success", "User Registered Successfully!")
    reg_user.delete(0, END)
    reg_pass.delete(0, END)
    show_screen(login_frame)

Button(register_frame, text="Register", command=register_user, bg="#4CAF50", fg="white",
       font=("Helvetica", 12, "bold"), width=12).pack(pady=20)

Button(register_frame, text="Back to Login", command=lambda: show_screen(login_frame),
       bg="#FF5722", fg="white", font=("Helvetica", 12), width=14).pack()

# --- MAIN MENU SCREEN ---
main_menu_frame = Frame(project, bg="#1a1a2e")

Label(main_menu_frame, text="Main Menu", fg="#00cccc", bg="#1a1a2e", font=("Helvetica", 26, "bold")).pack(pady=30)

Button(main_menu_frame, text="ECA", command=lambda: show_screen(eca_frame),
       width=14, height=2, fg="white", bg="#008080", font=("Helvetica", 12, "bold")).pack(pady=15)

Button(main_menu_frame, text="Grades", command=lambda: show_screen(grades_frame),
       width=14, height=2, fg="white", bg="#008080", font=("Helvetica", 12, "bold")).pack(pady=15)

Button(main_menu_frame, text="Logout", command=lambda: show_screen(login_frame),
       width=14, height=2, fg="white", bg="#f44336", font=("Helvetica", 12, "bold")).pack(pady=25)

# --- ECA SCREEN ---
eca_frame = Frame(project, bg="#1a1a2e")

Label(eca_frame, text="Extra Curricular Activities", fg="#00cccc", bg="#1a1a2e",
      font=("Helvetica", 20, "bold")).pack(pady=20)

try:
    with open("student_data/eca.txt", "r") as f:
        eca_data = f.read()
except FileNotFoundError:
    eca_data = "No ECA data available."

Label(eca_frame, text=eca_data, fg="white", bg="#1a1a2e", font=("Helvetica", 13),
      wraplength=700, justify="left").pack(pady=10)

Button(eca_frame, text="Back", command=lambda: show_screen(main_menu_frame),
       bg="#FF5722", fg="white", font=("Helvetica", 12), width=12).pack(pady=20)

# --- GRADES SCREEN ---
grades_frame = Frame(project, bg="#1a1a2e")

Label(grades_frame, text="Grades", fg="#00cccc", bg="#1a1a2e",
      font=("Helvetica", 20, "bold")).pack(pady=20)

try:
    with open("student_data/grades.txt", "r") as f:
        grades_data = f.read()
except FileNotFoundError:
    grades_data = "No Grades available."

Label(grades_frame, text=grades_data, fg="white", bg="#1a1a2e", font=("Helvetica", 13),
      wraplength=700, justify="left").pack(pady=10)

Button(grades_frame, text="Back", command=lambda: show_screen(main_menu_frame),
       bg="#FF5722", fg="white", font=("Helvetica", 12), width=12).pack(pady=20)

# Start with login screen
show_screen(login_frame)
project.mainloop()