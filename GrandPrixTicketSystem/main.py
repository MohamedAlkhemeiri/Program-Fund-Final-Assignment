import tkinter as tk
from login import open_login_window
from register import open_register_window

def main_menu():
    root = tk.Tk()
    root.title("Grand Prix Experience")
    root.geometry("400x300")
    root.configure(bg="#e6f2ff")

    tk.Label(root, text="🏁 Grand Prix Ticket System 🏁", font=("Helvetica", 16, "bold"), bg="#e6f2ff", fg="#003366").pack(pady=20)

    tk.Button(root, text="Login", width=25, height=2, bg="#007acc", fg="white", font=("Helvetica", 12),
              command=lambda: open_login_window(root)).pack(pady=10)

    tk.Button(root, text="Register", width=25, height=2, bg="#009966", fg="white", font=("Helvetica", 12),
              command=lambda: open_register_window(root)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
