import csv
import requests
from bs4 import BeautifulSoup

# specify the search query
query = 'inurl:"view_items.php?id="'

# make the request to Google
response = requests.get(f"https://www.google.com/search?q={query}")

# parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# create an empty list to store the URLs
search_results = []

# extract the URLs from the HTML
for result in soup.find_all('a'):
    link = result.get('href')
    if 'http' in link and 'view_items' in link:
        search_results.append(link)

# write the URLs to a CSV file
with open("search_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for url in search_results:
        writer.writerow([[url]])
