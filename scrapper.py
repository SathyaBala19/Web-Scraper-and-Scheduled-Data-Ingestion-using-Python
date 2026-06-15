import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import logging

url = "https://quotes.toscrape.com/"

response = requests.get(url, timeout=10)

data = []

try:
 if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    quote_blocks = soup.find_all("div", class_="quote")

    for block in quote_blocks:
        quote = block.find("span", class_="text").text
        author = block.find("small", class_="author").text

        data.append({
            "quote": quote,
            "author": author
        })

    df = pd.DataFrame(data)

    os.makedirs("data", exist_ok =True)

    logging.basicConfig(
        filename='logs/scraper.log',
        level = logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    today = datetime.now().strftime("%Y-%m-%d")
    df.to_csv(f"data/quotes_{today}.csv", index=False)
    
    logging.info("Data saved successfully")
    print("Data saved successfully")


 else:
    logging.error(f"Failed to connect. Status code: {response.status_code}")
    print("Failed to Connect")

except Exception as e:
   logging.error(f"Error occured: {e}")
   print("Error occured: ",e)