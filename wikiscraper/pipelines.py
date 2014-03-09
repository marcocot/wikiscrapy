from pyelasticsearch import ElasticSearch


class WikiscraperPipeline(object):
    def process_item(self, item, spider):
        return item


class ESPipeline(object):
    def __init__(self, *args, **kwargs):
        self.client = ElasticSearch('http://localhost:9200/')

    def process_item(self, item, spider):
        self.client.index('wiki', 'page', dict(item))
        return item