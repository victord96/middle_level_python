def divisors(num):
    divisors = [x for x in range(1,num+1) if num % x == 0]
    return divisors


def run():
    num = input('Write a number: ')
    assert num.isnumeric(), 'Please, write a number'
    #assert int(num) > 0, 'Please enter a positive number'
    num = divisors(int(num))
    print (num)


if __name__ == '__main__':
    run()