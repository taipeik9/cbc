import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["www.cbc.ca"]
    start_urls = ["http://www.cbc.ca/"]

    def parse(self, response):
        pass
