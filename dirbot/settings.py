# Scrapy settings for dirbot project

BOT_NAME = 'dirbot'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['dirbot.pipelines.FilterWordsPipeline']
