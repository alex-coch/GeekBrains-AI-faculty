from lxml import html
import requests
from datetime import datetime
from pymongo import MongoClient

    
news = []

headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }

keys = ('title', 'date', 'link')
date_format = '%Y-%m-%dT%H:%M:%S%z'


link_mail_ru = 'https://mail.ru/'

request = requests.get(link_mail_ru, headers=headers)
root = html.fromstring(request.text)

news_links = root.xpath('''(//div[@class =  "news-item o-media news-item_media news-item_main"]  |  
                            //div[@class =  "news-item__inner"])
                            /a[contains(@href, "news.mail.ru")]/@href''')
news_links = root.xpath('/html/body/main/div[2]/div[2]/div[3]/div[1]/ul/li/div/a/@href')
                        # '/html/body/main/div[2]/div[2]/div[3]/div[1]/ul/li[3]/div/a'
news_text = root.xpath('''(//div[@class =  "news-item o-media news-item_media news-item_main"]//h3  |  
                           //div[@class =  "news-item__inner"]/a[contains(@href, "news.mail.ru")])
                           /text()''')
news_text = root.xpath('/html/body/main/div[2]/div[2]/div[3]/div[1]/ul/li/div/a/text()')
for i in range(len(news_text)):
    news_text[i] = news_text[i].replace(u'\xa0', u' ')

news_links_temp = []
for item in news_links:
    item = item.split('/')
    news_links_temp.append('/'.join(item[0:5]))

news_links = news_links_temp
del(news_links_temp)

news_date = []

for item in news_links:
    request = requests.get(item, headers=headers)
    root = html.fromstring(request.text)
    date = root.xpath('//span[@class="note__text breadcrumbs__text js-ago"]/@datetime')
    news_date.extend(date)

for i in range(len(news_date)):
    news_date[i] = datetime.strptime(news_date[i], date_format)

for item in list(zip(news_text, news_date, news_links)):
    news_dict = {}
    for key, value in zip(keys, item):
        news_dict[key] = value

    news_dict['source'] = 'mail.ru'
    news.append(news_dict)
    
print(news)

mongodb = MongoClient('mongodb://192.168.1.11:27017/')
db = mongodb['news']
collection = db['news_db']
for item in news:
    collection.insert_one(item)
