from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from papers.items import PapersItem

class UsenixSpider(BaseSpider):
    name = 'usenix'
    allowed_domains = ['www.usenix.org']
    start_urls = [
        'https://www.usenix.org/conference/osdi12/tech-schedule/osdi-12-program',
        'https://www.usenix.org/conference/nsdi12/tech-schedule/technical-sessions',
        'https://www.usenix.org/conference/atc12/tech-schedule/usenix-atc-12-technical-sessions',
        'https://www.usenix.org/conference/webapps12/tech-schedule/webapps-12-technical-sessions',
        'https://www.usenix.org/conference/hotstorage12/tech-schedule/workshop-program',
        'https://www.usenix.org/conference/mad12/tech-schedule/workshop-program'
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        nodes = hxs.select('//div[@id and @class=\"node node-paper node-teaser paper-type-0 clearfix\"]')
        items = []

        for node in nodes:
            item = PapersItem()
            item['title'] = node.select('h2/a/text()').extract()
            item['author'] = node.select('div/div[2]/div/div/p/text()').extract()
            item['affiliation'] = node.select('div/div/div/div/p/em/text()').extract()
            item['fulltext'] = node.select('div/div[3]/div/div/span/a/attribute::href').extract()
            item['conference'] = node.select('/html/head/title/text()').extract()
            items.append(item)

        return items
