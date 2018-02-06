import urllib2
from bs4 import BeautifulSoup



def get_bitcoin_price_from():

    bitcoin_url = 'https://coinmarketcap.com/currencies/bitcoin/'

    page = urllib2.urlopen(bitcoin_url).read()

    soup = BeautifulSoup(page,'lxml')

    bc_price = soup.find_all('span',class_='text-large2')

    for value in bc_price:
        return "${}".format(value.text)


def get_litecoin_price_from():

    litecoin_url = 'https://coinmarketcap.com/currencies/litecoin/'

    page = urllib2.urlopen(litecoin_url).read()

    soup = BeautifulSoup(page, 'lxml')

    litecoin_price = soup.find_all('span',class_='text-large2')

    for value in litecoin_price:
         return "${}".format(value.text)



def get_xr_price_from():

    ripple_url = 'https://coinmarketcap.com/currencies/ripple/'

    page = urllib2.urlopen(ripple_url).read()

    soup = BeautifulSoup(page, 'lxml')

    ripple_price = soup.find_all('span', class_='text-large2')

    for value in ripple_price:
        return "${}".format(value.text)
