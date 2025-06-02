# contact_manager.py

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    """Loads contacts from the file."""
    contacts = []
    try:
        with open(CONTACTS_FILE, 'r') as f:
            for line in f:
                name, phone = line.strip().split(',')
                contacts.append({'name': name, 'phone': phone})
    except FileNotFoundError:
        pass # File doesn't exist yet, return empty list
    return contacts

def save_contacts(contacts):
    """Saves contacts to the file."""
    with open(CONTACTS_FILE, 'w') as f:
        for contact in contacts:
            f.write(f"{contact['name']},{contact['phone']}\n")

def add_contact(contacts):
    """Adds a new contact."""
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts.append({'name': name, 'phone': phone})
    save_contacts(contacts)
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    """Displays all contacts."""
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Your Contacts ---")
    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}")
    print("---------------------\n")


def delete_contact(contacts):
    """Deletes an existing contact."""
    view_contacts(contacts) # Show current contacts to help user choose
    if not contacts:
        return

    try:
        choice = int(input("Enter the number of the contact to delete: "))
        if 1 <= choice <= len(contacts):
            deleted_contact = contacts.pop(choice - 1)
            save_contacts(contacts)
    print(f"Contact '{deleted_contact['name']}' deleted.")
    else:
    print("Invalid contact number.")
    except ValueError:
    print("Invalid input. Please enter a number.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact") # New option
        print("4. Exit")         # Changed from 3 to 4
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3': # New handling
            delete_contact(contacts)
        elif choice == '4': # Changed from 3 to 4
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()