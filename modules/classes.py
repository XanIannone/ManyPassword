class Generator:
    def scramble_password(self, unscrambled_string):
        import random
        string = list(unscrambled_string)
        random.shuffle(string)
        return ''.join(string)

class SaveView:
    def view_passwords(self):
        from data.Saved_Passwords import saved
        for password in saved:
            print(f"{password}: {saved[password]}\n")
    def save_passwords(self, password_list):
        global password
        global reader
        from data.Saved_Passwords import saved
        reader = open('Saved_Passwords.py', 'w')
        for password in password_list:
            saved[password] = password_list[password]
        reader.write(f"saved = {saved}")
        reader.close()