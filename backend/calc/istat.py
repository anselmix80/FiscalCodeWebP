import os
import csv
import urllib.request
import codecs


# Retrieve the file of commons
def retrieve_file(url, input_filename):
    """Checks if URL is available.

    Subjects:
        url: The URL of the file.
        input_filename: The name of the file.

    Returns:
        True if URL is available and then downloads the file, False otherwise.
    """
    try:
        urllib.request.urlopen(url)
        urllib.request.urlretrieve(url, input_filename)
        print(f"File {input_filename} downloaded successfully.")
    except (urllib.error.URLError, TimeoutError):
        print(f"File {input_filename} could not be downloaded.")

def check_file_istat(file):

    """Checks if a file exists.

    Subjects:
        file_path: The full path to the file.

    Returns:
        True if the file exists, False otherwise.
    """
    # Get the path to the current file
    path = os.path.dirname(os.path.abspath(__file__))
    # Build the full path to the file
    # full_path = os.path.join(path, file)
    relative_path = os.getcwd()
    full_path = os.path.join(relative_path, file)
    # Check if the file exists and return true if present
    if os.path.isfile(full_path):
        print(f"File {full_path} exists.")
        return True
    else:
        print(f"File {full_path} does not exist.")
        return False

# Remove istat files
def clean_files(input_filename, output_filename):
    for i in (input_filename, output_filename):
        if os.path.exists(i):
            os.remove(i)

# Reduce the information needed
def extract_columns(file_name, output_filename, column_6, column_20):
    """
    Extract specific columns from a CSV file, skipping the first row.

    Subjects:
        file_name (str): The name of the CSV file.
        column_6 (int): The index of column 6 (zero-based).
        column_19 (int): The index of column 19 (zero-based).
    """

    header1 = "Column 1"
    header2 = "Column 2"

    with open(file_name, 'r', encoding='utf-8', errors='replace') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        # Skip the first row
        next(reader)

        # Open the output file in write mode
        with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # Process each row
            for row in reader:
                # Extract the desired columns
                new_row = [row[column_6].upper(), row[column_20].upper()]
                writer.writerow(new_row)

def add_header_to_csv(csv_file, header_row):
    """
    Adds a header row to a CSV file that doesn't have one.

    Args:
        csv_file (str): Path to the CSV file.
        header_row (list): List of header values.
    """

    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    rows.insert(0, header_row)

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
