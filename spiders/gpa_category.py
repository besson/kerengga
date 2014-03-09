 #!/usr/bin/env python

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from kerengga.items import Category

class GPACategorySpider(CrawlSpider):
    name = "gpa_category"
    allowed_domains = ["pontofrio.com.br", "casabahia.com.br"]
    start_urls = ["http://www.pontofrio.com.br"]

    def parse(self, response):
        sel = Selector(response)
        categories = sel.xpath('//li[contains(@class,"it-sbmn")]/a[contains(@href,"Filtro")]')

        items = []
        for category in categories:
            item = Category()
            item['url'] = category.xpath('@href').extract()[0]

            description = category.xpath('text()').extract()
            if (description):
              item['description'] = description[0]

            item['player_id'] = 4
            items.append(item)

        return items
