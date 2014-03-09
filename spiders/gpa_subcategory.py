 #!/usr/bin/env python

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from kerengga.items import Category

class GPASubcategorySpider(CrawlSpider):
    name = "gpa_subcategory"
    allowed_domains = ["pontofrio.com.br", "casabahia.com.br"]

    def __init__(self, category=None, *args, **kwargs):
        super(GPASubcategorySpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url')]
        global parent_id
        parent_id = [kwargs.get('pid')]

    start_urls = ["http://www.pontofrio.com.br"]

    def parse(self, response):
        sel = Selector(response)
        subcategories = sel.xpath('//h3[contains(@class,"tit title2")]/a')

        items = []
        for subcategory in subcategories:
            item = Category()
            item['url'] = subcategory.xpath('@href').extract()[0]

            description = subcategory.xpath('text()').extract()
            if (description):
              item['description'] = description[0]

            item['player_id'] = 4
            item['parent_id'] = parent_id
            items.append(item)

        return items
