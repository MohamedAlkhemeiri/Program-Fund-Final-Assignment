from models import Customer, Admin, Ticket, Order
from storage import save_data, load_data

def test_user_creation():
    user = Customer("test_user", "test@example.com", "secure123")
    assert user.username == "test_user"
    assert user.email == "test@example.com"
    print("Customer creation test passed.")

def test_order_creation():
    customer = Customer("john", "john@example.com", "pass")
    ticket = Ticket("Single-Race", 100, "One day", "Basic access")
    order = Order(customer, [ticket])
    assert order.total_price == 100
    assert len(order.tickets) == 1
    print("Order creation test passed.")

def test_admin_sales_summary():
    admin = Admin("admin", "admin@example.com", "adminpass")
    customer = Customer("jane", "jane@example.com", "pass")
    tickets = [
        Ticket("Single-Race", 100, "One day", "Basic access"),
        Ticket("Weekend", 200, "3 days", "All events")
    ]
    order1 = Order(customer, [tickets[0]])
    order2 = Order(customer, [tickets[1]])
    summary = admin.view_ticket_sales([order1, order2])
    assert summary["Single-Race"] == 1
    assert summary["Weekend"] == 1
    print("Admin ticket sales summary test passed.")

def run_all_tests():
    test_user_creation()
    test_order_creation()
    test_admin_sales_summary()

if __name__ == "__main__":
    run_all_tests()
