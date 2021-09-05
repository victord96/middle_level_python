class Person:

    def __init__(self, name):
        self.name = name

    def avance(self):
        print('I\'m walking')

class Ciclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def avance(self):
        print('I\'m moving with my bike')

def main():
    person = Person('David')
    person.avance()

    ciclist = Ciclist('Daniel')
    ciclist.avance()

if __name__ == '__main__':
    main()