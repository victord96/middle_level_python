PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('What\'s your password?')

        if password == PASSWORD:
            return func()
        else:
            print('The password is incorrect')

    return wrapper    

@password_required
def needs_password():
    print('Password right!')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper    


@upper
def say_my_name(name):
    return f'Hi, {name}'

def run():
    print(say_my_name('David'))


if __name__ == '__main__':
    run()