import sys, csv, sqlite3
from pathlib import Path
from typing import Iterator

from utils import db_exists, file_exists


RentalData = tuple[int, int, str, str, int, str, str]

INSERT_STATION_COMMAND = '''
    INSERT OR IGNORE INTO Stations (station_name)
    VALUES (?)
'''
INSERT_RENTAL_COMMAND = '''
    INSERT OR IGNORE INTO Rentals (rental_id, bike_number, rental_time, return_time, duration, rental_station, return_station)
    VALUES (?, ?, ?, ?, ?, (SELECT station_id FROM Stations WHERE station_name = ?), (SELECT station_id FROM Stations WHERE station_name = ?))
'''


def get_file_paths() -> tuple[Path, Path]:
    """
    Get file paths from the arguments.
    """
    if len(sys.argv) <= 2:
        raise SystemExit('Missing courses file path or database name (usage: python load_data.py <data_file_path> <database_name>).')
    courses_file: Path = file_exists(sys.argv[1])
    db_file: Path = db_exists(sys.argv[2])
    return courses_file, db_file

def insert_station(cursor: sqlite3.Cursor, station_name: str):
    """
    Insert station names (if they aren't already there) into table "Stations".
    """
    cursor.execute(INSERT_STATION_COMMAND, (station_name,))
    
def insert_rental(cursor: sqlite3.Cursor, rental_data: RentalData):
    """
    Insert rental data into table "Rentals".
    """
    cursor.execute(INSERT_RENTAL_COMMAND, (*rental_data,))

def load_data(courses_file: Path, db_file: Path):
    """
    Load data from the given file into the database.
    """
    db: sqlite3.Connection = sqlite3.connect(db_file)
    cursor: sqlite3.Cursor = db.cursor()

    with open(courses_file, 'r') as file:
        reader: Iterator = csv.reader(file)
        next(reader)  # Skip file header

        for row in reader:
            rental_id: int = int(row[0])
            bike_number: int = int(row[1])
            rental_time: str = row[2]
            return_time: str = row[3]
            rental_station: str = row[4]
            return_station: str = row[5]
            duration: int = int(row[6])
            rental_data: RentalData = (rental_id, 
                                       bike_number, 
                                       rental_time, 
                                       return_time, 
                                       duration, 
                                       rental_station, 
                                       return_station)

            insert_station(cursor, rental_station)
            insert_station(cursor, return_station)
            insert_rental(cursor, rental_data)

    db.commit()
    db.close()
    print('Data loaded successfully.')
    
    
if __name__ == '__main__':
    courses_file, db_file = get_file_paths()
    load_data(courses_file, db_file)
