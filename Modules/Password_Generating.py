class Generator:
    def scramble_password(self, unscrambled_string):
        import random
        string = list(unscrambled_string)
        random.shuffle(string)
        return ''.join(string)