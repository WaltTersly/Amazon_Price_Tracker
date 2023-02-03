import requests
import lxml
from bs4 import BeautifulSoup
from Notifications import NotificationsManager


BUY_PRICE = 35


url = "https://www.amazon.com/Study-Bible-Hardcover-Full-Color-Comfort/dp/0785220623/ref=sr_1_22?crid=AQCLOT1RS6S0&keywords=bible&qid=1675341439&sprefix=bible%2Caps%2C448&sr=8-22"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=header)

notification = NotificationsManager()

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-color-base").getText()
title = soup.find(name="span", class_="a-size-extra-large").getText().strip()
# print(title)
strip_price = float(price.split("$")[1])
# print(strip_price)

if strip_price < BUY_PRICE:
    message = f"{title} is now {strip_price} at  {url}"
    notification.send_email(message)

