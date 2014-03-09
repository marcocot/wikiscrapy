__author__ = 'marco'

from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from ..items import PageLoader, Page


class Wiki(BaseSpider):
    name = 'wiki'
    allowed_domains = ['it.wikipedia.org']
    start_urls = ['http://it.wikipedia.org/wiki/Speciale:PaginaCasuale']
    rules = [
        Rule(SgmlLinkExtractor(unique=True), callback="parse", follow=True),
    ]


    def parse(self, response):
        hxs = Selector(response)

        for link in hxs.xpath("//div[@id='mw-content-text']//a[starts-with(@href, \"/wiki/\")]/@href").extract():
            yield Request("http://it.wikipedia.org" + link, callback=self.parse)

        loader = PageLoader(item=Page(), response=response)
        loader.add_xpath('title', "//h1[@id='firstHeading']/span/text()")
        loader.add_xpath('intro', "//div[@id='mw-content-text']/p")
        loader.add_xpath('categories', "//div[@id='mw-normal-catlinks']//li//a/text()")
        loader.add_value('url', response.url)

        yield loader.load_item()