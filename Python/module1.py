value = 42

def allowed_fun():
    print(restricted_fun())
    return 'I am allowed!'

def restricted_fun():
    return 'I am restricted!'