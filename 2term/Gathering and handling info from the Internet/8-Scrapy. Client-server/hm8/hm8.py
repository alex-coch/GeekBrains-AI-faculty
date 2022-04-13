class YellowPages(scrapy.Spider):
    name = 'yp'

    start_urls = [
           "https://www.yellowpages.com/search?search_terms=agent&geo_location_terms=Los%20Angeles%2C%20CA&page=1",
           ]

    def parse(self, response):
        agent_name = response.xpath("//a[@class='business-name']/span/text()").extract()
        phone_number = response.xpath("//div[@class='phones phone primary']/text()").extract()
        address = response.xpath("//div[@class='street-address']/text()").extract()
        locality = response.xpath("//div[@class='locality']/text()").extract()


        data = zip(agent_name, phone_number, address, locality)

        for item in data:
            info = {
                'page' : response.url,
                'Agent_name': item[0],
                'Phone_number': item[1],
                'address': item[2],
                'locality': item[3],
            }
            yield info