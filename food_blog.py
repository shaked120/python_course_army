import string


class UsernameContainsIllegalCharacter (Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return " your username contains invalid characters please change it"

    def get_username(self):
        return self.username


class UsernameTooShort(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return " your user name is too short, you need more than 3 characters"

    def get_username(self):
        return self.username


class UsernameTooLong(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return " your user name is too long, you need less than 16 characters"

    def get_username(self):
        return self.username


class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return " your password does not contain at least one of the nust characters "

    def get_password(self):
        return self.password


class PasswordTooShort(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return " your password is too short, you need at least 8 characters "

    def get_password(self):
        return self.password


class PasswordTooLong (Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return " your password is too long, you need less than 40 characters "

    def get_password(self):
        return self.password


def check_input(username, password):
    if "_" in username or has_numbers(username) or any(upper.isupper() for upper in username) and (len(username) >= 3
                                                                                                   or len(username) <=
                                                                                                   16):
        if 8 <= len(password) <= 40 and any(big.isupper() for big in password) and \
                any(small.islower() for small in password) and has_numbers(password) and \
                any(punc in string.punctuation for punc in password):
            print("ok")
        else:
            print("not valid")
    else:
        print("not valid")


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def main():
    check_input("ofir12", "Dh4!asdfc")


main()


