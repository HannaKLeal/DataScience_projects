import requests
from bs4 import BeautifulSoup
import time
from random import randint
import csv

with open('e_commerce.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Brand', 'Ratings', 'Title', 'Used', 'Promo',
                         'Price', 'Offers', 'Shipping'])
    # requests to get html file
    response = requests.get('https://www.newegg.com/VR-Headsets/SubCategory/ID-3629')
    content = response.content

    # parse html file
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.prettify())
    time.sleep(randint(2, 3))
    # pages for scraping
    url_list = ['https://www.newegg.com/VR-Headsets/SubCategory/ID-3629',
                'https://www.newegg.com/VR-Headsets/SubCategory/ID-3629/Page-2',
                'https://www.newegg.com/VR-Headsets/SubCategory/ID-3629/Page-3',
                'https://www.newegg.com/VR-Headsets/SubCategory/ID-3629/Page-4']
    for ls in url_list:
        # find all the items
        containers = soup.find_all('div', 'item-container')

        # initiate the for loop
        # to iterate and scrape through
        # every div container that stored in containers
        for container in containers:
            time.sleep(0.2)
            # handling exceptions
            try:
                # locate the first element that matches
                brand = container.find('a', {'class': 'item-brand'}).img['title']
            except Exception as e:
                brand = None

            try:
                ratings = container.find(attrs={'item-rating-num'}).text.strip('()')
            except Exception:
                ratings = None

            # select finds multiple instances and returns a list
            item_title = container.select('.item-title')[0].get_text()

            try:
                # find all the item and return them as a list
                ul_price = container.find_all('ul', {'class': 'item-buying-choices'})
                price_was = ul_price[0].find('strong', class_='item-buying-choices-price').text
            except Exception as e:
                price_was = None

            try:
                promo = container.p.text.strip()
            except Exception as e:
                promo = None

            item_action = container.find('div', {'class': 'item-action'})
            ulTag = item_action.find('ul', {'class': 'price'})
            liTag = ulTag.find_all('li', {'class': 'price-current'})
            for li in liTag:
                strong = li.find('strong').string
                sup = li.find('sup').string
                price = strong + sup
                try:
                    offers = li.find('a').text.strip('()').strip('Offers')
                except Exception as e:
                    offers = 'No offers'

            # grab elements using their siblings
            shipping = liTag[0].find_next_sibling().find_next_sibling().text.strip('Shipping')

            csv_writer.writerow([brand, ratings, item_title,
                                 price_was, promo, price, offers, shipping])
