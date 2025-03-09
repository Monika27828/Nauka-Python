# Funkcja do filtrowania liczb pierwszych

import pytest
array = [3,6,5,7,13,11,22,25,75]

def filtruj_tablice(array):
    for element in array:
        if czy_liczba_pierwsza(element) == True:
            print(element)
            array.remove(element)
    return array

def test_filtruj_tablice():
    assert filtruj_tablice(array) == [6, 7, 11, 22, 25, 75]

if __name__ == '__main__':
    pytest.main()