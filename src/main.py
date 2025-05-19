def main_menu():
    """Display the main menu and handle user input."""
    print("\n--- Main Menu ---")
    print("1. Account Info")
    print("2. Services")
    print("0. Exit")
    choice = input("Select an option: ")
    if choice == "1":
        account_info_menu()
    elif choice == "2":
        services_menu()
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice.")
        main_menu()


def account_info_menu():
    """Display the account information menu and handle user input."""
    print("\n--- Account Info ---")
    print("1. Balance")
    print("2. Data Usage")
    print("9. Back")
    print("0. Main Menu")
    choice = input("Select an option: ")
    if choice == "1":
        print("Your balance is 100Ar.")
        account_info_menu()
    elif choice == "2":
        print("You have used 500Mo.")
        account_info_menu()
    elif choice == "9":
        main_menu()
    elif choice == "0":
        main_menu()
    else:
        print("Invalid choice.")
        account_info_menu()


def services_menu():
    """Display the services menu and handle user input."""
    print("\n--- Services ---")
    print("1. Buy Data")
    print("2. Buy Airtime")
    print("9. Back")
    print("0. Main Menu")
    choice = input("Select an option: ")
    if choice == "1":
        print("Data purchased!")
        services_menu()
    elif choice == "2":
        print("Airtime purchased!")
        services_menu()
    elif choice == "9":
        main_menu()
    elif choice == "0":
        main_menu()
    else:
        print("Invalid choice.")
        services_menu()


if __name__ == "__main__":
    main_menu()
