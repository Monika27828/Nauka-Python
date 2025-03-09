import pytest
import sqlite3

def zapisz_do_bazy(db_name, dane):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXIST dane (id INTEGER PRIMARY KEY, tekst TEXT)')
    cursor.execute('INSERT INTO dane (tekst) VALUES (?)', (dane,))
    conn.commit()
    conn.close()

def test_zapisz_do_bazy():
    db_name = 'baza.db'
    dane = 'To jest tekst do zapisu do bazy'
    zapisz_do_bazy(db_name, dane)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT tekst FROM dane')
    wynik = cursor.fetchall() [0]
    assert wynik == dane, f'Oczekiwano: {dane}, otrzymano {wynik}'
    conn.close()
    print('Test integracyjny zakończony sukcesem')

if __name__ == '__main__':
    pytest.main()

