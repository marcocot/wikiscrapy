from scrapy.item import Item, Field
from scrapy.utils.markup import remove_entities, replace_tags
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Join, MapCompose


class PageLoader(ItemLoader):
    title_out = TakeFirst()
    url_out = TakeFirst()

    intro_in = MapCompose(remove_entities, replace_tags)
    intro_out = Join()


class Page(Item):
    title = Field()
    intro = Field()
    categories = Field()
    url = Field()