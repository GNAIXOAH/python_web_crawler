import scrapy
from ..items import QuotesItem

class QuotespiderSpider(scrapy.Spider):
    name = 'quotespider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    page_offset= 1

    def parse(self, response):
        item = QuotesItem()
        list_of_quotes = response.xpath('//div[@class="quote"]')
        for quote in list_of_quotes:
            content = quote.xpath('./span[@class = "text"]/text').get()
            author = quote.xpath('./span/small[@class = "author"]/text').get()
            tags = []
            tags_list = quote.xpath('./div[@class = "tags"]/a')
            for t in tags_list:
                tags.append(t.xpath('./text()').get())
            item['content'] = content
            item['author'] = author
            item['tags'] = tags
            yield item
        if self.page_offset < 10:
            self.page_offset += 1
            next_page = response.xpath('//nav/ul/li[@class = "next"]/a/@herf').get()
            if next_page:
                next_page_url = response.urljoin(next_page)
                yield scrapy.Request(next_page_url, callback=self.parse)















