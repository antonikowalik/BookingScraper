from bs4 import BeautifulSoup
import requests

url = "https://www.booking.com/hotel/pl/happy-tower.html"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select("script[data-capla-store-sata='apollo']")
review = reviews.pop(-1)
print(review)