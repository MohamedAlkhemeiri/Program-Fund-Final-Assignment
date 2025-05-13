import uuid
from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Customer(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.purchase_history = []

    def view_purchase_history(self):
        return self.purchase_history

    def update_account_info(self, email=None, password=None):
        if email:
            self.email = email
        if password:
            self.password = password

class Admin(User):
    def view_ticket_sales(self, orders):
        sales_summary = {}
        for order in orders:
            for ticket in order.tickets:
                sales_summary[ticket.ticket_type] = sales_summary.get(ticket.ticket_type, 0) + 1
        return sales_summary

    def update_discounts(self, tickets, discount):
        for ticket in tickets:
            ticket.price -= ticket.price * (discount / 100)

class Ticket:
    def __init__(self, ticket_type, price, validity, features):
        self.ticket_id = str(uuid.uuid4())
        self.ticket_type = ticket_type
        self.price = price
        self.validity = validity
        self.features = features

class Order:
    def __init__(self, customer, tickets):
        self.order_id = str(uuid.uuid4())
        self.customer = customer
        self.tickets = tickets
        self.total_price = self.calculate_total()
        self.purchase_date = datetime.now()

    def calculate_total(self):
        return sum(ticket.price for ticket in self.tickets)