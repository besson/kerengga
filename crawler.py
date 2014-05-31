from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from kerengga.spiders.gpa_subcategory import GPASubcategorySpider

spider = GPASubcategorySpider(start_url='http://www.pontofrio.com.br/livros/Audiolivros/audiolivrosLiteraturaNacional/?Filtro=C484_C1376_C1443')
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run()
