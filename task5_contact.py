contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added!")

    elif choice == "2":
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print("Phone:", details["phone"])
            print("Email:", details["email"])

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print("Phone:", contacts[search]["phone"])
            print("Email:", contacts[search]["email"])
        else:
            print("Contact not found!")

    elif choice == "4":
        delete = input("Enter name to delete: ")
        if delete in contacts:
            del contacts[delete]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")