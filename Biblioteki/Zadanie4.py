import pytest
class Prostokat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * (self.x * self.y)

    def test_pole(self):
        p = Prostokat(5, 10)
        assert p.pole() == 50
        assert p.obwod() == 30

if __name__ == '__main__':
    pytest.main()

class Uzytkownik:
    @staticmethod
    def waliduj_haslo(haslo):
        assert Uzytkownik.waliduj_haslo('123456789') is True
        assert Uzytkownik.waliduj_haslo('1234') is False

if __name__ == '__main__':
    pytest.main()