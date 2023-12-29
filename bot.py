import requests as r
import bs4



base_url = 'https://www.amazon.com'
url = 'https://www.amazon.com/gp/aw/d/B084ZV4DXB/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

base_response = r.get(base_url, headers=headers )
print(base_response)

cookies = base_response.cookies

product_response = r.get(url, headers=headers, cookies=cookies)
soup = bs4.BeautifulSoup(product_response.text, 'lxml')
dollar_lines = soup.find_all(class_="a-price-whole")
decimal_lines = soup.find_all(class_="a-price-fraction")

price = f'{dollar_lines[0].text}{decimal_lines[0].text}'
print(price)
