import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Form")
root.geometry("400x400")
root.configure(bg="#f0f2f5")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="USER LOGIN",
    font=("Arial", 22, "bold"),
    bg="#f0f2f5",
    fg="#2563eb"
)
title_label.pack(pady=20)

username_label = tk.Label(
    root,
    text="Username",
    font=("Arial", 11),
    bg="#f0f2f5",
    fg="black"
)
username_label.pack(pady=5)

username_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)
username_entry.pack(pady=5, ipady=5)

password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 11),
    bg="#f0f2f5",
    fg="black"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    show="•"
)
password_entry.pack(pady=5, ipady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Missing Information",
            "Please enter your username and password.")
        return

    if username == "admin" and password == "12345":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid username or password!"
        )

login_button = tk.Button(
    root,
    text="LOG IN",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    width=20,
    relief="flat",
    cursor="hand2",
    command=login
)
login_button.pack(pady=20, ipady=5)

root.mainloop()