import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["www.cbc.ca"]
    start_urls = ["http://www.cbc.ca/"]



    def parse(self, response):
        # Card links xPath //a[contains (@class, "card")]
        for news_card in response.xpath('//a[contains (@class, "card")]'):
            headline = news_card.xpath(".//div/div/div/h3/text()").get()
            url = news_card.xpath(".//@href").get()

            meta={
                'title' : headline,
                'url' : url
            }
            
            if "www.cbc.ca" in url:
                yield scrapy.Request(
                    url=url,
                    callback=self.parse_article,
                    meta=meta
                )
            else:
                yield response.follow(
                    url=url,
                    callback=self.parse_article,
                    meta=meta
                )
    
    def parse_article(self, response):
        text = response.xpath('//div[@class="story"]/p/text()').getall()
        yield {
            'title' : response.request.meta['title'],
            'text': '\n'.join(text),
            'url' : response.request.meta['url']
        }