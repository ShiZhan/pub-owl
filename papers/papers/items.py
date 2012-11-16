# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PapersItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    author = Field()
    affiliation = Field()
    fulltext = Field()
    conference = Field()
    pass
