settings = {
    'option_1': True,
    'option_2': 100,
    'option_3': "Witam"
}

def set_option(key, value):
    settings[key] = value

def get_option(key):
    return settings.get(key, None)