class Washing_Machine:

    def __init__(self):
        pass
    
    def wash(self, temperature='hot'):
        self._fill_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _fill_tank(self, temperature):
        print(f'Filling tank {temperature}')

    def _add_soap(self):
        print('Adding soap')

    def _wash(self):
        print('Washing clothes')

    def _centrifuge(self):
        print('Spinning clothes')

if __name__ == '__main__':
    washing_machine = Washing_Machine()
    washing_machine.wash()