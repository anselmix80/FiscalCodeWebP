import csv
import sqlite3

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
