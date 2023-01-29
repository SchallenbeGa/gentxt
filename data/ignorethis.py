import requests, random
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Example; Intel Mac OS X 10_09_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'content-type': 'text/html',
    'accept-language': 'en-US',
    'accept-encoding': 'gzip, deflate',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}

data = []
pages =["je-suis","dans-l-attente"]
for page in pages:
    url = f"example.com"
    print(url)
    results = requests.get(url,headers=headers)
    soup = BeautifulSoup(results.content, "html.parser")
    for bookSection in soup.select('[class*="col-md-example"]'):
        print(bookSection)
        data.append({
            'text':bookSection.find("p", id_="cs-source-text-example").get()
        })
    books = pd.DataFrame(data)

    books.to_csv("scrp.csv", index=False, header=True,encoding = 'utf-8-sig')