import calc.logics as logics
import calc.istat as istat
import calc.populate_common as pc
from fiscal_code.settings import url, input_filename, output_filename, header_row, db_file, table_name
import os
import codecs

# Data configuration information variables
url = url
input_filename = input_filename
output_filename = output_filename
header_row = header_row
db_file = db_file
table_name = table_name

def fc(name, surname, date, city, sex):
    """Create the fiscal code based on the name, surname, date of birth, city of birth and sex.
    Run the function to retrieve file from web if not present in the folder
    Run the function to normalize the data
    Add the header to the output file
    Run the function to clean table
    Run the function to insert data into table
    Run the function create the fiscal code

    Args:
        name (str): name of the person
        surname (str): surname of the person
        date (date): date of birth
        city (str): city of birth
        sex (str): sex of the person

    Returns:
        str: fiscal code
    """

    # Start the program if R or r and files don't exist download data from istat else go ahead
    check_output = istat.check_file_istat(output_filename)
    check_input = istat.check_file_istat(input_filename)
    if (check_output is False or check_input is False):
        # Clean all csv file from istat and also the output file normalized
        istat.clean_files(input_filename, output_filename)
        # Retrieve the file of commons
        istat.retrieve_file(url, input_filename)
        
        # Convert ISO-8859-1 to UTF-8
        sourceFileName = input_filename
        targetFileName = input_filename+'.tmp'
        BLOCKSIZE = 1048576 # or some other, desired size in bytes
        with codecs.open(sourceFileName, "r", "ISO-8859-1") as sourceFile:
            with codecs.open(targetFileName, "w", "utf-8") as targetFile:
                while True:
                    contents = sourceFile.read(BLOCKSIZE)
                    if not contents:
                        break
                    targetFile.write(contents.replace('ISO-8859-1','utf-8'))

        os.rename(targetFileName,sourceFileName)

        # Run the function to normalize the data
        istat.extract_columns(input_filename, output_filename, 5, 19)  # Remember the index starts at 0
        # Add the header to the output file
        istat.add_header_to_csv(output_filename, header_row)

        # Reset the table COMMONS
        pc.empty_table(db_file, table_name)
        pc.import_csv_to_sqlite(output_filename, db_file, table_name)

    # Convert the date to a datetime object in format DD/MM/YYYY
    date = logics.datetime.datetime.strptime(date, "%d/%m/%Y")

    # Get the day, month and year separately
    day = date.strftime("%d")
    month = date.strftime("%m")
    year = date.strftime("%Y")

    # Create the string to pass to the function of control character
    valor = logics.calc_surname(surname.upper()) + logics.calc_name(name.upper()) + str(year[2:4]) \
        + logics.convert_month(month.upper()) \
        + str(logics.day_creation(str(day), sex)) + logics.find_city(output_filename, city, 1)

    # Get the control character
    control_char = logics.control_character(valor)

    # Create the fiscal code
    cf = valor + control_char

    # print("Fiscal code: " + cf)
    return cf
