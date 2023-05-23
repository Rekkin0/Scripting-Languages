import sqlite3

def display_data(database_file):
    # Połączenie z bazą danych
    conn = sqlite3.connect(database_file)
    c = conn.cursor()

    # Wykonanie zapytania i pobranie wszystkich danych z tabeli "Rentals"
    c.execute("SELECT * FROM Rentals")
    rentals_data = c.fetchall()

    # Wyświetlenie danych z tabeli "Rentals"
    print("Rentals:")
    for row in rentals_data:
        print(row)

    # Wykonanie zapytania i pobranie wszystkich danych z tabeli "Stations"
    c.execute("SELECT * FROM Stations")
    stations_data = c.fetchall()

    # Wyświetlenie danych z tabeli "Stations"
    print("\nStations:")
    for row in stations_data:
        print(row)

    # Zamknięcie połączenia z bazą danych
    conn.close()

if __name__ == '__main__':
    database_file = 'rentals.sqlite3'  # Podaj nazwę swojego pliku bazy danych SQLite
    display_data(database_file)
