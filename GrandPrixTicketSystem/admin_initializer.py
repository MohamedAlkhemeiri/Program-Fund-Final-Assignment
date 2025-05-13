# admin_initializer.py

import os
from storage import load_data, save_data
from models import Admin, Customer

def create_admin_account():
    # Check if the users file exists and is empty
    users_file = os.path.join("data", "users.pkl")
    if not os.path.exists(users_file) or os.path.getsize(users_file) == 0:
        print("Creating default admin account...")
        
        # Create default admin credentials
        admin_email = "admin@grandprix.com"
        admin_password = "admin1234"
        admin_username = "Admin"

        # Create and save admin user
        admin = Admin(admin_username, admin_email, admin_password)
        users = [admin]  # Start with the admin user
        
        # Save the user list to the file
        save_data("users.pkl", users)
        print("Admin account created successfully.")
    else:
        print("Admin account already exists.")

if __name__ == "__main__":
    create_admin_account()
