import random

def lineal_search(list, objective):
    match = False

    for element in list:
        if element == objective:
            match = True

    return match

if __name__ == '__main__':
    size_list = int(input('Size of the list?: '))
    objective = int(input('What number do you like to find?: '))

    list = [random.randint(0, 100) for i in range(size_list)]

    founded = lineal_search(list, objective)
    print(list)

    if founded:
        print('Element', objective, 'is on the list')
    else:
        print('Element', objective, 'not found on the list')