phonebook = {}

while True:
    print("\n--- Phonebook ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Show all contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print(name, "added.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phonebook:
            print(name, ":", phonebook[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(name, "deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        if phonebook:
            for name, phone in phonebook.items():
                print(name, ":", phone)
        else:
            print("Phonebook is empty.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
