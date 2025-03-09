def add_v1(a,b):
    return a + b

def add_v2(a,b):  # przerobienie na stringi
    return f'{a}' + f'{b}'

def add_v3(a,b):
    return f'podano {a=} i {b=}'

def load_version(number):
    if number == 1:
        return add_v1
    elif number == 2:
        return add_v2
    elif number == 3:
        return add_v3
    else:
        raise ValueError('Funkcja o tym numerze nie istnieje')