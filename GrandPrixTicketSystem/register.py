import tkinter as tk
from tkinter import messagebox
from models import Customer
from storage import load_data, save_data

def open_register_window(root_window=None):
    if root_window:
        root_window.destroy()

    reg_window = tk.Tk()
    reg_window.title("Register")
    reg_window.geometry("350x300")
    reg_window.configure(bg="#eafbea")

    tk.Label(reg_window, text="Create Your Account", font=("Helvetica", 14, "bold"), bg="#eafbea").pack(pady=10)

    tk.Label(reg_window, text="Username", bg="#eafbea").pack()
    entry_username = tk.Entry(reg_window)
    entry_username.pack()

    tk.Label(reg_window, text="Email", bg="#eafbea").pack()
    entry_email = tk.Entry(reg_window)
    entry_email.pack()

    tk.Label(reg_window, text="Password", bg="#eafbea").pack()
    entry_password = tk.Entry(reg_window, show="*")
    entry_password.pack()

    def register():
        username = entry_username.get()
        email = entry_email.get()
        password = entry_password.get()

        if not username or not email or not password:
            messagebox.showerror("Error", "All fields are required.")
            return

        users = load_data("users.pkl")
        for u in users:
            if u.email == email:
                messagebox.showerror("Error", "Email already registered.")
                return

        new_user = Customer(username, email, password)
        users.append(new_user)
        save_data("users.pkl", users)
        messagebox.showinfo("Success", "Registration complete!")
        reg_window.destroy()

    tk.Button(reg_window, text="Register", bg="#009966", fg="white", command=register).pack(pady=10)

    reg_window.mainloop()
