# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections
import functools
import types
from itertools import combinations
import random
import winsound
import itertools


class MusicNotes:
    def __init__(self):
        self.index = -1
        self.la = 66
        self.si = 61.74
        self.do = 65.41
        self.re = 73.42
        self.mi = 82.41
        self.fa = 87.31
        self.sol = 98
        self.list = [[self.la, self.la * 2, self.la * 4, self.la * 8, self.la * 16],
                     [self.si, self.si * 2, self.si * 4, self.si * 8, self.si * 16],
                     [ self.do, self.do * 2, self.do * 4, self.do * 8, self.do * 16],
                     [self.re, self.re * 2, self.re * 4, self.re * 8, self.re * 16],
                     [self.mi, self.mi * 2, self.mi * 4, self.mi * 8, self.mi * 16],
                     [self.fa, self.fa * 2, self.fa * 4, self.fa * 8, self.fa * 16],
                     [self.sol, self.sol * 2, self.sol * 4, self.sol * 8, self.sol * 16]]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list) -1:
            raise StopIteration
        self.index += 1
        return self.list[self.index]


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)


class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_name(self):
        return self.name


class EmployeeManger:
    def __init__(self):
        self.employee_list = []
        self.eml_index = -1

    def add_employee(self, new_empl):
        self.employee_list.append(new_empl)

    def __iter__(self):
        return self

    def __next__(self):
        if self.eml_index >= len(self.employee_list) -1:
            raise StopIteration()

        self.eml_index += 1
        return self.employee_list[self.eml_index].get_name()


hr_manager = EmployeeManger()
hr_manager.add_employee(employee("lia levi", 30, 20000))
hr_manager.add_employee(employee("yosef cohen", 32, 4000))
hr_manager.add_employee(employee("oded haim", 47, 5100))

for emp_name in hr_manager:
    print(emp_name)


gen5 = (x ** 2 for x in [1, 2, 3])
print(dir(gen5))


class UnderAge(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return " your age is under 18. you can come in %s years" + str(18 - self.age)

    def get_age(self):
        return self.age


class FactorialArgumentError(Exception):

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "provided argument %s us not a positive integer." % self.arg

    def get_arg(self):
        return self.arg


def add(a, b):
    return a + b


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
    return str1 + str1


def secret(a):
    return a % 3 != 0 and a % 5 != 0


result = filter(secret, range(1, 31))
print(list(result))


def double_letter(my_str):
    return str(map(double_letter1, my_str))


def four_dividers(number):
    return list(filter(dividers_to_number, range(1, number + 1)))


def sum_of_digits(number):
    return functools.reduce(add, range(1, number + 1))


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

number_1 = int(input("enter first number:"))
number_2 = int(input("enter second number:"))
try:
    print(" the result is: " + str(number_1 / number_2))

except ZeroDivisionError as e:
    print("cannot divide the provided input.")

except ValueError:
    print("invalid input was provided, please provide integers only! ")


def read_file(file_name):
    print("__CONTENT_START__")
    try:
        output = open(file_name, "r")
        object_file = output.read().split()
        print(object_file)
    except FileNotFoundError:
        print("__NO_SUCH_FILE__")
    finally:
        print("__CONTENT_END__")


def factorial(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise FactorialArgumentError(n)
    except FactorialArgumentError as e:
        print("Function Expected positive integer, and instead got %s. " % type(e.get_arg()))

    else:
        fact = 1
        for i in range(n, 0, -1):
            fact = fact * i
        return fact


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print("under age" % type(e.get_age()))
    else:
        print("You should send an invite to " + name)


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def translate(str1):
    word1 = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    str2 = list(str1.split())
    gen = (n for n in str2)
    for i in range(len(str2)):
        print(word1.get(next(gen)))


def first_prime_over(n):
    prime_generator = (i for i in range(n, n ** n) if is_prime(i))
    print(next(prime_generator))


def parse_ranges(ranges_string):
    list2 = list(ranges_string.split(","))
    print(list2)
    gen = (n for n in list2 if n != ',')
    for i in gen:
        gen1 = (num for num in range(int(i[0]), int(i[2]) + 1))
        return gen1


cube_game = (random.randint(1, 6) for i in range(4))


def get_fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    read_file("sg.txt")
    print(factorial(4))
    send_invitation("ofir", 20)
    print(translate("el gato esta en la casa"))
    print(first_prime_over(1000000))
    gen = (i / 2 for i in [0, 9, 21, 32])
    print(next(gen))
    print(next(gen))

    total = 0
    for num in cube_game:
        total += num
    print(total)

    for permutation in itertools.permutations([0, 5, 6, 9]):
        print(permutation)
    print(parse_ranges("1-2,4-4,8-10"))
    print("----------")
    fibo_gen = get_fibo(5)
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print("----------------")
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }

    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    song = notes.split("-")
    iter_song = song.__iter__()
    for i in range(len(song)):
        yon = next(iter_song).split(",")
        winsound.Beep(freqs.get(yon[0]), int(yon[1]))

    numbers = iter(list(range(1, 101, 3)))
    for i in numbers:
        print(i)
    print("------------")


main()
