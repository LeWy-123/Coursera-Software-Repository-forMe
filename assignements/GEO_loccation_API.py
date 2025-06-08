import urllib.request, urllib.parse
import json, ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# API bridge
API_endpoint = 'http://py4e-data.dr-chuck.net/opengeo?'

print(f'Hello, welcome to GEO-Location API.py')
address = input('Enter address: ')

if not address:
    exit('Address cannot be empty!')

# clean up the address from new lines amd whitespace
address = address.strip()

# building the URL the q is the attribute comes after the '?'
URL = API_endpoint + urllib.parse.urlencode({'q': address})

print('Retrieving', URL)
uh = urllib.request.urlopen(URL, context=ctx)
data = uh.read().decode()
print(f'Data received: {len(data)} char long. {data[:20].replace('\n', ' ')} end of data.')

try:
    json_data = json.loads(data)
except:
    json_data = None

if not json_data:
    print('Data could not be parsed.')
    exit()

print(json.dumps(json_data, indent=4))

lat = json_data['features'][0]['properties']['lat']
lon = json_data['features'][0]['properties']['lon']
print('lat', lat, 'lon', lon)
location = json_data['features'][0]['properties']['formatted']
print(location)
print(f'plus_code: {json_data["features"][0]["properties"]["plus_code"]}')