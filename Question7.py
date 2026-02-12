# extracting structured content from a webpage using Beautiful Soup

# import requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

# using headers as 'user-agent' to allow requests from website
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/124.0.0.0 Safari/537.36"}

# get the url from given wikipedia website
data_science_wikipedia_url = "https://en.wikipedia.org/wiki/Data_science"

# download the page onto the program
html_content_of_data_science_url = requests.get(data_science_wikipedia_url, headers=headers).text

# parse HTML text using BeautifulSoup
data_science_html_parsing = BeautifulSoup(html_content_of_data_science_url, "html.parser")

# extract and print the page title
title_of_data_science_article = data_science_html_parsing.title.text
print("The page title is:", title_of_data_science_article)

# extract the first paragraph from the main article content using ID
# get content from page
data_science_article_content = data_science_html_parsing.find("div", id="mw-content-text")

# get the first paragraph with st least 50 characters after stripping whitespace
first_paragraph = ""
for p in data_science_article_content.find_all("p"):
    text_inside_tag = p.get_text
    text_inside_tag = ' '.join(p.get_text().split()) # remove any extra spaces that exist in the outcome paragraph
    if len(text_inside_tag) >= 50:
        first_paragraph = text_inside_tag
        break # break the loop once the first instance of the condition is met

# print the first paragraph
print(first_paragraph)