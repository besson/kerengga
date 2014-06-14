# -*- coding: UTF-8 -*-

from scrapy.item import Item, Field

class Product(Item):
    url = Field()
    name = Field()
    ean = Field()
    price = Field()
    player_id = Field()
    category_id = Field()

class Category(Item):
    url = Field()
    description = Field()
    parent_id = Field()
    player_id = Field()