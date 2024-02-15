class SaveAndView:
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