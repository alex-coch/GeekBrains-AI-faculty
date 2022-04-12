import scrapy
from read_files import read_csv, read_excel
base_url = 'https://stackoverflow.com/questions/tagged/{}'
class SoSpider(scrapy.Spider):
    name = 'so'
    def start_requests(self):
        for tag in read_excel():
            yield scrapy.Request(base_url.format(tag))
    def parse(self, response):
        questions = response.xpath('normalize-space(//*[@id="mainbar"]/div[4]/div/div[1]/text())').get()
        questions = questions.strip('questions')
        yield {
            'questions': questions,
            'url': response.url
        }
exit(1)


from pprint import pprint
import csv
from requests import get
import pandas as pd
url = 'https://data.gov.ru/opendata/7706562710-harakteristika/data-20200113T1400-structure-20200113T1400.csv'
data_frame = pd.read_csv(url, sep=',')
result = data_frame[data_frame['годы'] > 2015]
print(result)