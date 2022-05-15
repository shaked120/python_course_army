import re
import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, invalid):
        self.username = username
        self.invalid = invalid

    def __str__(self):
        return " your username contains invalid characters please change it", self.invalid

    def get_username(self):
        return self.username

    def get_invalid(self):
        return self.invalid


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
    def __init__(self, password, missing_char):
        self.password = password
        self.missing_char = missing_char

    def __str__(self):
        return " your password does not contain at least one of the nust characters (", self.missing_char, ")"

    def get_password(self):
        return self.password

    def get_missing_char(self):
        return self.missing_char


class PasswordTooShort(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return " your password is too short, you need at least 8 characters "

    def get_password(self):
        return self.password


class PasswordTooLong(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return " your password is too long, you need less than 40 characters "

    def get_password(self):
        return self.password


def check_input(username, password):
    try:
        if '<' in username:
            raise UsernameContainsIllegalCharacter(username, '<')
        if '>' in username:
            raise UsernameContainsIllegalCharacter(username, '>')
        if '/' in username:
            raise UsernameContainsIllegalCharacter(username, '/')
        if '{' in username:
            raise UsernameContainsIllegalCharacter(username, '{')
        if '}' in username:
            raise UsernameContainsIllegalCharacter(username, '}')
        if '[' in username:
            raise UsernameContainsIllegalCharacter(username, '[')
        if '~' in username:
            raise UsernameContainsIllegalCharacter(username, '~')
        if ']' in username:
            raise UsernameContainsIllegalCharacter(username, ']')
        if '[' in username:
            raise UsernameContainsIllegalCharacter(username, '[')
        if '^' in username:
            raise UsernameContainsIllegalCharacter(username, '^')
        if len(username) < 3:
            raise UsernameTooShort(username)
        if len(username) > 16:
            raise UsernameTooLong(username)
        if not any(punc in string.punctuation for punc in password):
            raise PasswordMissingCharacter(password, (punc in string.punctuation for punc in password))
        if len(password) < 8:
            raise PasswordTooShort(password)
        if len(password) > 40:
            raise PasswordTooLong(password)
    except UsernameContainsIllegalCharacter as not_valid:
        print("username except only valid characters " % type(not_valid.get_username()))
    except UsernameTooShort as not_valid1:
        print("username too short " % type(not_valid1.get_username()))
    except UsernameTooLong as not_valid2:
        print("username too long " % type(not_valid2.get_username()))
    except PasswordMissingCharacter as not_valid3:
        print("password must at least one the have to characters" % type(not_valid3.get_password()))
    except PasswordTooShort as not_valid4:
        print("password too short " % type(not_valid4.get_password()))
    except PasswordTooLong as not_valid5:
        print("password too long " % type(not_valid5.get_password()))

    else:
        print("ok")


# if "_" in username or has_numbers(username) or any(upper.isupper() for upper in username) and (len(username) >= 3
#    or len(username) <=
#   16):
# if 8 <= len(password) <= 40 and any(big.isupper() for big in password) and \
# any(small.islower() for small in password) and has_numbers(password) and \
# any(punc in string.punctuation for punc in password):
# print("ok")
# else:
#  print("not valid")
# else:
# print("not valid")

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def main():
    check_input("1afghan_", "2seafoodsS!")


main()
