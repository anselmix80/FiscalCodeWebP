import istatdata as istat
import csv
import sqlite3

# Data configuration information variables
url = 'https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv'
input_filename = "commons.csv"
csv_file = "output.csv"
db_file = "../backend/db.sqlite3"
table_name = "api_common"
header_row = ["Common_Name", "Common_Code"]

# Run the function to retrieve file
istat.clean_files(input_filename, csv_file)

istat.retrieve_file(url, input_filename)

# Run the function to normalize the data
istat.extract_columns(input_filename, csv_file, 5, 19)  # Remember the index starts at 0

# Add the header to the output file
istat.add_header_to_csv(csv_file, header_row)

# Run the function to clean table
def empty_table(db_file, table_name):

    """
    Empties a table in a SQLite database.

    Args:
        database_name (str): The name of the database file.
        table_name (str): The name of the table to
    """

    try:
        # DB Connection
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # SQL query to empty the table
        sql = f"DELETE FROM {table_name}"
        cursor.execute(sql)

        # Commit the changes
        conn.commit()
        conn.close()
        print(f"Table '{table_name}' emptied successfully.")

    except sqlite3.Error as e:
        print(f"Error while emptying table: {e}")

# Run the function
empty_table(db_file, table_name)

# Run the function to import csv to sqlite
def import_csv_to_sqlite(csv_file, db_file, table_name):
    """
    Imports a CSV file into a SQLite database table.

    Args:
        csv_file (str): Path to the CSV file.
        db_file (str): Path to the SQLite database file.
        table_name (str): Name of the table to create in the database.
    """
    try:
        # DB Connection
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

            print(f"Table '{table_name}' populated successfully.")

    except sqlite3.Error as e:
        print(f"Error while populating table: {e}")

import_csv_to_sqlite(csv_file, db_file, table_name)
