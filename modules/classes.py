class Generator:
    def __init__(self):
        Generator.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v',
                   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                   'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        Generator.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        Generator.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def create_password(self):
        import random
        Generator.use_case = input("What website/application are you using this password for?\n")

        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))

        selected_letters = ""
        selected_numbers = ""
        selected_symbols = ""

        for n in range(1, nr_letters + 1):
            selected_letters += (Generator.letters[random.randint(0, len(Generator.letters) - 1)])
        for n in range(1, nr_numbers + 1):
            selected_numbers += (Generator.numbers[random.randint(0, len(Generator.numbers) - 1)])
        for n in range(1, nr_symbols + 1):
            selected_symbols += (Generator.symbols[random.randint(0, len(Generator.symbols) - 1)])


        combined_string = (selected_letters + selected_numbers + selected_symbols)
        shuffled_string = list(combined_string)
        random.shuffle(shuffled_string)
        Generator.generated_password = ''.join(shuffled_string)
        print(f"\nYour randomly generated password for {Generator.use_case}: {Generator.generated_password}")


class Save:
    def save_passwords(self, password_list):
        from modules.data.Saved_Passwords import saved
        reader = open(r'modules\data\Saved_Passwords.py', 'w')
        for password in password_list:
            saved[password] = password_list[password]
        reader.write(f"saved = {saved}")
        reader.close()


class View:
    def view_passwords(self):
        from data.Saved_Passwords import saved
        for password in saved:
            print(f"{password}: {saved[password]}\n")
