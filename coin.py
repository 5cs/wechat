from urllib import urlopen
from bs4 import BeautifulSoup
from bs4 import NavigableString
from top100 import COINS

# return a dict
# dict['name'] := coin's name
# dict['cap'] := market cap
# dict['price'] := price
# dict['vol'] := volume(24h)
# dict['cir_sup'] := circulating supply
# dict['change'] := change(24h)
def parse(coin):
    ret = dict()
    name = coin.find_all(attrs={"class", "currency-name"})
    if name != None:
        name = name[0].span.string.strip()

    cap = coin.find_all(attrs={"class", "market-cap"})
    if cap != None:
        cap = cap[0].string.strip()

    price = coin.find_all(attrs={'class', 'price'})
    if price != None:
        price = price[0].string.strip()

    vol = coin.find_all(attrs={'class', 'volume'})
    if vol != None:
        vol = vol[0].string.strip()

    sup = coin.find_all(attrs={'class', 'circulating-supply'})

    change = coin.find_all(attrs={'class', 'percent-24h'})
    if change != None:
        change = change[0].string.strip()

    ret['name'], ret['cap'], ret['price'], ret['vol'], ret['change'] = name, cap, price, vol, change
    return ret


def crypto_currency(coin):
    # url = 'https://coinmarketcap.com/all/views/all/'
    url = 'https://coinmarketcap.com/'
    content = urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.tbody
    
    result = []
    for child in table.children:
        if isinstance(child, NavigableString):
            continue
        else:
            result.append(parse(child))

    # dict to string
    s = ''
    coin = coin.strip().upper()
    if coin in COINS.split(','):
        for item in result:
            if coin in item['name'].decode('ascii'):
                s += 'coin: ' + item['name'] + '\n' + \
                    'price: ' + item['price'] + '\n' + \
                    'change(24h): ' + item['change']
                break
    else:
        for i in range(6):
            s += 'coin: ' + result[i]['name'] + '\n' + \
                'price: ' + result[i]['price'] + '\n' + \
                'change(24h): ' + result[i]['change'] + '\n' + '='*13 + '\n'

    return s

def main():
    crypto_currency()

if __name__ == '__main__':
    main()
