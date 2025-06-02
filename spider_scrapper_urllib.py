# Importing the modules
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

from sympy.physics.units import current

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# assignments URL
URL = input('Enter URL: ')
# debug prints
def digging(URL, linkto = None):
    # the HTML loaded by urllib
    html = urlopen(URL, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup('a')
    counter = 1
    try:
        linkto = int(linkto)
    except ValueError:
        print(f'{linkto} is not an integer, quitting!')
        exit()

    for tag in anchors:
        print(f'{counter}) {tag.get('href', None)}')
        if linkto == counter:
            print(f'stopped at {counter}')
            return str(tag.get('href', None))
        counter += 1

# Main loop for digging
a = 1
current_url = URL
names = []
while True:
    if a == 1:
        print(f'Printing the list of links:')
    if current_url:
        # loading and printing the list
        print('-' * 50)
        html = urlopen(current_url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        anchors = soup('a')
        counter = 1
        for tag in anchors:
            print(f'{counter}) {tag.get('href', None)}')
            counter += 1
        print('-' * 50)

    name = re.findall('_by_(.*).html', current_url)
    names.append(name)
    print(f'Current URL: {current_url}, deepness: {a}, current name: {name[0]}')
    print(f'Names by order: ', end='')
    for nam in names:
        for nn in nam:
            print(f'{nn} > ', end=' ')
    print(f'\nWhat link you wanna follow? enter its number.')
    n = input('> ')
    current_url = digging(current_url, n)

    a += 1
    if a > 15: break