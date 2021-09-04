from car import Car

class UberX(Car):
    brand = str
    model = str

    def __init__(self, license, driver, brand, model):
        super().__init__(license,driver)
        self.brand = brand
        self.model = model    


   #ENCAPSULATE    

    def setPassenger(self,passengerNum):
        if passengerNum >= 4:
            self.__passenger = int(passengerNum)
            print("Passengers assigned : " + str(self.__passenger)) 

        else:
            print("You need to write 4 passengers")

    def getPassenger(self):
        if self.__passenger != int:
            print(self.__passenger)           