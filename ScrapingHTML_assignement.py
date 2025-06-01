# Importing the modules
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://py4e-data.dr-chuck.net/comments_2223028.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
numbers = [int(span.text) for span in soup.find_all('span', class_='comments')]

print(f'SUM: {sum(numbers)}')
print(f'Count: {len(numbers)}')