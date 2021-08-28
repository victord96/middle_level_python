def divisors(num):
    divisors = [x for x in range(1,num+1) if num % x == 0]
    return divisors


def run():
    try:
        num = int(input('Write a number: '))
        if num < 0:
            raise ValueError
        num = divisors(num)
        print (num)
    except ValueError:
        print('Please, Write a positive number')



if __name__ == '__main__':
    run()