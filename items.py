# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerTaw01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    User = scrapy.Field()
    Comment = scrapy.Field()
    Time = scrapy.Field()
    pass
