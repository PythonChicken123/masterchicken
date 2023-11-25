from numba import jit

try:
    import taichi as ti
    import pandas as pd
    import numpy
    import csv
    import sys
    import time
    import warnings
    import math
    import random
except:
    import subprocess

    subprocess.check_call(['pip', 'install', 'numpy'])
    subprocess.check_call(['pip', 'install', 'upgrade', 'pandas'])
    subprocess.check_call(['pip', 'install', 'csv'])
    subprocess.check_call(['pip', 'install', 'sys'])
    subprocess.check_call(['pip', 'install', 'os'])
    subprocess.check_call(['pip', 'install', 'time'])
    subprocess.check_call(['pip', 'install', 'numba'])
    subprocess.check_call(['pip', 'install', 'numpy'])
    subprocess.check_call(['pip', 'install', 'warnings'])
    subprocess.check_call(['pip', 'install', 'math'])
    subprocess.check_call(['pip', 'install', 'random'])

"""
Importing CSV file for mapping
= Field names: 0 = chicken's name; 1 = type; 2 = hatched; 3 = Token
"""

ti.init(arch=ti.cpu, default_ip=ti.i64)

time_int = 0
matrix_basemap = []


def control_basemap(row_field_names):
    print("Updating base map")
    list.append(matrix_basemap, row_field_names)
    print(matrix_basemap)
    print(row_field_names)


def update(get_requirements, file_name, number_to_check=0, force_open=False):
    """
    :param force_open:
    :param file_name:
    :param get_requirements:
    :type number_to_check: str
    :type force_open: bool
    """
    file_field_names = numpy.array(['chicken_name', 'type', 'hatch_date', 'token_id', 'achievements', 'collections',
                                    'flying_eligibility', 'drumstick_value'])
    with open(f'map/{file_name}', mode='r', newline='') as csv_map:
        csv_main_reader = csv.DictReader(csv_map, fieldnames=file_field_names)
        df = pd.read_csv(f'map/{file_name}', header=None, names=file_field_names)
        for row in csv_main_reader or df.iterrows():
            if row == file_field_names.any:
                if force_open:
                    if get_requirements != row[number_to_check]:
                        raise ValueError(f"Invalid field name: {get_requirements}")
                    elif get_requirements == ('true' or 'false' or True or False):
                        print(file_field_names[number_to_check] + ': ')
                        print()  # New line
                    else:
                        warnings.resetwarnings()
                        print(f"Successfully set {file_name.upper()}")
                else:
                    raise SystemExit(f"Unable to find the file: {file_name}")
                    time.sleep(0)
            elif row[file_field_names[number_to_check]] != get_requirements:
                if row[file_field_names[number_to_check]] != file_field_names[number_to_check]:
                    row_field_names = row[file_field_names[number_to_check]]
                    control_basemap(row_field_names)
            elif force_open:
                ti.warn(f"Unable to find {get_requirements} while formatting {get_requirements.upper()}!")
                raise UserWarning(f"Invalid get_requirements: {get_requirements} not found in {file_name}")
            pass
        pass
    if force_open and not warnings.warn:
        raise ValueError('Invalid field names')
        sys.exit()
    pass


pass


class Open:
    def __init__(self):
        self.force_open = False
        self.open = None
        self.filename = None
        self.file_field_names = ti.field(dtype=ti.i32, shape=8)
        self.matrix_basemap = ti.field(ti.i64, shape=(1000, 1000))

    def open_file(self, get_file_name):
        self.filename = get_file_name.lower()
        self.force_open = True  # If true then force the file to open and read
        print('Collecting File: ', self.filename)  # Print the following file
        print(' ')  # Leave a line
        update(get_file_name, self.filename, number_to_check=6, force_open=self.force_open)

    @staticmethod
    @jit(nopython=True)
    def get_rand_cal(n: ti.i32) -> ti.f32:
        z = 0
        for i in range(n):
            x = ti.random()
            y = ti.random()
            z += ti.pow(x, y-2)
        return z

    @staticmethod
    @jit(fastmath=True)
    def get_rand_calculation(n: ti.i32) -> ti.f32:
        z = 0.0
        for i in range(n):
            x = ti.random()
            y = ti.random()
            z += ti.pow(x, y-2)
        return z


if __name__ == '__main__':
    start = time.time()
    Get_File = Open()
    Get_File.open_file(
        'CHICKEN.CSV')  # Can stil read the file even if the name is in CAPS and if the force_open is True
    end = time.time()
    print(end - start)
