# Fiscal Code calculator
import datetime
import csv
from pyfiglet import Figlet

def ascii_banner(name):
    custom_fig = Figlet(font='graffiti')
    banner = custom_fig.renderText(name)
    return banner

# Date format validation
def check_date(date):
    try:
        datetime.datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Find city in normalized data output_file
def find_city(filename, city, column_result):
    """
    Searches for a keyword in a specific column of a CSV file and returns the corresponding value in another column.

    Args:
        file_name: The name of the CSV file.
        keyword: The word to search for (case-sensitive).
        result_column: The index of the column to return (starting at 0).

    Returns:
        The value of the column specified for the keyword found, or None if it is not found.
    """

    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0].upper() == city.upper():
                return row[column_result]
    return None

# Run the function to calculate the surname with rules
def calc_surname(value):
    """
    Parses a string and returns consonants and vowel queries.

    Subjects:
        string: The string to parse.

    Returns:
        A string with the result of the analysis.
    """

    # Replace all spaces with nothing
    value = value.replace(" ", "")
    vowels = "aeiouAEIOU"
    consonants = ""
    first_vowels = ""

    for letter in value:
        if letter.isalpha():
            if letter not in vowels:
                consonants += letter
            else:
                first_vowels += letter

    if len(consonants) >= 3:
        return consonants[:3]
    elif len(consonants) == 2:
        return consonants + first_vowels[:1]
    elif len(consonants) == 1:
        return consonants + first_vowels[:2] + "X"
    elif len(first_vowels) >= 2:
        return first_vowels[:2] + "X"
    else:
        return "no consonants"

# Run the function to calculate the name with rules
def calc_name(value):
    """
    Parses a string and returns consonants and vowel queries.

    Subjects:
        string: The string to parse.

    Returns:
        A string with the result of the analysis.
    """

    # Replace all spaces with nothing
    value = value.replace(" ", "")

    # Define vowels and consonants
    vowels = "aeiouAEIOU"
    consonants = ""
    first_vowels = ""

    for letter in value:
        if letter.isalpha():
            if letter not in vowels:
                consonants += letter
            else:
                first_vowels += letter

    # Check if there are enough consonants
    if len(consonants) >= 4:
        return consonants[0] + consonants[2:4]
    elif len(consonants) == 3:
        return consonants
    elif len(consonants) == 2:
        return consonants + first_vowels[0]
    elif len(consonants) == 1:
        if len(first_vowels) >= 2:
            return consonants + first_vowels[:2]
        else:
            return consonants + first_vowels + "x"
    else:
        return first_vowels + "xx"

# Convert month in letter
def convert_month(month):
    """Converts a month number to a letter according to the table provided.

    Args:
        month: An integer between 1 and 12 representing a month.

    Returns:
        The letter corresponding to the month, or "Invalid month" if the number is out of range.
    """

    # Month table
    month_table = {
        "01": "A", "02": "B", "03": "C", "04": "D", "05": "E", "06": "H",
        "07": "L", "08": "M", "09": "P", "10": "R", "11": "S", "12": "T"
    }

    return month_table[month]

# Day of birth creation
def day_creation(day, sex):
    if sex == "F":
        day = int(day) + 40
    return day

# Generate the control character
def control_character(valor):
    """
    Converts even characters in a string according to the specified rules.

    Args:
        string: The string to process.

    Returns:
        A list containing the converted values.
    """

    # Dictionary of characters
    char_table_even = {
        'A': 0, '0': 0, 'F': 5, '5': 5, 'K': 10, 'P': 15, 'U': 20,
        'B': 1, '1': 1, 'G': 6, '6': 6, 'L': 11, 'Q': 16, 'V': 21,
        'C': 2, '2': 2, 'H': 7, '7': 7, 'M': 12, 'R': 17, 'W': 22,
        'D': 3, '3': 3, 'I': 8, '8': 8, 'N': 13, 'S': 18, 'X': 23,
        'E': 4, '4': 4, 'J': 9, '9': 9, 'O': 14, 'T': 19, 'Y': 24, 'Z': 25
    }

    char_table_odd = {
        'A': 1, '0': 1, 'F': 13, '5': 13, 'K': 2, 'P': 3, 'U': 16,
        'B': 0, '1': 0, 'G': 15, '6': 15, 'L': 4, 'Q': 6, 'V': 10,
        'C': 5, '2': 5, 'H': 17, '7': 17, 'M': 18, 'R': 8, 'W': 22,
        'D': 7, '3': 7, 'I': 19, '8': 19, 'N': 20, 'S': 12, 'X': 25,
        'E': 9, '4': 9, 'J': 21, '9': 21, 'O': 11, 'T': 14, 'Y': 24, 'Z': 23
    }

    char_1 = char_2 = 0

    for i in range(0, len(valor), 2):
        char_odd = valor[i].upper()  # Convert the character to uppercase
        if char_odd in char_table_odd:
            char_1 = char_1 + char_table_odd[char_odd]

    for i in range(1, len(valor), 2):
        char_even = valor[i].upper()  # Convert the character to uppercase
        if char_even in char_table_even:
            char_2 = char_2 + char_table_even[char_even]

    # Sum of even and odd characters and take the remainder of the division by 26
    control_number = (char_1 + char_2) % 26

    char_table_control = {
        0: 'A', 5: 'F', 10: 'K', 15: 'P', 20: 'U',
        1: 'B', 6: 'G', 11: 'L', 16: 'Q', 21: 'V',
        2: 'C', 7: 'H', 12: 'M', 17: 'R', 22: 'W',
        3: 'D', 8: 'I', 13: 'N', 18: 'S', 23: 'X',
        4: 'E', 9: 'J', 14: 'O', 19: 'T', 24: 'Y', 25: 'Z'
    }

    return char_table_control[control_number]
