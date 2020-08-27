import scrapy


class CardItem(scrapy.Item):
    cardName = scrapy.Field()
    imgId = scrapy.Field()
    rare = scrapy.Field()
    enName=scrapy.Field()
    jpName=scrapy.Field()
    cardNumber=scrapy.Field()
    packageName=scrapy.Field()
