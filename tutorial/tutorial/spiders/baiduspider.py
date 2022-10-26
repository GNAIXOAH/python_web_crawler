import scrapy


class BaiduspiderSpider(scrapy.Spider):
    name = 'baiduspider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        title = response.xpath('//html/head/title/text()').extract_first()
        print('baidu首页的title是：', title)