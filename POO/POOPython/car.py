class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'STANDBY'
        self._motor = Motor(cylinder=4)

    def accelerate(self, type='slow'):
        if type == 'quickly':
            self._motor.inyect_Gasoline(10)
        else:
            self._motor.inyect_Gasoline(3)

        self._state = 'in motion'    

    def deccelerate(self, type='quickly'):
        if type == 'slow':
            self._motor.inyect_Gasoline(3)
        else:
            self._motor.inyect_Gasoline(10)

        self._state = 'in motion'

class Motor:

    def __init__(self, cylinder, type = 'Gasoline'):
        self.cylinder = cylinder
        self.type = type
        self._temperature = 0

    def inyect_Gasoline(self, quantity):
        self.quantity = 100
    
class Gearbox:
    def __init__(self, n_gear):
        self.n_gear = n_gear

    def change_gear(self, gear):
        self.gear = gear
        if gear <= self.n_gear: 
            print(f'The new gear is' , gear)
        else:
            print('That exceed the number of car gears')


def run():
    gear1 = Gearbox(6)

    gear1.change_gear(7)


if __name__ == '__main__':
    run()