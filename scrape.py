import urllib2
from bs4 import BeautifulSoup


def get_lp(url):

    page = urllib2.urlopen(url).read()

    soup = BeautifulSoup(page, 'lxml')

    litecoin_price = soup.find_all('span',class_='text-large2')

    for a in litecoin_price:
        return "${}".format(a.text)

print get_lp('https://coinmarketcap.com/currencies/litecoin/')
