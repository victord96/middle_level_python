import re
def run():

    string = input('Pasame un String')
    resultado = string.find('0x')
    print(resultado)

if __name__ == '__main__':
    run()