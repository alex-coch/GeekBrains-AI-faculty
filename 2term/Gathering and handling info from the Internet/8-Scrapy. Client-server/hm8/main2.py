import scrapy
from csv import DictReader

class MySpider(scrapy.Spider):

    def start_requests(self):

        with open('addresses.csv') as rows:

            for row in DictReader(rows):

                name=row["Name"].replace(',','')
                email=row["Email"].replace(',','')

                link = 'http://www.example.com/search/?where='+row["Address"].replace(',','').replace(' ','+')

                yield Request(url = link, 
                        callback = self.parse, 
                        method = "GET", 
                        meta={'name':name, 'email':email}
                    )


    def parse(self,response):
        yield{
         'name': resposne.meta['name'],
         'email': respose.meta['email'],
         'address' FROM SCRAPING: 
         'city' FROM SCRAPING: 
        }