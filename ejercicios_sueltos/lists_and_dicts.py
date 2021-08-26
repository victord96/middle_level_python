def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict= {'firstname':'Victor', 'lastname':'García'}
    cont = 1

    super_list = [
        {'firstname':'Victor', 'lastname':'García'},
        {'firstname':'Miguel', 'lastname':'Torres'},
        {'firstname':'Pepe', 'lastname':'Rodelo'},
        {'firstname':'Susana', 'lastname':'Martinez'},
        {'firstname':'Jose', 'lastname':'García'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    for values in super_list:
        for key, value in values.items():
            print(f'{key}-{value}')


if __name__ == '__main__':
    run()