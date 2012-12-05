from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from papers.items import PapersItem

class UsenixProceedingsSpider(CrawlSpider):
    name = 'usenix_proceedings'
    allowed_domains = ['www.usenix.org']
    start_urls = ['https://www.usenix.org/publications/proceedings?page=1']

    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths='//a[text()="Prev"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        tr = hxs.select('//tbody/tr')

        for row in tr:
            i = PapersItem()
            i['conference'] = row.select('td[1]/a/text()').extract()
            i['title'] = row.select('td[2]/a/text()').extract()
            i['author'] = row.select('td[3]/text()').extract()
            # i['affiliation']
            # i['fulltext'] = row.select().extract()
            # i['description'] = row.select().extract()
            items.append(i)

        return items
