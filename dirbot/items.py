from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    description = Field()
    url = Field()

    def __str__(self):
        return "Website: name=%s url=%s" % (self.get('name'), self.get('url'))
