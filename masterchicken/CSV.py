# encoding=UTF-8
from functools import wraps, lru_cache
import importlib
import subprocess
import sys
import csv
import pandas as pd
import numpy as np

# List of required libraries
required_libraries = ['numpy', 'pandas', 'csv']

# Check if required libraries are installed and install them if missing
missing_libraries = []
for lib in required_libraries:
    try:
        importlib.import_module(lib)
    except ModuleNotFoundError:
        missing_libraries.append(lib)

if missing_libraries:
    print(f"The following required libraries are missing and will be installed: ")
    for lib in missing_libraries:
        print(lib)
    try:
        for lib in missing_libraries:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', lib])
        print(f"Installation complete.")
    except Exception as e:
        print(f"An error occurred while installing the required libraries: {str(e)}")
        sys.exit(1)

# Memoization cache
memoization_cache = {}


@lru_cache(maxsize=None)
def memoize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (func, args, frozenset(kwargs.items()))
        if key in memoization_cache:
            return memoization_cache[key]
        result = func(*args, **kwargs)
        memoization_cache[key] = result
        return result

    return wrapper


@memoize
def read_csv(file_path, delimiter=',', quotechar='"', encoding='utf-8', skiprows=None, filters=None,
             group_by=None, columns_to_print=None, group_entire_print=False, **kwargs):
    """
    Read a CSV file using advanced options.

    Parameters:
    - file_path (str): The path to the CSV file.
    - delimiter (str): The character used to separate fields.
    - quotechar (str): The character used to denote the start and end of a quoted item.
    - encoding (str): The encoding of the file.
    - skiprows (list or int): Rows to skip while reading.
    - filters (dict): A dictionary of column-value pairs to filter the data.
    - group_by (str): The column by which to group the data.
    - columns_to_print (list): A list of column names to print.
    - **kwargs: Additional keyword arguments to be passed to pandas.read_csv.

    Returns:
    - pd.DataFrame: A Pandas DataFrame containing the CSV data.
    :return:
    :param group_entire_print:
    :param columns_to_print:
    :param group_by:
    :param filters:
    :param skiprows:
    :param encoding:
    :param quotechar:
    :param delimiter:
    :type file_path: file
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            csv_reader = csv.reader(file, delimiter=delimiter, quotechar=quotechar)
            if skiprows is not None:
                for _ in range(skiprows):
                    next(csv_reader)

            # Read the first row to get column names
            all_columns = next(csv_reader)

            # Read data into a list of dictionaries
            data = [dict(zip(all_columns, row)) for row in csv_reader]

        df = pd.DataFrame(data)

        # Apply additional filters
        if filters is not None:
            def filter_df(df, column, value):
                if column not in df.columns:
                    raise ValueError(f"Filter column '{column}' not found in CSV columns.")
                return df[df[column] == value]

            df = map(lambda item: filter_df(df, *item), filters.items())

        # Group by the specified column
        if group_by is not None:
            grouped_df = df.groupby(group_by)

            # Print each group separately
            for name, group in grouped_df:
                if group_entire_print:
                    print(f"Group {name}:")
                    print(group[columns_to_print if columns_to_print is not None else slice(None)])

        return df
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None


@memoize
def write_csv(data_frame: pd.DataFrame, file_path: str, index: bool = False, **kwargs) -> None:
    """
    Write a Pandas DataFrame to a CSV file.

    Parameters:
    - data_frame (pd.DataFrame): The DataFrame to be written to the CSV file.
    - file_path (str): The path to the CSV file.
    - index (bool): Whether to write row names (index).
    - **kwargs: Additional keyword arguments to be passed to pandas.DataFrame.to_csv.

    Returns:
    - None
    """
    try:
        data_frame.to_csv(file_path, index=index, **kwargs)
        print(f"DataFrame successfully written to {file_path}.")
    except Exception as e:
        print(f"An error occurred while writing the DataFrame to CSV: {e}")


if __name__ == '__main__':
    file_path = 'map/chicken.csv'
    group_by_column = 'token_id'
    columns_to_print = np.array(['chicken_name', 'type', 'hatch_date', 'token_id', 'achievements', 'collections',
                                 'flying_eligibility', 'drumstick_value'])
    data_frame = read_csv(file_path, delimiter=',', quotechar='"', encoding='utf-8', skiprows=0,
                          group_by=group_by_column, columns_to_print=None, group_entire_print=False)
    if data_frame is not None:
        # Convert 'type' column to a list and print
        type_column_as_list = data_frame['type'].tolist()
        print(type_column_as_list)
        print("1. type: " + type_column_as_list[1])
        print("2. type: " + type_column_as_list[2])
