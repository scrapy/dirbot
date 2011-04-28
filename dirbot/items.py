from scrapy.item import Item, Field

class Website(Item):

    name = Field()
    url = Field()
    description = Field()

    def __str__(self):
        return "Website: name=%s url=%s" % (self['name'], self['url'])
