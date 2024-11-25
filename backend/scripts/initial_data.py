import istatdata as istat
import populate_commons as pc
import populate_weather as pw
import os
from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv()

DOT_ENV_FILE = os.path.join(BASE_DIR, ".env")
if os.path.isfile(DOT_ENV_FILE):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY')

# Data configuration information variables
# Load environment variables from .env file
url = os.environ.get('URL')
input_filename = os.environ.get('INPUT_FILENAME')
output_filename = os.environ.get('OUTPUT_FILENAME')
header_row = ["Common_Name", "Common_Code"]
banner = "Fiscal code calculator!!!"
db_file = os.environ.get('DB_FILE')

# Data to populate commons
csv_file1 = output_filename
table_name1 = os.environ.get('TABLE_NAME')

# Data to populate weather
# Example usage
csv_file2 = os.environ.get('INPUT_FILENAME_WEATHER')
table_name2 = os.environ.get('TABLE_NAME_WEATHER')
print(csv_file2)

# Retrieve the file of commons
istat.retrieve_file(url, input_filename)
# Run the function to normalize the data
istat.extract_columns(input_filename, output_filename, 5, 19)  # Remember the index starts at 0
# Add the header to the output file
istat.add_header_to_csv(output_filename, header_row)

# Run the function to populate commons
pc.import_csv_to_sqlite(csv_file1, db_file, table_name1)

# Run the function to populate weather
pw.import_csv_to_sqlite(csv_file2, db_file, table_name2)

# https://www.weatherapi.com/docs/weather_conditions.csv --> icons mapping