# Obsługa wyjątków i testowanie oprogramowania - 18.01.2025 - MS

from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3
import os

# Tworzymy aplikację Flask
app = Flask(__name__)

# Nazwa pliku bazy danych
DATABASE = 'users.db'


# Funkcja do połączenia z bazą danych
# Otwiera połączenie z plikiem bazy danych i ustawia Row Factory, aby rekordy były dostępne jako słowniki

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Umożliwia dostęp do kolumn przez nazwy
    return conn


# Funkcja do tworzenia tabeli użytkowników, jeśli baza danych jeszcze nie istnieje
def create_tables():
    if not os.path.exists(DATABASE):  # Sprawdzamy, czy baza danych już istnieje
        conn = get_db_connection()  # Tworzymy połączenie z bazą danych
        conn.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')  # Tworzymy tabelę 'users' z kolumnami id, username i email
        conn.commit()  # Zapisujemy zmiany w bazie
        conn.close()  # Zamykamy połączenie


# Strona główna, która wyświetla listę użytkowników i umożliwia dodanie nowego użytkownika
@app.route('/')
def home():
    conn = get_db_connection()  # Otwieramy połączenie z bazą danych
    users = conn.execute('SELECT * FROM users').fetchall()  # Pobieramy wszystkich użytkowników z bazy danych
    conn.close()  # Zamykamy połączenie z bazą
    users = [dict(user) for user in users]  # Konwertujemy Row na dict dla kompatybilności z Jinja2
    return render_template('index.html', users=users)  # Renderujemy stronę główną z listą użytkowników


# Obsługa dodawania użytkownika z formularza na stronie głównej
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']  # Pobieramy nazwę użytkownika z formularza
    email = request.form['email']  # Pobieramy email z formularza
    if not username or not email:  # Walidacja: czy oba pola są wypełnione
        return jsonify({"error": "Username and email are required"}), 400

    conn = get_db_connection()  # Otwieramy połączenie z bazą danych
    try:
        conn.execute(
            'INSERT INTO users (username, email) VALUES (?, ?)',
            (username, email)  # Wstawiamy nowego użytkownika do tabeli
        )
        conn.commit()  # Zapisujemy zmiany
        conn.close()  # Zamykamy połączenie
        return redirect(url_for('home'))  # Przekierowanie na stronę główną
    except sqlite3.IntegrityError as e:  # Obsługa błędów unikalności dla username lub email
        conn.close()  # Zamykamy połączenie w przypadku błędu
        return jsonify({"error": str(e)}), 400


# Rejestracja użytkownika za pomocą API (endpoint)
@app.route('/api/register', methods=['POST'])
def register_api():
    data = request.get_json()  # Pobieramy dane JSON z żądania
    if not data or not data.get('username') or not data.get('email'):  # Walidacja danych wejściowych
        return jsonify({"error": "Invalid data"}), 400

    conn = get_db_connection()  # Otwieramy połączenie z bazą danych
    try:
        conn.execute(
            'INSERT INTO users (username, email) VALUES (?, ?)',
            (data['username'], data['email'])  # Wstawiamy nowego użytkownika do tabeli
        )
        conn.commit()  # Zapisujemy zmiany
        user_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]  # Pobieramy ID nowego użytkownika
        conn.close()  # Zamykamy połączenie
        return jsonify({"id": user_id, "username": data['username'], "email": data['email']}), 201
    except sqlite3.IntegrityError as e:  # Obsługa błędów unikalności
        conn.close()  # Zamykamy połączenie w przypadku błędu
        if 'username' in str(e):
            return jsonify({"error": "Username already exists"}), 400
        elif 'email' in str(e):
            return jsonify({"error": "Email already exists"}), 400


# Pobieranie wszystkich użytkowników za pomocą API
@app.route('/api/users', methods=['GET'])
def get_users_api():
    conn = get_db_connection()  # Otwieramy połączenie z bazą danych
    users = conn.execute('SELECT * FROM users').fetchall()  # Pobieramy wszystkich użytkowników
    conn.close()  # Zamykamy połączenie
    return jsonify([{"id": user["id"], "username": user["username"], "email": user["email"]} for user in users])  # Zwracamy listę użytkowników jako JSON


# Usuwanie użytkownika po ID za pomocą API
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()  # Otwieramy połączenie z bazą danych
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()  # Sprawdzamy, czy użytkownik istnieje
    if not user:  # Jeśli użytkownik nie istnieje, zwracamy błąd 404
        conn.close()
        return jsonify({"error": "User not found"}), 404
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))  # Usuwamy użytkownika z tabeli
    conn.commit()  # Zapisujemy zmiany
    conn.close()  # Zamykamy połączenie
    return jsonify({"message": "User deleted"}), 200


# Pobieranie użytkownika po ID za pomocą API
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()  # Otwieramy połączenie z bazą danych
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()  # Pobieramy użytkownika po ID
    conn.close()  # Zamykamy połączenie
    if not user:  # Jeśli użytkownik nie istnieje, zwracamy błąd 404
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user["id"], "username": user["username"], "email": user["email"]}), 200  # Zwracamy dane użytkownika jako JSON


if __name__ == '__main__':
    create_tables()  # Tworzenie tabeli przed uruchomieniem aplikacji, jeśli jeszcze nie istnieje
    app.run(debug=True)  # Uruchamiamy serwer w trybie debugowania
