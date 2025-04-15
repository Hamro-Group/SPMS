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