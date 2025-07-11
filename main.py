from manager import save_password, get_password

def main():
    print("=== Password Manager ===")

    while True:
        print("\n1. Save new password")
        print("2. Retrieve password")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            service = input("Service Name (e.g., Gmail, Facebook): ")
            username = input("Username/Email: ")
            password = input("Password: ")
            save_password(service, username, password)
            print(f"Password for '{service}' saved successfully!")

        elif choice == "2":
            service = input("Enter Service Name to retrieve password: ")
            username, password = get_password(service)
            if username:
                print(f"\n✅ Username: {username}\n🔑 Password: {password}")
            else:
                print("❌ No password found for this service.")

        elif choice == "3":
            print("🔒 Exiting Password Manager.")
            break

        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
