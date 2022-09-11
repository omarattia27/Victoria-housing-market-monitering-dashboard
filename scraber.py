import requests
import time
import pandas as pd 
from bs4 import BeautifulSoup

# base URL for the Kijiji website
base_url = "https://www.kijiji.ca"

# URL for the first page
page_1_url = base_url + '/b-apartments-condos/victoria-bc/c37l1700173' 

# use requests library to get respo
response = requests.get(page_1_url)

# use BS to parse the text of the HTML response
soup = BeautifulSoup(response.text, "lxml")

# find the number of pages, and the number of ads per page
number_of_pages = soup.find("span", attrs={"class": ["resultsShowingCount-1707762110"]})
results = [int(s) for s in number_of_pages.text.split() if s.isdigit()]

print(results)
# 

number_of_pages =round(results[2]/results[1])
count = 0

for page in range(number_of_pages):
    base_url = "https://www.kijiji.ca"

    # URL for the first page
    page_1_url = base_url + '/b-apartments-condos/victoria-bc/page-'+ str(page) +'/c37l1700173' 

    # use requests library to get respo
    response = requests.get(page_1_url)

    # use BS to parse the text of the HTML response
    soup = BeautifulSoup(response.text, "lxml")

    ads = soup.find_all("div", attrs={"class": ["search-item", "regular-ad"]})
    for ad in ads:
        texts_to_print = ad.find_all("div", {"class": "description"})
        for element in texts_to_print:
            pass
            #print(element.text.replace('\n',''))
            #print("---------------------------------------------------------------------------------------------------------------")
            count+=1
print(count)