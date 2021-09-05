def run():

    class Goku:

        def __init__(self):
            self.power = 1000
            self.defense = 2000
            self._ki = 10000

        @property
        def ki(self):
            return int(self._ki)

        @ki.setter
        def ki(self, n):
            self._ki = n

        @ki.deleter
        def ki(self):
            print('Deleting ki')
            del self._ki

        def super_saiyan(n):

            def war_declaration():
                print('I\'m going to destroy you Freezer!!')

            war_declaration()
            return f'AHHHHH! I\'m going to transform into super saiyan {n}'

        def kaioken(n):
            return f'¡kaito tecnique x{n}! ¡TRANSFORMATION!'

        def tecnique(input_function):
            return input_function("1")

    goku1 = Goku()

    print(Goku.tecnique(Goku.super_saiyan))
    print(Goku.tecnique(Goku.kaioken))

    goku1.ki = 8000
    print(goku1.ki)
    del goku1.ki


if __name__ == '__main__':
    run()
