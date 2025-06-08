import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# reading the URL
URL = input("Enter the URL: ")
if not URL.startswith("http"):
    URL = 'https://www.scrapethissite.com/pages/simple/'

HTML = urllib.request.urlopen(url=URL, context=ctx).read()

# Now pass it to BeautifulSoup
soup = BeautifulSoup(HTML, "html.parser")

# getting anchor tags from the HTML
a = soup('a')
dive = soup('div', attrs={'class': 'col-md-4 country'})
#print(f'Number of links: {len(a)}')
#print(soup.prettify())
main_element = soup.find_all('div', class_='col-md-4 country')
countries_names = soup.find_all('h3', class_='country-name')

full_data = {country.text.strip(): {"population": None, "capital": None, "Area (km2)": None} for country in countries_names}

countries = {}

print(f'Countries: {len(full_data)}')
for country_div in soup.find_all("div", class_="col-md-4 country"):
    country_name = country_div.find("h3", class_="country-name").text.strip()
    capital = country_div.find("span", class_="country-capital").text.strip()
    population = int(country_div.find("span", class_="country-population").text.strip())
    area = float(country_div.find("span", class_="country-area").text.strip())

    # Store extracted data in dictionary
    countries[country_name] = {
        "Capital": capital,
        "Population": population,
        "Area (km²)": area
    }

for country in countries:
    print(f'{country}:\n', countries[country]["Capital"], countries[country]["Population"], str(countries[country]["Area (km²)"])+' km²')
    print('-------------------')