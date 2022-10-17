from bs4 import BeautifulSoup
import requests
import lxml

# put the configuration in the zillow website than copy the link here 
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

HEADER = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
}


class Scrapper:
    def __init__(self):
        self.response = requests.get(url=ZILLOW_URL, headers=HEADER).text
        self.soup = BeautifulSoup(self.response, "lxml")

    def get_data(self):
        data = self.soup.select("span[data-test='property-card-price']")
        prices = [price.getText()[:6] for price in data]
        address = self.soup.select(selector=".StyledPropertyCardDataWrapper-c11n-8-73-8__sc-1omp4c3-0.gXNuqr.property-card-data a")
        links = [site.get(key="href") if "https://www.zillow.com" in site.get(key="href") else "https://www.zillow.com" + site.get(key="href") for site in address]
        address = [addr.getText() for addr in address]
        return address, prices, links
