import urllib2
from bs4 import BeautifulSoup


def get_litecoin_price_from():

    litecoin_url = 'https://coinmarketcap.com/currencies/litecoin/'

    page = urllib2.urlopen(litecoin_url).read()

    soup = BeautifulSoup(page, 'lxml')

    litecoin_price = soup.find_all('span',class_='text-large2')

    for a in litecoin_price:
         return "${}".format(a.text)

def get_xr_price_from():

    ripple_url = 'https://coinmarketcap.com/currencies/ripple/'

    page = urllib2.urlopen(ripple_url).read()

    soup = BeautifulSoup(page, 'lxml')

    ripple_price = soup.find_all('span', class_='text-large2')

    for xr in ripple_price:
        return "${}".format(xr.text)
