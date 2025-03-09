import pytest

class
if n == 0:
    return 1
else:
    return n * silnia(n-1)

def test_silnia():
    assert silnia(5) == 120
    assert silnia(8) == 2
    try:
        silnia(-2)
    except ValueError as e:
        assert str(e) == 'Silnia nie istnieje dla liczb ujemnych'

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def test_czy_pierwsza():
    assert czy_pierwsza(7) is True
    assert czy_pierwsza(9) is False

def formatuj_tekst(tekst):
    return tekst.strip().capitalize()

def test_formatuj_tekst():
    assert formatuj_tekst('hello') == 'Hello'
    assert formatuj_tekst('WORLD') == 'World'

if __name__ == '__main__':
    pytest.main()