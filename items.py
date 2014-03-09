# -*- coding: UTF-8 -*-

from scrapy.item import Item, Field

def encode(value):
  return value.encode('utf-8')

class Product(Item):
    url = Field()
    name = Field(serializer=encode)
    ean = Field()
    price = Field()
    player_id = Field()
    category_id = Field()

class Category(Item):
    url = Field()
    description = Field()
    parent_id = Field()
    player_id = Field()