from scrapy.item import Item, Field


class DirbotItem(Item):

    name = Field()
    description = Field()


class Website(DirbotItem):

    url = Field()

    def __str__(self):
        return "Website: name=%s url=%s" % (self.get('name'), self.get('url'))
