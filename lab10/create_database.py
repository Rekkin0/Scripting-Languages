import sys, sqlite3


def create_database(db_name: str) -> None:
    """
    Create a database with the given name.
    """
    
    # Connect to the database
    db: sqlite3.Connection = sqlite3.connect(f'{db_name}.sqlite3')
    cursor: sqlite3.Cursor = db.cursor()
    
    # Create table "Rentals"
    cursor.execute('''
        CREATE TABLE Rentals (
            rental_id INTEGER PRIMARY KEY UNIQUE,
            bike_number INTEGER,
            rental_time DATETIME,
            return_time DATETIME,
            duration INTEGER,
            rental_station INTEGER,
            return_station INTEGER,
            FOREIGN KEY (rental_station) REFERENCES Stations(station_id),
            FOREIGN KEY (return_station) REFERENCES Stations(station_id)
        )
    ''')
    
    # Create table "Stations"
    cursor.execute('''
        CREATE TABLE Stations (
            station_id INTEGER PRIMARY KEY UNIQUE,
            station_name TEXT UNIQUE
        )
    ''')
    
    # Commit changes and close the connection
    db.commit()
    db.close()
    

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise SystemExit('Missing database name (usage: python create_database.py <database_name>).') 
    db_name: str = sys.argv[1]
    create_database(db_name)
    print(f'Database "{db_name}.sqlite3" created successfully.')
    