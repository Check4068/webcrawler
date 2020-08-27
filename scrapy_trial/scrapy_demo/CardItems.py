import scrapy


class CardItem(scrapy.Item):
    price=scrapy.Field()
    pricelist = scrapy.Field()
    rare = scrapy.Field()
    website = scrapy.Field()
    cardname = scrapy.Field()

    '''
    
    imgId = scrapy.Field()
    
    enName=scrapy.Field()
    jpName=scrapy.Field()
    cardNumber=scrapy.Field()
    packageName=scrapy.Field()
    
    '''