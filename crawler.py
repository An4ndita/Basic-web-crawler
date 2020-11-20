# importing modules
import requests
import re
import urlparse

# Input domain for crawling
url = raw_input("Enter the domain >> ")
links = []

# function for extracting links from the target website
def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

# function for crawling
def crawl(target_url):
    href_links = extract_links_from(target_url)
    for link in href_links:
        link = urlparse.urljoin(target_url, link)

        if "#" in link:
            link = link.split("#")[0]

        if url in link and link not in links:
            links.append(link)
            print(link)
            crawl(link)

# exit
try:
    crawl(str(url))
except KeyboardInterrupt:
    print("\rCtrl+c detected...... Quitting.......!!!")
    exit(0)
