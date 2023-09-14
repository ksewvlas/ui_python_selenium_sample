# ui_python_selenium_sample
This repository contains automated UI tests using the Selenium library and the Pytest framework for the site https://www.saucedemo.com/

These tests are designed to validate the functionality of a web application through automated interactions with the user interface as sample.

## Installation

1. Install the required Python packages using pip:  
``pip install -r requirements.txt``

## Running tests
1. For running tests use the command:  
``pytest -s -v``

## Generating reports
1. For generating a test report in Allure use the command:  
``pytest --alluredir=test_results/``
2. For open generated report use the command:  
``allure serve test_results/``

