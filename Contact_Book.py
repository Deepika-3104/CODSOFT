class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}, {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append(Contact(name, phone, email, address))

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        for contact in results:
            print(contact)

    def update_contact(self, old_phone, name=None, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact.phone == old_phone:
                contact.name = name or contact.name
                contact.phone = phone or contact.phone
                contact.email = email or contact.email
                contact.address = address or contact.address
                print("Contact updated.")
                return
        print("Contact not found.")

    def delete_contact(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)
                print("Contact deleted.")
                return
        print("Contact not found.")

def display_menu():
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    manager = ContactManager()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            manager.add_contact(name, phone, email, address)
            print("Contact added.")
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            old_phone = input("Enter the phone number of the contact to update: ")
            name = input("New Name (leave blank to keep unchanged): ")
            phone = input("New Phone (leave blank to keep unchanged): ")
            email = input("New Email (leave blank to keep unchanged): ")
            address = input("New Address (leave blank to keep unchanged): ")
            manager.update_contact(old_phone, name, phone, email, address)
        elif choice == '5':
            phone = input("Enter the phone number of the contact to delete: ")
            manager.delete_contact(phone)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
