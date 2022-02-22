import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

response = requests.get('http://127.0.0.1:5000/')
dom = BS(response.text, 'html.parser')

# type(dom.find('a'))


tag_a = dom.find('a')
parent_a = tag_a.parent.parent

# parent_a = tag_a.parent.parent
# children_div = parent_a.findChildren(recursive=False)

tag_div =  dom.find('div', {'id': 'd2'})

tags_p = dom.find_all('p')

result = dom.select('p.red.paragraph')

p6 = dom.find(text='Шестой параграф')


pprint()