def divisors(num):
    divisors = [x for x in range(1,num+1) if num % x == 0]
    return divisors


def run():
    num = int(input('Ingresa un numero: '))
    num = divisors(num)
    print (num)
    print('Termino mi programa')


if __name__ == '__main__':
    run()