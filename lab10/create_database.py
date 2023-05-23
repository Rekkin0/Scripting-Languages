import sys, sqlite3


def create_database(db_name: str) -> None:
    """
    Create a database with the given name.
    """
    
    db: sqlite3.Connection = sqlite3.connect(f'{db_name}.sqlite3')
    cursor: sqlite3.Cursor = db.cursor()
    
    cursor.execute('''
        CREATE TABLE Rentals (
            rental_id INTEGER PRIMARY KEY,
            bike_number INTEGER,
            rental_time DATETIME,
            return_time DATETIME,
            rental_station INTEGER,
            return_station INTEGER,
            duration INTEGER,
            FOREIGN KEY (rental_station) REFERENCES Stations(station_id),
            FOREIGN KEY (return_station) REFERENCES Stations(station_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE Stations (
            station_id INTEGER PRIMARY KEY,
            station_name TEXT
        )
    ''')
    
    db.commit()
    db.close()
    

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise SystemExit('Missing database name') 
    db_name: str = sys.argv[1]
    create_database(db_name)
    print(f'Database "{db_name}.sqlite3" created successfully.')
    