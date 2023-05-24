import sys, sqlite3
from typing import Any


Station = tuple[str, int]


ALL_STATIONS_COMMAND: str = '''
    SELECT station_name, station_id
    FROM Stations
'''
AVERAGE_DURATION_STARTED_FROM_GIVEN_STATION_COMMAND: str = '''
    SELECT AVG(duration)
    FROM Rentals
    WHERE rental_station = ?
'''
AVERAGE_DURATION_FINISHED_AT_GIVEN_STATION_COMMAND: str = '''
    SELECT AVG(duration)
    FROM Rentals
    WHERE return_station = ?
'''
UNIQUE_BIKES_PARKED_AT_GIVEN_STATION_COMMAND: str = '''
    SELECT COUNT(DISTINCT bike_number)
    FROM Rentals
    WHERE rental_station = ?
'''
STATIONS_MOST_STARTED_FROM: str = '''
    SELECT station_name, COUNT(rental_station) as rental_count
    FROM Rentals
    INNER JOIN Stations
    ON Rentals.rental_station = Stations.station_id
    GROUP BY rental_station
    ORDER BY rental_count DESC
    LIMIT
'''

def get_database_name() -> str:
    """
    Get database name from the arguments.
    """
    if len(sys.argv) <= 1:
        raise SystemExit('Missing database name (usage: python queries.py <database_name>).') 
    db_name: str = sys.argv[1]
    return db_name

def all_stations(cursor: sqlite3.Cursor) -> list[Station]:
    """
    Get all stations.
    """
    cursor.execute(ALL_STATIONS_COMMAND)
    stations: list[Station] = cursor.fetchall()
    return stations

def list_stations(stations: list[Station]):
    """
    List all stations.
    """
    print("Available stations:")
    for index, station in enumerate(stations):
        print(f"[{index+1}] {station[0]}")

def select_station(cursor: sqlite3.Cursor, stations: list[Station]) -> Station:
    """
    Select a station from the list.
    """
    station_choice: int = int(input("Select a station: "))
    if station_choice < 1 or station_choice > len(stations):
        raise SystemExit("\nInvalid station choice.")
    selected_station: Station = stations[station_choice-1]
    return selected_station

def average_duration_started_from_given_station(cursor: sqlite3.Cursor, station: Station) -> float:
    """
    Get average duration of rentals started from the given station.
    """
    station_name, station_id = station
    cursor.execute(AVERAGE_DURATION_STARTED_FROM_GIVEN_STATION_COMMAND, (station_id,))
    result: float = cursor.fetchone()[0]
    print(f"Average duration of a course started from '{station_name}': {result} seconds")
    return result

def average_duration_finished_at_given_station(cursor: sqlite3.Cursor, station: Station) -> float:
    """
    Get average duration of rentals finished at the given station.
    """
    station_name, station_id = station
    cursor.execute(AVERAGE_DURATION_FINISHED_AT_GIVEN_STATION_COMMAND, (station_id,))
    result: float = cursor.fetchone()[0]
    print(f"Average duration of a course finished at '{station_name}': {result} seconds")
    return result

def unique_bikes_parked_at_given_station(cursor: sqlite3.Cursor, station: Station) -> int:
    """
    Get number of unique bikes parked at the given station.
    """
    station_name, station_id = station
    cursor.execute(UNIQUE_BIKES_PARKED_AT_GIVEN_STATION_COMMAND, (station_id,))
    result: int = cursor.fetchone()[0]
    print(f"Number of unique bikes parked at '{station_name}': {result}")
    return result

def stations_most_started_from(cursor: sqlite3.Cursor, num: int) -> list[Station]:
    cursor.execute(STATIONS_MOST_STARTED_FROM + str(num))
    result: list[Station] = cursor.fetchall()
    print(num, "stations most started from:")
    for record in result:
        print(f'{record[0]}\t{record[1]}')
    return result

def main(db_name: str):
    db: sqlite3.Connection = sqlite3.connect(f'{db_name}.sqlite3')
    cursor: sqlite3.Cursor = db.cursor()

    stations: list[Station] = all_stations(cursor)
    list_stations(stations)
    selected_station: Station = select_station(cursor, stations)
    print()

    average_duration_started_from_given_station(cursor, selected_station)
    average_duration_finished_at_given_station(cursor, selected_station)
    unique_bikes_parked_at_given_station(cursor, selected_station)
    stations_most_started_from(cursor, 10)
    
    db.close()

if __name__ == '__main__':
    db_name: str = get_database_name()
    main(db_name)
