from uberX import UberX
from account import Account
from car import Car
def run():
    uberX = UberX('AMS234', Account("Andres Herrera", "ANDA876"), 'Chevrolet', 'Sonic')
    #uberX.printDataCar()
    uberX.setPassenger(4)
    print('There are ' + uberX.getPassenger)

if __name__ == '__main__':
    run()