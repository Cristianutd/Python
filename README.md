**Python Challenge**
====

**Installation Instructions**
=
Below you will find the list of commands you need to run in order to install all the dependencies to run the automated tests. It is important to run all the commands in the root path of the project.

- Install pytest: `pip install pytest`

- Install pandas: `pip install pandas`

- Install panda_schema: `pip install pandas-schema`

Packages:

`attrs           22.1.0`
`exceptiongroup  1.0.0`
`iniconfig       1.1.1`
`numpy           1.23.4`
`packaging       21.3`
`pandas          1.5.1`
`pandas-schema   0.3.6`
`pip             22.3`
`pluggy          1.0.0`
`pyparsing       3.0.9`
`pytest          7.2.0`
`python-dateutil 2.8.2`
`pytz            2022.6`
`setuptools      60.2.0`
`six             1.16.0`
`tomli           2.0.1`
`wheel           0.37.1`


**Tests**
=
The tests have been grouped in 3 different test classes:

- test_header_field.py
- test_product_field.py
- test_source_field.py

Each test class contains one test case in order to validate each field that is present in the `elastic_data.json` file.

Please make sure the `elastic_data.json` file is in the `test_data` folder before executing the tests.

**How to run the tests**
=
In order to run the tests in the console, you can use the following commands:

- pytest -s test_header_fields.py
- pytest -s test_product_fields.py
- pytest -s test_source_fields.py

At the end of the execution the file `output_errors.csv` will be written in the `test_data` folder, please check the folder.
