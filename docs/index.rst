Masterchicken: The original chicken's python pypi package
=========================================================

|PyPI version| |Downloads| |Coverage| |GitHub license|

MasterChicken is a Python package that provides a robust and efficient
way to manage your chicken coop. It offers a comprehensive set of tools
and functionalities that make it easier to monitor and control the
conditions of your chicken coop, ensuring the health and productivity of
your chickens. This amazing package also has an Optimized CSV file
reader which can read .csv files with ease and also has a faster speed
to calculate math than NumPy.

|masterchicken|

.. _-links:

🔗 Links
--------

|GitHub|

|PyPi|

Features
--------

-  Faster speed on calculating math
-  Optimized CSV file reader and writer
-  Various versions of python
-  The Backrooms Game: Noclip to the backrooms and try to escape its
   moist carpet with thousands of infinite rooms to be trapped in, Be
   Careful: Escape with concentration to dodge entities and
   2.1.313,123.2131.23.2
-  Backroom File Extension: can open any .brs file under a second
-  Backrooms engine file load compiler

Chicken Coop Features:
^^^^^^^^^^^^^^^^^^^^^^

-  Health Monitoring: Keep track of the health status of each chicken in
   your coop. The package allows you to record and monitor various
   health parameters, helping you detect any potential health issues
   early.
-  Feed Management: Manage the feeding schedule of your chickens
   effectively. The package enables you to set up and modify feeding
   times, ensuring your chickens are well-fed and healthy.
-  Egg Production Tracking: Monitor the egg production of your chickens.
   The package provides tools to record and analyze egg production data,
   helping you optimize productivity.
-  Environment Control: Control the conditions of your chicken coop. The
   package allows you to adjust parameters like temperature and
   humidity, creating the ideal environment for your chickens.
-  Achievements: The championship of the chicken production

Installation
------------

Masterchicken can be installed via pip:

.. code:: shell

   python.exe -m pip install --upgrade --force masterchicken

Masterchicken can be installed using the '--user' args:

.. code:: shell

   python.exe -m pip install --upgrade --force masterchicken

Installing Masterchicken via the GitHub CLI:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

   gh repo clone PythonChicken123/masterchicken

.. code:: bash

   cd /masterchicken

.. code:: bash

   python.exe setup.py

Installing Masterchicken via Docker:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Release upcoming for Docker
'''''''''''''''''''''''''''

Examples
--------

-  `Basic Coop <#basic-coop>`__
-  `Reading CSV <#reading-csv>`__
-  `Writing CSV <#writing-csv>`__
-  `Converting CSV <#webhook-with-embedded-content>`__
-  `Edit Webhook Message <#edit-webhook-messages>`__
-  `Delete Webhook Message <#delete-webhook-messages>`__
-  `Send Files <#send-files>`__
-  `Remove Embeds and Files <#remove-embeds-and-files>`__
-  `Allowed Mentions <#allowed-mentions>`__
-  `Use Proxies <#use-proxies>`__
-  `Timeout <#timeout>`__
-  `Async Support <#async-support>`__

Basic Coop
----------

.. code:: python

   from masterchicken import Coop
      
   coop = Coop.Coop()
   chicken = coop.create(type='egg')
   chicken.hatch()
   if chicken.get_hatched():
       print("Congratulations!! You have hatched a chicken")

   if __name__ == '__main__':
       print(f"Chicken Stats: {chicken.get_status}")

Reading CSV
-----------

.. code:: python

   from masterchicken.OpenCSV import *
   import numpy as np

   # Path to CSV file
   file_path = 'map/chicken.csv'
   group_by_column = 'token_id'
   # TODO: Rewrite all of the columns in the CSV file on columns_to_print
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

Writing CSV
-----------

.. code:: python

   from masterchicken.OpenCSV import *
   import numpy as np

   if __name__ == '__main__':
       # Path to the CSV file
       file_path = 'map/chicken.csv'
       group_by_column = 'token_id'
       # TODO: Rewrite all of the columns in the CSV file on columns_to_print
       columns_to_print = np.array(
           ['chicken_name', 'breed', 'type', 'hatch_date', 'token_id', 'achievements', 'collections',
            'flying_eligibility', 'current_health', 'max_health', 'abilities', 'age'])
       data_frame = read_csv(file_path, delimiter=',', quotechar='"', encoding='utf-8', skiprows=0,
                             group_by=group_by_column, columns_to_print=None, group_entire_print=False)
       if data_frame is not None:
           type_column_as_list = data_frame['breed'].tolist()
           print(type_column_as_list)
           write_csv(data_frame, column='chicken_name', row=1, value='Pyrastra', file_path=file_path)
           print(data_frame['chicken_name'].tolist())

.. |PyPI version| image:: https://badge.fury.io/py/masterchicken.svg
   :target: https://badge.fury.io/py/masterchicken
.. |Downloads| image:: https://img.shields.io/badge/Downloads-50M%2B-blue
   :target: https://pypi.org/project/masterchicken/#files
.. |Coverage| image:: https://img.shields.io/badge/coverage-100%25-brightgreen
   :target: https://organicchicken.netlify.app
.. |GitHub license| image:: https://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: https://github.com/PythonChicken123/masterchicken/blob/main/LICENSE
.. |masterchicken| image:: ./masterchicken.png
   :target: https://pypi.org/project/masterchicken/
.. |GitHub| image:: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
   :target: https://github.com/PythonChicken123/masterchicken/
.. |PyPi| image:: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
   :target: https://github.com/PythonChicken123/masterchicken/
