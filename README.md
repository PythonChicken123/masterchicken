
# Masterchicken: The original chicken's python pypi package

[![PyPI version](https://badge.fury.io/py/masterchicken.svg)](https://badge.fury.io/py/masterchicken)
[![Downloads](https://img.shields.io/badge/Downloads-50M%2B-blue)](https://pypi.org/project/masterchicken/#files)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://organicchicken.netlify.app)
[![GitHub license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/PythonChicken123/masterchicken/blob/main/LICENSE)

MasterChicken is a Python package that provides a robust and efficient way to manage your chicken coop. It offers a comprehensive set of tools and functionalities that make it easier to monitor and control the conditions of your chicken coop, ensuring the health and productivity of your chickens. This amazing package also has an Optimized CSV file reader which can read .csv files with ease and also has a faster speed to calculate math than NumPy.

[![masterchicken](./masterchicken.png)](https://pypi.org/project/masterchicken/)


## 🔗 Links
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/PythonChicken123/masterchicken/)

[![PyPi](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://github.com/PythonChicken123/masterchicken/)

## Features

- Faster speed on calculating math
- Optimized CSV file reader and writer
- Various versions of python
- The Backrooms Game: Noclip to the backrooms and try to escape its moist carpet with thousands of infinite rooms to be trapped in, Be Careful: Escape with concentration to dodge entities and 2.1.313,123.2131.23.2
- Backroom File Extension: can open any .brs file under a second
- Backrooms engine file load compiler

#### Chicken Coop Features:
- Health Monitoring: Keep track of the health status of each chicken in your coop. The package allows you to record and monitor various health parameters, helping you detect any potential health issues early.
- Feed Management: Manage the feeding schedule of your chickens effectively. The package enables you to set up and modify feeding times, ensuring your chickens are well-fed and healthy.
- Egg Production Tracking: Monitor the egg production of your chickens. The package provides tools to record and analyze egg production data, helping you optimize productivity.
- Environment Control: Control the conditions of your chicken coop. The package allows you to adjust parameters like temperature and humidity, creating the ideal environment for your chickens.

## Installation

Masterchicken can be installed via pip:
```shell
python.exe -m pip install --upgrade --force masterchicken
```
Masterchicken can be installed using the '--user' args:
```shell
python.exe -m pip install --upgrade --force masterchicken
```
#### Installing Masterchicken via the GitHub CLI:
```bash
gh repo clone PythonChicken123/masterchicken
```
```bash
cd /masterchicken
```
```bash
python.exe setup.py
```
#### Installing Masterchicken via Docker:
##### Release upcoming for Docker

## Examples
* [Basic Coop](#basic-coop)
* [Basic CSV](#basic-csv)
* [Manage Being Rate Limited](#manage-being-rate-limited)
* [Embedded Content](#webhook-with-embedded-content)
* [Edit Webhook Message](#edit-webhook-messages)
* [Delete Webhook Message](#delete-webhook-messages)
* [Send Files](#send-files)
* [Remove Embeds and Files](#remove-embeds-and-files)
* [Allowed Mentions](#allowed-mentions)
* [Use Proxies](#use-proxies)
* [Timeout](#timeout)
* [Async Support](#async-support)


## Basic Coop

```python
from masterchicken import Coop
   
coop = Coop.Coop()
chicken = coop.create(type='egg')
chicken.hatch()
if chicken.get_hatched():
    print("Congratulations!! You have hatched a chicken")

if __name__ == '__main__':
    print(f"Chicken Stats: {chicken.get_status}")
```

### Basic CSV

```python
from masterchicken.csv import read_csv
import numpy as np

file_path = 'map/chicken.csv'
group_by_column = 'token_id'
columns_to_print = np.array(['chicken_name', 'type', 'hatch_date', 'token_id', 'achievements', 'collections',
                             'flying_eligibility', 'drumstick_value'])

if __name__ == '__main__':
    
    data_frame = read_csv(file_path, delimiter=',', quotechar='"', encoding='utf-8', skiprows=0,
                          group_by=group_by_column, columns_to_print=None, group_entire_print=False)
    if data_frame is not None:
        # Convert 'type' column to a list and print
        type_column_as_list = data_frame['type'].tolist()
        print(type_column_as_list)
        print("1. type: " + type_column_as_list[1])
        print("2. type: " + type_column_as_list[2])

```