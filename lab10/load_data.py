import sys, csv, sqlite3
from pathlib import Path
from typing import Iterator

from utils import db_exists, file_exists


def load_data(courses_file: Path, db_file: Path):
    """
    Load data from the given file into the database.
    """
    
    # Connect to the database
    db: sqlite3.Connection = sqlite3.connect(db_file)
    cursor: sqlite3.Cursor = db.cursor()

    # Open the file with data
    with open(courses_file, 'r') as file:
        reader: Iterator = csv.reader(file)
        next(reader)  # Skip file header

        # Iterate over data in the file and insert it into the database
        for row in reader:
            rental_id: int = int(row[0])
            bike_number: int = int(row[1])
            rental_time: str = row[2]
            return_time: str = row[3]
            rental_station: str = row[4]
            return_station: str = row[5]
            duration: int = int(row[6])

            # Insert rental station names (if they aren't already there) into table "Stations"
            cursor.execute('''
                INSERT OR IGNORE INTO Stations (station_name)
                VALUES (?)
                ''',
                (rental_station,)
            )
            
            # Insert return station names (if they aren't already there) into table "Stations"
            cursor.execute('''
                INSERT OR IGNORE INTO Stations (station_name)
                VALUES (?)
                ''',
                (return_station,)
            )

            # Insert data into table "Rentals"
            cursor.execute('''
                INSERT INTO Rentals (rental_id, bike_number, rental_time, return_time, duration, rental_station, return_station)
                VALUES (?, ?, ?, ?, ?, (SELECT station_id FROM Stations WHERE station_name = ?), (SELECT station_id FROM Stations WHERE station_name = ?))
                ''', 
                (rental_id, bike_number, rental_time, return_time, duration, rental_station, return_station)
            )

    # Commit changes and close the connection
    db.commit()
    db.close()

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        raise SystemExit('Missing courses file path or database name (usage: python load_data.py <data_file_path> <database_name>).')
    courses_file: Path = file_exists(sys.argv[1])
    db_file: Path = db_exists(sys.argv[2])
    load_data(courses_file, db_file)
    print('Data loaded successfully.')
