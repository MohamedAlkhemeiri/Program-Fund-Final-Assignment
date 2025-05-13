import os
import sys
from admin_initializer import create_admin_account
from data_loader import generate_sample_tickets
from main import main_menu

def reset_data():
    """Reset all data (users and tickets)."""
    if os.path.exists("data"):
        # Clear existing data
        for file in os.listdir("data"):
            os.remove(os.path.join("data", file))
        print("Data reset successfully.")
    else:
        print("No data directory found.")

def boot_app():
    """Boot the app after ensuring that the data is initialized."""
    # Ensure admin account exists
    create_admin_account()

    # Ensure tickets exist (if not already there)
    if not os.path.exists(os.path.join("data", "tickets.pkl")):
        generate_sample_tickets()

    # Run the main menu
    main_menu()

if __name__ == "__main__":
    # Check if the user wants to reset the data
    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        reset_data()
    else:
        boot_app()
