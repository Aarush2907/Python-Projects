def load_file():
    credentials = {}

    try:
        with open('credentials.txt', 'r') as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue  # skip empty lines

                try:
                    site, user, pwd = line.split(' ', 2)
                    credentials[site] = [user, pwd]
                except ValueError:
                    print(f"Skipping corrupted line: {line}")

    except FileNotFoundError:
        return {}

    return credentials



def save_file(new_creds):
    with open('credentials.txt' , 'w') as file:
        for site in new_creds:
            user , pwd = new_creds[site]
            file.write(f"{site} {user} {pwd}\n")

credentials = load_file()

while(True):
    try:
        print("1. Add new password")
        print("2. Get password")
        print("3. View all sites")
        print("4. Exit")

        user_input = int(input("> Enter your choice "))

        if user_input == 1:
            website = input("Enter the website's name: ").strip()
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            if website in credentials:
                print("⚠️ Website already exists, updating it.")

            credentials[website] = [username,password]
            save_file(credentials)
            print("✅ Saved successfully")

        elif user_input == 2:
            sitename = input("Enter the site name for which you want your creds: ").strip()
            if sitename in credentials:
                user , pwd = credentials[sitename]
                print(f"Username: {user} | Password: {pwd}")
            else:
                print("❌ Site not found")

        elif user_input == 3:
            if not credentials:
                print("No saved credentials")
            else:
                for site, (user, pwd) in credentials.items():
                    print(f"{site} → {user} | {pwd}")
        elif user_input == 4:
            print("Exiting Bye")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter a valid number")

    except Exception as e:
        print("Error:", e)
    