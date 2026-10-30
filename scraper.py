import requests

# Beautiful soup allows you to find an element by its ID
from bs4 import BeautifulSoup
import random

# Headers disguise the bot as a normal user browsing the site.
# Without it the site can recognise the bot and flag a 403 error

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrapeWikiArticle(url):
    response = requests.get(
        url = url,
        headers= headers
)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    if title:
        print(title.text)  


    # Getting all the links
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)

    for link in allLinks:
        # only wiki ARTICLE  
        href = link.get("href", "")
        if href.startswith("/wiki/"):
            next_url = "https://en.wikipedia.org" + href
            scrapeWikiArticle(next_url)
            break
        
scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")


