# Scrapy settings for wikiscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wikiscraper'

SPIDER_MODULES = ['wikiscraper.spiders']
NEWSPIDER_MODULE = 'wikiscraper.spiders'
LOG_LEVEL = 'DEBUG'

ITEM_PIPELINES = {
    'wikiscraper.pipelines.ESPipeline': 100,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wikiscraper (+http://www.yourdomain.com)'
