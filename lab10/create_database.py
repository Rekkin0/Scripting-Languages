import sys, sqlite3

from utils import db_not_exists


CREATE_TABLE_STATIONS_COMMAND: str = '''
    CREATE TABLE Stations (
        station_id INTEGER PRIMARY KEY UNIQUE,
        station_name TEXT UNIQUE
    )
'''
CREATE_TABLE_RENTALS_COMMAND: str = '''
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
'''


def get_database_name() -> str:
    """
    Get database name from the arguments.
    """
    if len(sys.argv) <= 1:
        raise SystemExit('Missing database name (usage: python create_database.py <database_name>).') 
    db_name: str = db_not_exists(sys.argv[1])
    return db_name

def create_table_stations(cursor: sqlite3.Cursor):
    """
    Create table "Stations".
    """
    cursor.execute(CREATE_TABLE_STATIONS_COMMAND)

def create_table_rentals(cursor: sqlite3.Cursor):
    """
    Create table "Rentals".
    """
    cursor.execute(CREATE_TABLE_RENTALS_COMMAND)
    
def create_database(db_name: str):
    """
    Create a database with the given name.
    """
    db: sqlite3.Connection = sqlite3.connect(f'{db_name}.sqlite3')
    cursor: sqlite3.Cursor = db.cursor()
    
    create_table_rentals(cursor)
    create_table_stations(cursor)
    
    db.commit()
    db.close()
    print(f'Database "{db_name}.sqlite3" created successfully.')
    

if __name__ == '__main__':
    db_name: str = get_database_name()
    create_database(db_name)  
    