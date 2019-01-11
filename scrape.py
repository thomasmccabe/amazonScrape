import requests
from bs4 import BeautifulSoup as bsoup
import json

page = requests.get("https://www.amazon.com/Mpow-Microphone-Cancelling-Lightweight-Headphones/dp/B06XWG12QS/ref=sr_1_7?ie=UTF8&qid=1547074182&sr=8-7&keywords=phone+headset")
print(page.status_code)

urls = ['https://www.amazon.com/Mpow-Microphone-Cancelling-Lightweight-Headphones/dp/B06XWG12QS/ref=sr_1_7?ie=UTF8&qid=1547074182&sr=8-7&keywords=phone+headset']
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36'}

for url in urls:
    response = requests.get(url, headers = headers)
    soup = bsoup(response.content, 'html.parser')
    infoTitle = soup.find('h1', class_ = 'a-size-large a-spacing-none')
    infoPrice = soup.find('span', class_ = 'a-size-medium a-color-price')
    infoTable = soup.find('table', class_ = 'a-keyvalue prodDetTable')

    with open ('amzndata.txt', 'a') as r:
        r.write("-----------------------------------------------------------\n")
        r.write("Product Name: " + infoTitle.get_text().strip() + '\n')
        r.write("Product Price: " + infoPrice.get_text().strip() + '\n')
        for row in infoTable.find_all('tr'):
            for cell in row.find_all('th'):
                if cell.get_text().strip() == "Item Weight":
                    for cell in row.find_all('td'):
                        r.write("Product Weight: " + cell.get_text().strip() + '\n')
                if cell.get_text().strip() == "Product Dimensions":
                    for cell in row.find_all('td'):
                        r.write("Product Dimensions: " + cell.get_text().strip() + '\n')
