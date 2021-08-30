def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)        


def write():
    names = ['Facundo', 'Miguel', 'Eduardo']
    with open('./files/numbers.txt', 'w', encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    write()


if __name__ == '__main__':
    run()