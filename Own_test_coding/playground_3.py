import urllib.request
from bs4 import BeautifulSoup
import ssl
import json

print(f'The starting of the program...')
# this is a list comprehension uses dir() to return current name spaces, and it shows in this f-string filters out
# with a method of startswith()
print(f'Imported modules: {[i for i in dir() if i.startswith("__") == False]}\n')

# a plain certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(f'Certificate: {ctx}\nctx.check_hostname = {ctx.check_hostname:<3}\nctx.verify_mode = {ctx.verify_mode:<3}\n')

URL = input("Enter a URL: ")
if not URL:
    URL = 'https://realpython.com/python-f-strings/'
    print(f'URL: {URL}')


print('-' * 40)
request = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html, 'html.parser')
a = soup('a')
x = soup.prettify()

print(x)
print('-' * 40)
print('Links:')
n = 1
for i in a:
    try:
        if not i['href'].startswith('http'):
            X = '(Relative Link)'
        else:
            X = ''

        print(f'{n} {X} URL:', i['href'])
        n += 1
    except KeyError:
        continue

print('-' * 40)
print('application/json data:')
dirty_js = soup.find_all('script')

'''
print(dirty_js[0].__doc__,'\n', dirty_js[0])
print(dirty_js[0].text)
print(dir(dirty_js[0]))
print('getting type: ', dirty_js[0].get('type'))
'''

n = 1
jsons_list = []
for i in dirty_js:
    #print(f'debuting print: {i}')
    if i.get('type') == 'application/json' or i.get('type') == 'application/ld+json':
        #print(f'{n} type: {i.get("type")} content of it > {i.text}')
        try:
            js = json.loads(i.text)
            jsons_list.append(js)
        except:
            print('Could not decode JSON')
            print('-' * 40)
    else:
        continue
    n += 1

print(f'all json-s found: {len(jsons_list)}')
for i in jsons_list:
    print(f'{i}')

with open('last_run_log.json', 'w') as f:
    json.dump(jsons_list, f, indent=4)