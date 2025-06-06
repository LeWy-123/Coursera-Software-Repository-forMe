import urllib.request
import xml.etree.ElementTree as ET

# Asking for the XML file link from and online source
print('Welcome to XML Parsing, please enter a URL or press enter to proceed with a default XML file.')
URL = input("Enter the URL: ")

# If the link doesn't end with XML it will quit
if '.xml' not in URL.lower():
    print('Invalid URL, "must end with .xml". Please enter a valid URL.')
    exit()

# reading the URL, if the URL invalid or return error, the program quit
try:
    XML_data = urllib.request.urlopen(URL).read().decode('utf-8')
    print(f'XML loaded successfully. the file length is {len(XML_data)}')
except:
    print('Invalid URL! The URL you entered is invalid. Please enter a valid URL.', URL)
    exit()

# printing out the content based on request
print(f'Parsing XML...')
question = input('Would you like to print the contents of the XML file? (Y/N): ')
if question.upper() == 'Y':
    print(XML_data)

# building XML tree element
tree = ET.fromstring(XML_data)
# Searching for count in the file using XPath
stuff = tree.findall('.//count')
count = 0

# --------------------------- just test
# another way to access data inside a tag
oop = tree.findall('./comments/comment')
c = 0
for o in oop:
    c += 1

# ---------------------------- test end

for i in stuff:
    count += int(i.text)

print(f'Items: {len(stuff)}')
print(f'SUM: {count}')