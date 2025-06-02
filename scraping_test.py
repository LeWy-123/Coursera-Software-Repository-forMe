import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# opening and reading the link and saving the content onto html variable
hyperlink = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(hyperlink, context=ctx).read()

# defining an object to be a soup object
soup = BeautifulSoup(html, 'html.parser')

numbers = soup.find_all('span', attrs={'class': 'comments'})

print("Number of comments:", len(numbers))
print("Printing the values:", numbers[0].text)  # First number on the same line
n = int(numbers[0].text)        # this put the initial number as first number value
elements = []

for i in numbers[1:]:  # Start from the second item
    print(f'{i.text:>23}')  # Adjust spacing here if needed
    n += int(i.text)
    elements.append(i.text)

print('-' * 50)
print(f'Sum of the elements: {n}')
print(f'Average of the elements: {n / len(numbers)}')
print(f'Biggest number {max(elements)}')
print(f'Smallest number {min(elements)}')
print('-' * 50)