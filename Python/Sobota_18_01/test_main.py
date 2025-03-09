import unittest
from flask import json
from Aplikacja_Flask import app, get_db_connection, create_tables

# Testy jednostkowe dla aplikacji Flask
class FlaskTestCase(unittest.TestCase):

    # Metoda uruchamiana raz przed wszystkimi testami
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True  # Ustawienie aplikacji w tryb testowy
        cls.client = app.test_client()  # Tworzenie klienta testowego

        # Tworzenie tabel w bazie danych
        create_tables()

    # Metoda uruchamiana przed każdym testem
    def setUp(self):
        # Czyszczenie tabel przed każdym testem
        conn = get_db_connection()
        conn.execute('DELETE FROM users')  # Usuwanie wszystkich danych z tabeli users
        conn.execute('DELETE FROM sqlite_sequence WHERE name="users"')  # Resetowanie sekwencji ID
        conn.commit()
        conn.close()


    # Testowanie strony głównej aplikacji
    def test_home_route(self):
        response = self.client.get('/')  # Wysyłanie żądania GET na stronę główną
        self.assertEqual(response.status_code, 200)  # Sprawdzanie, czy odpowiedź ma status 200
        self.assertIn(b"<!DOCTYPE html>", response.data)  # Sprawdzanie, czy odpowiedź zawiera kod HTML

    # Test rejestracji użytkownika przez API
    def test_register_user(self):
        response = self.client.post('/api/register',
                                     data=json.dumps({"username": "testuser", "email": "test@example.com"}),
                                     content_type='application/json')  # Wysyłanie danych JSON
        self.assertEqual(response.status_code, 201)  # Sprawdzanie, czy użytkownik został utworzony
        self.assertIn("testuser", response.get_data(as_text=True))  # Sprawdzanie, czy odpowiedź zawiera nazwę użytkownika

    # Test rejestracji użytkownika z duplikatem nazwy
    def test_register_duplicate_user(self):
        self.client.post('/api/register',
                         data=json.dumps({"username": "testuser", "email": "test@example.com"}),
                         content_type='application/json')  # Rejestracja użytkownika
        response = self.client.post('/api/register',
                                     data=json.dumps({"username": "testuser", "email": "test2@example.com"}),
                                     content_type='application/json')  # Próba rejestracji użytkownika z taką samą nazwą
        self.assertEqual(response.status_code, 400)  # Sprawdzanie, czy odpowiedź ma status 400
        self.assertIn("Username already exists", response.get_data(as_text=True))  # Sprawdzanie komunikatu o błędzie

    # Test pobierania wszystkich użytkowników
    def test_get_users(self):
        self.client.post('/api/register',
                         data=json.dumps({"username": "user1", "email": "user1@example.com"}),
                         content_type='application/json')  # Rejestracja pierwszego użytkownika
        self.client.post('/api/register',
                         data=json.dumps({"username": "user2", "email": "user2@example.com"}),
                         content_type='application/json')  # Rejestracja drugiego użytkownika
        response = self.client.get('/api/users')  # Pobieranie listy użytkowników
        self.assertEqual(response.status_code, 200)  # Sprawdzanie, czy odpowiedź ma status 200
        users = json.loads(response.data)  # Parsowanie odpowiedzi JSON
        self.assertEqual(len(users), 2)  # Sprawdzanie, czy lista zawiera dwóch użytkowników
        self.assertEqual(users[0]["username"], "user1")  # Sprawdzanie pierwszego użytkownika
        self.assertEqual(users[1]["username"], "user2")  # Sprawdzanie drugiego użytkownika

    # Test pobierania użytkownika po ID
    def test_get_user_by_id(self):
        self.client.post('/api/register',
                         data=json.dumps({"username": "user3", "email": "user3@example.com"}),
                         content_type='application/json')  # Rejestracja użytkownika

        response = self.client.get('/api/users/1')  # Pobieranie użytkownika o ID 1
        self.assertEqual(response.status_code, 200)  # Sprawdzanie, czy odpowiedź ma status 200
        self.assertIn("user3", response.get_data(as_text=True))  # Sprawdzanie, czy odpowiedź zawiera dane użytkownika

    # Test usuwania użytkownika po ID
    def test_delete_user(self):
        self.client.post('/api/register',
                         data=json.dumps({"username": "user4", "email": "user4@example.com"}),
                         content_type='application/json')  # Rejestracja użytkownika

        response = self.client.delete('/api/users/1')  # Usuwanie użytkownika o ID 1
        self.assertEqual(response.status_code, 200)  # Sprawdzanie, czy odpowiedź ma status 200
        self.assertIn("User deleted", response.get_data(as_text=True))  # Sprawdzanie komunikatu o usunięciu

        # Sprawdzenie, czy użytkownik został usunięty
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = 1').fetchone()  # Pobieranie użytkownika z bazy
        conn.close()
        self.assertIsNone(user)  # Sprawdzanie, czy użytkownik nie istnieje

    # Test usuwania nieistniejącego użytkownika
    def test_delete_nonexistent_user(self):
        response = self.client.delete('/api/users/999')  # Próba usunięcia użytkownika o ID, które nie istnieje
        self.assertEqual(response.status_code, 404)  # Sprawdzanie, czy odpowiedź ma status 404
        self.assertIn("User not found", response.get_data(as_text=True))  # Sprawdzanie komunikatu o błędzie


if __name__ == '__main__':
    unittest.main()  # Uruchamianie testów
