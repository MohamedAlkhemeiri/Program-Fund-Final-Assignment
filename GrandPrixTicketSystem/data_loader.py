from models import Ticket
from storage import save_data
import uuid

def generate_sample_tickets():
    tickets = [
        Ticket(ticket_type="Single-Race Pass", price=50.0, validity="1 Day", features="Access to all areas for one race"),
        Ticket(ticket_type="Weekend Package", price=120.0, validity="3 Days", features="All-access for the weekend"),
        Ticket(ticket_type="VIP Experience", price=250.0, validity="3 Days", features="VIP Access with premium seating"),
        Ticket(ticket_type="Group Discount", price=200.0, validity="1 Day", features="Discounted rate for groups of 5 or more")
    ]
    # Save tickets to the tickets.pkl file
    save_data("tickets.pkl", tickets)
    print("Sample tickets added successfully.")

if __name__ == "__main__":
    generate_sample_tickets()
