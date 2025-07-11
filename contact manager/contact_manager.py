import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print("✅ Contact added!")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts available.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

# Edit contact
def edit_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]['name'] = input("Enter new name: ")
            contacts[index]['phone'] = input("Enter new phone number: ")
            contacts[index]['email'] = input("Enter new email: ")
            print("✏️ Contact updated!")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"🗑️ Contact '{removed['name']}' deleted.")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Main program
def main():
    contacts = load_contacts()
    while True:
        print("\n📒 Contact Manager Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("💾 Contacts saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number 1-5.")

if __name__ == "__main__":
    main()
