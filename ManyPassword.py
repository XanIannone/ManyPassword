import random
from modules.data.art import logo
from modules.classes import Generator, SaveView

password_generator = Generator()
password_saveview = SaveView()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(logo)


def save_passwords(password_list):
    from modules.data.Saved_Passwords import saved
    reader = open(r'modules\data\Saved_Passwords.py', 'w')
    for password in password_list:
        saved[password] = password_list[password]
    reader.write(f"saved = {saved}")
    reader.close()


continue_running = True
while continue_running:
    # program start
    selected_mode = input("""
Generate New Passwords || View Saved Passwords || Save New Passwords
                        (Enter 1/2/3)

                            """)
    if selected_mode == "1":
        # password generation mode
        session_password_dict = {}

        continue_creating = True
        while continue_creating:
            password_generator.create_password()
            session_password_dict[password_generator.use_case] = password_generator.generated_password

            if input("Would you like to generate another password? (Yes/No):\n").lower() == "no":
                continue_creating = False

        if len(session_password_dict) > 1:
            print("\nYour password list for this session:")
            for password in session_password_dict:
                print(f"{password}: {session_password_dict[password]}")

        if input("\nWould you like to run the program again? (Yes/No):\n").lower() == "no":
            continue_running = False
        # saving passwords
        save_passwords(session_password_dict)

    elif selected_mode == "2":
        # View Password Mode
        from modules.data.Saved_Passwords import saved

        for password in saved:
            print(f"{password}: {saved[password]}\n")
        if len(saved) > 0:
            if input("Would you like to wipe your passwords? (Yes/No): ").lower() == "yes":
                reader = open(r'modules\data\Saved_Passwords.py', 'w')
                reader.write("saved = {}")
                reader.close()
                print("Your password list has been wiped.")
        else:
            print("You have no saved passwords to view.")

        if input("\nWould you like to run the program again? (Yes/No):\n").lower() == "no":
            continue_running = False

    elif selected_mode == "3":
        # Save Password Mode
        session_password_dict = {}

        continue_creating = True
        while continue_creating:
            use_case = input("What website/application are you using this password for?\n")
            password = input("Enter your password:\n")
            session_password_dict[use_case] = password
            print(f"Your password has been saved")
            if input("Would you like to save another password? (Yes/No):\n").lower() == "no":
                continue_creating = False
        save_passwords(session_password_dict)
        if input("\nWould you like to run the program again? (Yes/No):\n").lower() == "no":
            continue_running = False