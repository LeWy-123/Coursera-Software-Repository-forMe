import json
import urllib.request
import ssl

from IPython.core.oinspect import object_info

# Create an SSL context to ignore certificate verification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('URL: ')
json_file = urllib.request.urlopen(url, context=ctx).read()
print(f'Retrieving from {url}')
print(f'Retrieved {len(json_file)} characters')

myJson = json.loads(json_file)
print(f'Counts: {len(myJson['comments'])}')

print(myJson['comments'][0]['count'])
Z = 0

for X in myJson['comments']:
    Z += X['count']

print(Z)