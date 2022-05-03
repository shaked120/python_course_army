# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import functools


def add(a, b):
    return a+b


def combine_coins(coin, numbers):
    output = ""
    for i in numbers:
        output += coin + str(i) + ','
    return output[0:len(output) - 1]


def dividers_to_number(number):
    if number % 4 == 0:
        return True
    else:
        return False


def double_letter1(str1):
    return str1+str1


def secret(a):
    return a % 3 != 0 and a % 5 != 0


result = filter(secret, range(1, 31))
print(list(result))


def double_letter(my_str):
    return str(map(double_letter1, my_str))


def four_dividers(number):
    return list(filter(dividers_to_number, range(1, number+1)))


def sum_of_digits(number):
    return functools.reduce(add, range(1, number+1))


print(sum_of_digits(8))


def function(num, item):
    return num + 1


password = input("Enter Your password (integers only): ")
lst = list(map(int, password))
magic = functools.reduce(function, lst)
result = (lambda x: x % 4 == 0)(magic)
if result:
    print("Correct password!")
else:
    print("Wrong password.")

sentence = "the quick brown fox"
words = sentence.split()
secret1 = [word[0] for word in words if word != "the"]
print(secret1)








