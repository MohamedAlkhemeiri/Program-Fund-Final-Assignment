import tkinter as tk
from tkinter import messagebox
from models import Ticket, Order
from storage import load_data, save_data
from style import apply_style, style_button, style_label

def open_customer_dashboard(customer):
    window = tk.Tk()
    window.title(f"Customer Dashboard - {customer.username}")
    window.geometry("700x600")
    window.configure(bg="#f5fcff")

    apply_style(window)

    # Header
    style_label(window, f"Welcome, {customer.username}", size=16, weight="bold", fg="#003366").pack(pady=10)

    # Load tickets and orders
    tickets = load_data("tickets.pkl")
    orders = load_data("orders.pkl")

    # Section: Ticket selection
    ticket_frame = tk.LabelFrame(window, text="Available Tickets", bg="#f5fcff", font=("Helvetica", 12, "bold"))
    ticket_frame.pack(fill="x", padx=20, pady=10)

    ticket_var = tk.StringVar(value="")
    for ticket in tickets:
        tk.Radiobutton(
            ticket_frame,
            text=f"{ticket.ticket_type} - ${ticket.price:.2f} | {ticket.validity} | {ticket.features}",
            variable=ticket_var,
            value=ticket.ticket_id,
            bg="#f5fcff",
            anchor="w"
        ).pack(fill="x", padx=10, pady=2)

    def purchase_ticket():
        selected_id = ticket_var.get()
        selected_ticket = next((t for t in tickets if t.ticket_id == selected_id), None)
        if not selected_ticket:
            messagebox.showwarning("No Selection", "Please select a ticket.")
            return
        new_order = Order(customer, [selected_ticket])
        orders.append(new_order)
        customer.purchase_history.append(new_order)
        save_data("orders.pkl", orders)

        # update the user in users.pkl
        users = load_data("users.pkl")
        for i, u in enumerate(users):
            if u.email == customer.email:
                users[i] = customer
                break
        save_data("users.pkl", users)
        messagebox.showinfo("Success", "Ticket purchased successfully!")

    style_button(window, "Purchase Selected Ticket", purchase_ticket).pack(pady=10)

    # Section: Purchase history
    def show_history():
        history = customer.view_purchase_history()
        history_window = tk.Toplevel(window)
        history_window.title("Purchase History")
        history_window.geometry("500x300")
        apply_style(history_window)

        if not history:
            style_label(history_window, "No previous purchases found.").pack(pady=20)
            return

        for order in history:
            text = f"{order.order_id[:8]} | ${order.total_price:.2f} | {order.purchase_date.strftime('%Y-%m-%d')}"
            tk.Label(history_window, text=text, bg="#f5fcff").pack(anchor="w", padx=10)

    style_button(window, "View Purchase History", show_history).pack(pady=5)

    # Section: Update account info
    def update_info():
        update_window = tk.Toplevel(window)
        update_window.title("Update Account Info")
        update_window.geometry("300x200")
        apply_style(update_window)

        tk.Label(update_window, text="New Email", bg="#f5fcff").pack()
        entry_email = tk.Entry(update_window)
        entry_email.insert(0, customer.email)
        entry_email.pack()

        tk.Label(update_window, text="New Password", bg="#f5fcff").pack()
        entry_pass = tk.Entry(update_window, show="*")
        entry_pass.insert(0, customer.password)
        entry_pass.pack()

        def save_changes():
            customer.update_account_info(entry_email.get(), entry_pass.get())
            users = load_data("users.pkl")
            for i, u in enumerate(users):
                if u.email == customer.email:
                    users[i] = customer
                    break
            save_data("users.pkl", users)
            messagebox.showinfo("Updated", "Account info updated.")
            update_window.destroy()

        style_button(update_window, "Save Changes", save_changes).pack(pady=10)

    style_button(window, "Update Account Info", update_info).pack(pady=10)

    tk.Button(window, text="Logout", bg="#cc0000", fg="white", command=lambda: [window.destroy()]).pack(pady=10)

    window.mainloop()
