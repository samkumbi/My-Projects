# App name   => Phone Book 
# Programmer => Sam Kumbi
# Date       => 12.27.2024

# App description
# ---------------
# This app allows the user to add contacts to a phone book.

# Variables
contacts_count = 0
phone_book     = []
user_input     = ''

# Displays welcome message and phone book table
print("\nWELCOME TO PHONE BOOK")
print("\nAdd a contact")

while (user_input != 'no'):
    if(user_input != 'no'):
        
        # Get full name and phone number
        first_name = input("First name: ")
        last_name  = input("Last name: ")
        ph_number  = input("Phone number: ")
        contact_info = first_name.ljust(20) + last_name.ljust(20) + ph_number.ljust(20)
        
        # Add contact to phone book
        phone_book.append(contact_info)
        print("\nContact added successfully!\n")

        user_input = input("Type any key to add another contact or 'no' to exit.\n > ")
        print()
        
        user_input.lower()

# Display contact list
print("You have " + str(len(phone_book)) + " contact(s)\n")
print("First name".ljust(20) + "Last name".ljust(20) + "Ph. Number".ljust(20))
print("--------------------------------------------------")
for contact in phone_book:
    print(''.join(contact))
print()