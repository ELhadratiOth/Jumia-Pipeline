# Jumia Scraper and Data Loader

This project involves scraping product data from Jumia using BeautifulSoup and Python, and then loading that data into a PostgreSQL database.

## Workflow

1. **Scrape Data:**
   - **File:** `scrapper.py`
   - **Description:** Uses BeautifulSoup to scrape product information from Jumia and saves the data to a CSV file.

   ```bash
   python scrapper.py
Load Data into PostgreSQL:

File: csv2postgresql.py
Description: Reads the CSV file created by the scraper and loads the data into a PostgreSQL database. Configuration settings are managed via an .ini file for easy customization.
bash
Copier le code
python csv2postgresql.py
Configuration
An .ini file is provided for configuring the database connection and search parameters. Make sure to update it with your PostgreSQL connection details and any product search parameters you want to use.
Setup
Install Required Packages: Ensure you have all required Python packages installed. You can install them using:

bash
Copier le code
pip install -r requirements.txt
Update Configuration File: Edit the .ini file with your database connection details and any product search parameters.

Run the Scraper: Execute scrapper.py to scrape data and generate the CSV file.

bash
Copier le code
python scrapper.py
Load Data into PostgreSQL: Execute csv2postgresql.py to import the CSV data into the PostgreSQL database.

bash
Copier le code
python csv2postgresql.py
Requirements
Python 3.x
BeautifulSoup
PostgreSQL
psycopg2 (or an appropriate PostgreSQL adapter for Python)
Notes
Ensure your PostgreSQL server is running and accessible.
Verify that the CSV file path and PostgreSQL connection details are correctly specified in the .ini file.
css
Copier le code

This Markdown code provides a structured overview of the project, including instructions for
