from account import Account


class Car:
    id = int
    license = str
    driver = Account("","")
    __passenger = int

    def __init__(self, license, driver):
        self.license = license
        self.driver = driver 

    def printDataCar(self):
        print('License: ' + self.license + 'Name Driver: ' + self.driver.name)
 