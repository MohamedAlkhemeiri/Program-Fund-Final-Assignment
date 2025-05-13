import tkinter as tk
from tkinter import messagebox
from storage import load_data, save_data
from models import Admin, Customer, Order

def open_admin_dashboard(admin_user):
    window = tk.Tk()
    window.title("Admin Dashboard")
    window.geometry("700x600")
    window.configure(bg="#f2f9ff")

    # Header
    tk.Label(window, text=f"Admin Panel - {admin_user.username}", font=("Helvetica", 16, "bold"), bg="#f2f9ff", fg="#003366").pack(pady=10)

    # Section: Ticket Sales
    frame_sales = tk.LabelFrame(window, text="🎟️ Ticket Sales Summary", bg="#f2f9ff", font=("Helvetica", 12, "bold"))
    frame_sales.pack(fill="x", padx=20, pady=10)

    orders = load_data("orders.pkl")
    sales_summary = admin_user.view_ticket_sales(orders)

    if sales_summary:
        for ttype, count in sales_summary.items():
            tk.Label(frame_sales, text=f"{ttype}: {count} sold", bg="#f2f9ff").pack(anchor="w", padx=10)
    else:
        tk.Label(frame_sales, text="No tickets sold yet.", bg="#f2f9ff").pack(anchor="w", padx=10)

    # Section: Apply Discount
    frame_discount = tk.LabelFrame(window, text="💸 Apply Discount to All Tickets", bg="#f2f9ff", font=("Helvetica", 12, "bold"))
    frame_discount.pack(fill="x", padx=20, pady=10)

    tk.Label(frame_discount, text="Discount (%):", bg="#f2f9ff").pack(pady=5)
    discount_entry = tk.Entry(frame_discount)
    discount_entry.pack()

    def apply_discount():
        try:
            discount = float(discount_entry.get())
            if not (0 <= discount <= 100):
                raise ValueError
            tickets = load_data("tickets.pkl")
            admin_user.update_discounts(tickets, discount)
            save_data("tickets.pkl", tickets)
            messagebox.showinfo("Success", f"{discount}% discount applied to all tickets.")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid discount between 0 and 100.")

    tk.Button(frame_discount, text="Apply", bg="#007acc", fg="white", command=apply_discount).pack(pady=5)

    # Section: Customer Management
    frame_users = tk.LabelFrame(window, text="👤 Manage Customers", bg="#f2f9ff", font=("Helvetica", 12, "bold"))
    frame_users.pack(fill="x", padx=20, pady=10)

    def refresh_users():
        for widget in frame_users.winfo_children()[1:]:
            widget.destroy()
        users = load_data("users.pkl")
        for u in users:
            if isinstance(u, Customer):
                row = tk.Frame(frame_users, bg="#f2f9ff")
                row.pack(fill="x", pady=2)
                tk.Label(row, text=f"{u.username} | {u.email}", bg="#f2f9ff").pack(side="left", padx=5)
                tk.Button(row, text="Edit", command=lambda user=u: edit_user(user)).pack(side="right", padx=2)
                tk.Button(row, text="Delete", command=lambda user=u: delete_user(user)).pack(side="right", padx=2)

    def delete_user(user):
        users = load_data("users.pkl")
        users = [u for u in users if u.email != user.email]
        save_data("users.pkl", users)
        messagebox.showinfo("Deleted", f"User '{user.username}' deleted.")
        refresh_users()

    def edit_user(user):
        popup = tk.Toplevel(window)
        popup.title("Edit User")
        popup.geometry("300x200")
        tk.Label(popup, text="Email").pack()
        email_entry = tk.Entry(popup)
        email_entry.insert(0, user.email)
        email_entry.pack()

        tk.Label(popup, text="Password").pack()
        pass_entry = tk.Entry(popup, show="*")
        pass_entry.insert(0, user.password)
        pass_entry.pack()

        def save_changes():
            user.email = email_entry.get()
            user.password = pass_entry.get()
            users = load_data("users.pkl")
            save_data("users.pkl", users)
            messagebox.showinfo("Updated", "User info updated.")
            popup.destroy()
            refresh_users()

        tk.Button(popup, text="Save", bg="#28a745", fg="white", command=save_changes).pack(pady=10)

    refresh_users()

    # Section: Order Management
    frame_orders = tk.LabelFrame(window, text="📦 Purchase Orders", bg="#f2f9ff", font=("Helvetica", 12, "bold"))
    frame_orders.pack(fill="both", expand=True, padx=20, pady=10)

    def refresh_orders():
        for widget in frame_orders.winfo_children()[1:]:
            widget.destroy()
        orders = load_data("orders.pkl")
        if not orders:
            tk.Label(frame_orders, text="No orders found.", bg="#f2f9ff").pack()
            return
        for order in orders:
            frame = tk.Frame(frame_orders, bg="#f2f9ff")
            frame.pack(fill="x", pady=2)
            info = f"{order.order_id[:8]} | {order.customer.username} | ${order.total_price:.2f} | {order.purchase_date.strftime('%Y-%m-%d')}"
            tk.Label(frame, text=info, bg="#f2f9ff").pack(side="left", padx=5)
            tk.Button(frame, text="Delete", command=lambda o=order: delete_order(o)).pack(side="right", padx=5)

    def delete_order(order_to_delete):
        orders = load_data("orders.pkl")
        orders = [o for o in orders if o.order_id != order_to_delete.order_id]
        save_data("orders.pkl", orders)
        messagebox.showinfo("Deleted", "Order deleted.")
        refresh_orders()

    refresh_orders()

    # Logout Button
    tk.Button(window, text="Logout", bg="#cc0000", fg="white", command=lambda: [window.destroy()]).pack(pady=10)

    window.mainloop()
