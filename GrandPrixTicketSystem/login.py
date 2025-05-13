import tkinter as tk
from tkinter import messagebox
from storage import load_data
from dashboard_admin import open_admin_dashboard
from dashboard_customer import open_customer_dashboard
from register import open_register_window

def open_login_window(root_window):
    root_window.destroy()

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("350x250")
    login_window.configure(bg="#fdf5e6")

    tk.Label(login_window, text="Login to your Account", font=("Helvetica", 14, "bold"), bg="#fdf5e6", fg="#333").pack(pady=15)

    tk.Label(login_window, text="Email:", bg="#fdf5e6").pack()
    entry_email = tk.Entry(login_window, width=30)
    entry_email.pack()

    tk.Label(login_window, text="Password:", bg="#fdf5e6").pack()
    entry_password = tk.Entry(login_window, show="*", width=30)
    entry_password.pack()

    def login():
        email = entry_email.get()
        password = entry_password.get()
        users = load_data("users.pkl")

        for user in users:
            if user.email == email and user.password == password:
                login_window.destroy()
                if user.__class__.__name__ == "Admin":
                    open_admin_dashboard(user)
                else:
                    open_customer_dashboard(user)
                return
        messagebox.showerror("Login Failed", "Invalid email or password.")

    tk.Button(login_window, text="Login", bg="#007acc", fg="white", font=("Helvetica", 12), command=login).pack(pady=10)

    tk.Label(login_window, text="Don't have an account?", bg="#fdf5e6").pack()
    tk.Button(login_window, text="Register", bg="#009966", fg="white", command=lambda: [login_window.destroy(), open_register_window(None)]).pack()

    login_window.mainloop()
