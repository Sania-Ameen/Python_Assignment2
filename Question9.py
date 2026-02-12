# extract tubular data from a webpage and store it in a structured format

# import requests and BeautifulSoup and pandas (to save into .csv)
import requests
from bs4 import BeautifulSoup
import pandas as pd

# using headers as 'user-agent' to allow requests from website
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/124.0.0.0 Safari/537.36"}

# get the url from given wikipedia website
machine_learning_wikipedia_url = "https://en.wikipedia.org/wiki/Machine_learning"

# download the page onto the program
html_content_of_machine_learning_url = requests.get(machine_learning_wikipedia_url, headers=headers).text

# parse HTML text using BeautifulSoup
machine_learning_html_parsing = BeautifulSoup(html_content_of_machine_learning_url, "html.parser")

# locate the first table inside the main content area
machine_learning_content_div= machine_learning_html_parsing.find("div", id="mw-content-text")

# find all the tables inside the main content area
all_tables_inside_main_content_area = machine_learning_content_div.find_all("table")

# using a for loop, find the first table with at least 3 rows of data
for table in all_tables_inside_main_content_area:
    rows_of_tables = table.find_all("tr")
    data_rows = [row for row in rows_of_tables if row.find_all("td")]
    if len(data_rows) >=3:
        main_table = table
        break

# extract the headers
header_cells_of_table = main_table.find("tr").find_all("th")
if header_cells_of_table:
    headers = [th.get_text(strip=True) for th in header_cells_of_table]
# if there are no headers, create them (col1, col2, col3, etc.)
else:
    first_data_row = main_table.find("tr").find_all("td")
    added_headers = [f"col{i+1}" for i in range(len(first_data_row))]

# extract the table data and put into a new csv file
data_from_table =[]
for row in main_table.find_all("tr"):
    cells_in_table = row.find_all(["td","th"])
    row_data = [cell.get_text(" ",strip=True) for cell in cells_in_table]
    # any missing cells should be padded
    while len(row_data) < len(headers):
        row_data.append("") # add empty strings until the row is the sane length as the header
    if row_data:
        data_from_table.append(row_data)

# save to new csv
# skip over the header row in data_from_table
extracted_table_dataset_to_dataframe = pd.DataFrame(data_from_table[1:], columns = headers)
# ensure everything is saved correctly (no extra symbols or row indices)
# encoding and index = False
extracted_table_dataset_to_dataframe.to_csv("wiki_table.csv", index = False, encoding="utf-8")

# print final output message
print("The extracted table dataset is now saved to wiki_table.csv ")