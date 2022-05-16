import datetime


def gen_secs():
    for n in range(0, 60):
        yield n


def gen_minutes():
    for n in range(0, 60):
        yield n


def gen_hours():
    for n in range(0, 24):
        yield n


def gen_years(start=2019):
    while True:
        start += 1
        yield start


def gen_months():
    for n in range(1, 13):
        yield n


def gen_days(month, leap_year=True):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        yield 31
    if leap_year:
        yield 29
    else:
        yield 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        yield 30


def gen_date():
    gen = gen_time()
    gen1 = gen_days(2019)
    while True:
        time = next(gen)
        gen2 = gen_months()
        days = next(gen1)
        while True:
            gen3 = gen_years()
            months = next(gen2)
            while True:
                years = next(gen3)
                t = datetime.date(years, months, days)
                yield t, time


def gen_time():
    gen1 = gen_hours()
    for i in range(24):
        gen2 = gen_minutes()
        hour = next(gen1)
        for n in range(60):
            gen3 = gen_secs()
            minutes = next(gen2)
            for j in range(60):
                seconds = next(gen3)
                t = datetime.time(hour, minutes, seconds)
                yield t


def main():
    date = gen_date()
    day = gen_days(1)
    month = gen_months()
    year = gen_years(2077)
    hours = gen_hours()
    sec = gen_secs()
    minutes = gen_minutes()
    for i in sec:
        print(i)
    for j in minutes:
        print(j)
    for k in hours:
        print(k)
    print("------------------")
    for gt in gen_time():
        print(gt)
    print("------------------")
    print(next(year))
    print(next(year))
    print(next(month))
    print(next(month))
    print(next(day))
    print("-----------------")
    print(next(date))
    print(next(date))
    for i in range(0, True, 1000000):
        print(next(date))


main()
