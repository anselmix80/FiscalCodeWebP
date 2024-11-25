import csv
import sqlite3

def import_csv_to_sqlite(csv_file, db_file, table_name):
    """
    Imports a CSV file into a SQLite database table.

    Args:
        csv_file (str): Path to the CSV file.
        db_file (str): Path to the SQLite database file.
        table_name (str): Name of the table to create in the database.
    """

    with sqlite3.connect(db_file) as conn:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        # Create the table if it doesn't exist, specifying column types
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            columns = next(reader)
            c.execute('CREATE TABLE IF NOT EXISTS {} ({})'.format(table_name, ', \
                '.join([f'{column} TEXT' for column in columns])))

        # Insert data into the table
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            c.executemany(f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(next(reader)))})", reader)

        conn.commit()

# Example usage
csv_file = "weather_icon.csv"
db_file = "../backend/db.sqlite3"
table_name = "weather_icon_weather"

import_csv_to_sqlite(csv_file, db_file, table_name)
