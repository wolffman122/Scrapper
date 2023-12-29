import requests as r
import bs4
import mysql.connector



base_url = 'https://www.amazon.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

base_response = r.get(base_url, headers=headers )

cookies = base_response.cookies

mydb = mysql.connector.connect(
    host="localhost",
    user="scrapper",
    password='Scrapper#1322'
)

print(mydb)

TestDic = {'WD': ['B07B1HX5KN', 'B07D3N95GS', 'B084F34HZ6', 'B07RTMPWD8', 'B0CD2XBZWR', 'B08K3VVKSW', 'B08K3TFM92', 'B09TBF6GHJ', 'B0B5W1CQ8W'],
           'SG': ['B0B94R72J5', 'B0B94MX35D', 'B0B94M13NH', 'B0B94NQCV5', 'B0B94KSFTH', 'B0B94P481H', 'B0B94PNF7P', 'B0B94MRX2H', 'B0B94MF4LP', 'B0B94NBBJH']
           }

#Seagate_Codes = ['B0B94R72J5', 'B0B94MX35D', 'B0B94M13NH', 'B0B94NQCV5', 'B0B94KSFTH', 'B0B94P481H', 'B0B94PNF7P', 'B0B94MRX2H', 'B0B94MF4LP', 'B0B94NBBJH']
#WD_Codes = ['B07B1HX5KN', 'B07D3N95GS', 'B084F34HZ6', 'B07RTMPWD8', 'B0CD2XBZWR', 'B08K3VVKSW', 'B08K3TFM92', 'B09TBF6GHJ', 'B0B5W1CQ8W']

#Brand_Codes = ['WD', 'SG']

for brand in TestDic:
    print(brand)
    for product_code in TestDic[brand]:
        url = f'https://www.amazon.com/gp/aw/d/{product_code}/'
        product_response = r.get(url, headers=headers, cookies=cookies)
        soup = bs4.BeautifulSoup(product_response.text, 'lxml')
        titles = soup.find_all(class_="a-size-large product-title-word-break")
        dollar_lines = soup.find_all(class_="a-price-whole")
        decimal_lines = soup.find_all(class_="a-price-fraction")
        
        if titles:
            title = titles[0].text
            tbIndex = title.find('TB')
            
            if tbIndex > 0:
                if brand == 'WD':
                    dataSize = title[tbIndex - 2: tbIndex]
                elif brand == 'SG':
                    dataSize = title[tbIndex - 3: tbIndex -1]
                
                price = dollar_lines[0].text + decimal_lines[0].text
                pricePerTB = float(price) / float(dataSize)
                price = f'{dataSize}TB: {dollar_lines[0].text}{decimal_lines[0].text} : {pricePerTB}'
                print(price)
