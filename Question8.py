# extracting structured heading information from a webpage

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

# extract all <h2> section headings from the main content area
data_science_article_headings = data_science_html_parsing.find("div", id="mw-content-text")

# find all the h2 headings inside the main content of the article
# do not include headings containing words
# remove any [edit] text from headings

# create an empty list for all valid headings
valid_headings = []
# loop through and find valid headings to append to list
for h2 in data_science_article_headings.find_all("h2"):
    # remove any whitespace
    text_inside_tag = h2.get_text(strip=True)
    # remove any [edit] text from headings (replace with blank)
    text_inside_tag = text_inside_tag.replace("[edit]", "")

    # handle all other cases with unwanted headings
    # append all valid headings into the empty list
    if ("References" in text_inside_tag or
    "External links" in text_inside_tag or
    "See also" in text_inside_tag or
    "Notes" in text_inside_tag):
        continue
    else:
        valid_headings.append(text_inside_tag)

# save everything into a new text file
with open("headings.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(valid_headings))
    