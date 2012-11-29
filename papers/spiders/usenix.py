from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from papers.items import PapersItem
import json

class UsenixSpider(BaseSpider):
    name = 'usenix'
    allowed_domains = ['www.usenix.org']

    try:
        with open('usenix_urls.json', mode='r') as usenix_urls:
            urls = json.loads(usenix_urls.read())
            usenix_urls.close()
    except Exception, e:
        raise e

    start_urls = urls

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        nodes = hxs.select('//div[@id and @class="node node-paper node-teaser paper-type-0 clearfix"]')
        conference = hxs.select('/html/head/title/text()').extract()
        items = []

        for node in nodes:
            item = PapersItem()
            item['conference'] = conference
            item['title'] = node.select('h2/a/text()').extract()

            content = node.select('div[@class="content"]')
            item['author'] = content.select(
                'div[@class="field field-name-field-paper-people-text field-type-text-long field-label-hidden"]\
                /div[@class="field-items"]/div[@class="field-item even"]/p/text()'
                ).extract()
            item['affiliation'] = content.select(
                'div[@class="field field-name-field-paper-people-text field-type-text-long field-label-hidden"]\
                /div[@class="field-items"]/div[@class="field-item even"]/p/em/text()'
                ).extract()
            item['description'] = content.select(
                'div[@class="field field-name-field-paper-description-long field-type-text-long field-label-hidden"]\
                /p'
                ).extract()
            item['fulltext'] = content.select(
                'div[@class="field field-name-field-presentation-pdf field-type-file field-label-hidden"]\
                /div/div/span/a/attribute::href'
                ).extract()

            items.append(item)

        return items
