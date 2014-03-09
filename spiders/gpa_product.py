 #!/usr/bin/env python

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import Request
from kerengga.items import Product

class GPAProductSpider(CrawlSpider):
    name = "gpa_product"
    allowed_domains = ["pontofrio.com.br", "casabahia.com.br"]
    start_urls = ['http://www.pontofrio.com.br/tablets/Tablet/TabletAndroid/?Filtro=C2031_C2032_C2034&paginaAtual=1&numPorPagina=20']

    def parse(self, response):
        sel = Selector(response)
        products = sel.xpath('//a[contains(@href, "recsource=busca-int")]/@href')
        for product in products:
            yield Request(product.extract(), callback = self.parse_product)

    def parse_product(self, response):
        sel = Selector(response)
        product = Product()

        product['url'] = response.url
        product['name'] = sel.xpath('//h1/b/text()').extract()[0]
        product['ean'] =  sel.xpath('//h1/span/text()').extract()[1].split(" ")[3][:-1]
        product['price'] = sel.xpath('//i[contains(@class, "sale price")]/text()').extract()[0]

        return product

