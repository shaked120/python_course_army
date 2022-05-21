class IDIterator:
    def __init__(self, Id):
        self.Id = Id
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.Id == 999999999:
            raise StopIteration
        for i in range(self.Id, 999999999):
            if check_id_valid(self.Id + self.index):
                self.index += 1
                return self.Id + self.index - 1
            self.index += 1


def id_generator(id_number):
    prime_generator = (i for i in range(id_number, 999999999) if check_id_valid(i))
    return prime_generator


def check_id_valid(id_number):
    counter = 0
    id_list = [int(x) for x in str(id_number)]
    for i in range(len(id_list)):
        if i % 2 != 0:
            id_list[i] = id_list[i] * 2
            if id_list[i] > 9:
                id_list[i] = id_list[i] % 10 + id_list[i] // 10
        counter += id_list[i]
    if counter % 10 == 0:
        return True
    else:
        return False


def main():
    print(check_id_valid(123456780))
    print(check_id_valid(123456782))
    id1 = int(input("please enter an id:"))
    iterator_or_gen = input("if you want to create the id from iterator enter it else enter gen:")
    id_iter = IDIterator(id1)
    gen = id_generator(id1)
    if iterator_or_gen == "it":
        for i in range(10):
            print(next(id_iter))
    else:
        for i in range(10):
            print(next(gen))


main()
