import sys
import logicalcs as fc
import istatdata as istat

# Data configuration information variables
url = 'https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv'
input_filename = "commons.csv"
output_filename = "output.csv"
header_row = ["Common_Name", "Common_Code"]
banner = "Fiscal code calculator!!!"

def assembly(*args):
    # Set default values for variables
    name = None
    surname = None
    date = None
    city = None
    sex = None

    # Check if the user wants to reset the data from istat
    if len(sys.argv) < 2:
        print("Missing argument: add R to reset data from istat any other key to go on")
        sys.exit(1)

    # Get the arguments passed through the command line assignment
    list = args[0]
    for i in range(0, len(list)):
        start = list[0]
        if i == 1:
            name = list[1]
        if i == 2:
            surname = list[2]
        if i == 3:
            date = list[3]
        if i == 4:
            city = list[4]
        if i == 5:
            sex = list[5].upper()

    # Start the program if R or r and files don't exist download data from istat else go ahead
    check_output = istat.check_file_istat(output_filename)
    check_input = istat.check_file_istat(input_filename)
    if (check_output is False and check_input is False) or start == "R" or start == "r":
        # Clean all csv file from istat and also the output file normalized
        istat.clean_files(input_filename, output_filename)
        # Retrieve the file of commons
        istat.retrieve_file(url, input_filename)

        # Run the function to normalize the data
        istat.extract_columns(input_filename, output_filename, 5, 19)  # Remember the index starts at 0
        # Add the header to the output file
        istat.add_header_to_csv(output_filename, header_row)

    # Start input
    print(fc.ascii_banner(banner))
    print("Please insert data:")

    # Run the function to validate name and surname if not present, input them
    if name is None:
        name = input("Name: ")
    if surname is None:
        surname = input("Surname: ")

    # Run the function to validate date if not valid, retry
    while True:
        if date is None:
            date = input("Insert date in format DD/MM/YYYY: ")
        if fc.check_date(date):
            break
        else:
            print("Wrong Format, retry.")
            date = input("Insert date in format DD/MM/YYYY: ")

    # Convert the date to a datetime object in format DD/MM/YYYY
    date = fc.datetime.datetime.strptime(date, "%d/%m/%Y")

    # Get the day, month and year separately
    day = date.strftime("%d")
    month = date.strftime("%m")
    year = date.strftime("%Y")

    # Run the function to find the city if not found, retry
    while True:
        if city is None:
            city = input("City: ")
        result = fc.find_city(output_filename, city, 1)
        if result:
            print("City founded:", city.upper())
            break
        else:
            print("City didn't find. Retry")
            city = input("City: ")

    # Run the function to indicate the sex if it is wrong, retry
    while True:
        if sex is None:
            sex = input("Sex (M o F): ")  # Convert to uppercase
        if sex in ["M", "F"]:
            break  # Input valid -- exit loop
        else:
            sex = input("Sex (M o F): ")
            print("Invalid value. Enter M for male or F for female.")

    # Create the string to pass to the function of control character
    valor = fc.calc_surname(surname.upper()) + fc.calc_name(name.upper()) + str(year[2:4]) \
        + fc.convert_month(month.upper()) \
        + str(fc.day_creation(str(day), sex)) + fc.find_city(output_filename, city, 1)

    # Get the control character
    control_char = fc.control_character(valor)

    # Create the fiscal code
    cf = valor + control_char
    # print("Fiscal code: " + cf)
    return cf
