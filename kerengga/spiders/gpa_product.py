 #!/usr/bin/env python

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from kerengga.items import Category
from scrapy.http import Request
from kerengga.items import Product

from django.utils.encoding import smart_str, smart_unicode

class GPAProductSpider(CrawlSpider):
    name = "gpa_product"
    allowed_domains = ["pontofrio.com.br", "casabahia.com.br"]

    def __init__(self, category=None, *args, **kwargs):
        super(GPAProductSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url')]

    def parse(self, response):
        sel = Selector(response)
        products = sel.xpath('//a[contains(@href, "recsource=busca-int")]/@href')
        for product in products:
            yield Request(product.extract(), callback = self.parse_product)

    def parse_product(self, response):
        sel = Selector(response)
        product = Product()

        product['url'] = response.url
        product['name'] = smart_str(sel.xpath('//h1/b/text()').extract()[0])
        product['ean'] =  sel.xpath('//h1/span/text()').extract()[1].split(" ")[3][:-1]
        product['price'] = sel.xpath('//i[contains(@class, "sale price")]/text()').extract()[0]

        return product

