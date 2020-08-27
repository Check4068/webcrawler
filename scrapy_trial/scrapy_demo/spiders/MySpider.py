import scrapy
from scrapy_demo.CardItems import CardItem
from scrapy.http import Request
from selenium import webdriver
import numpy as np
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

Package = {1: ['ETCO-JP0', 'ETCO-JP00','紅蓮魔獣 ダ・イーザ', 80, 0],
           2: ['20PP-JP0', '20PP-JP00','緊急ダイヤ', 'Normal', 0],
           3: ['20TP-JP1', '20TP-JP10','抹殺の指名者', '20th-Secret', 0],
           4: ['20CP-JPF', '20CP-JPF0','魔封じの芳香', 10, 0],
           5: ['JF20-JP0', 'JF20-JP00','バージェストマ・ディノミスクス', 5, 0],
           6: ['LGB1-JP0', 'LGB1-JP00','幻影騎士団シェード・ブリガンダイン', 8, 0],
           7: ['LGB1-JPS', 'LGB1-JPS0','センサー万別',8, 0],
           8: ['SD37-JP0', 'SD37-JP00','無限泡影', 44, 0],
           9: ['SD37-JPP', 'SD37-JPP0','大捕り物', 5, 0],
           10: ['LVP3-JP0', 'LVP3-JP00','強欲で金満な壺', 100, 0],
           11: ['IGAS-JP0', 'IGAS-JP00','墓穴の指名者', 81, -1],
           12: ['SR09-JP0', 'SR09-JP00','閃刀起動-エンゲージ', 42, 0],
           13: ['19TP-JP4', '19TP-JP40','おろかな副葬', 16, 0],
           14: ['EP19-JP0', 'EP19-JP00','終末の騎士', 70, 0],
           15: ['LVDS-JPA', 'LVDS-JPA0','鬼ガエル', 10, 0],
           16: ['LVDS-JPB', 'LVDS-JPB0','増殖するG', 10, 0],
           17: ['20CP-JPT', '20CP-JPT0','魔界発現世行きデスガイド', 10, 0],
           18: ['DBMF-JP0', 'DBMF-JP00','スチーム・シンクロン', 45, 0],
           19: ['CHIM-JP0', 'CHIM-JP00','幽鬼うさぎ', 80, 0],
           20: ['19TP-JP3', '19TP-JP30','海亀壊獣ガメシエル', 16, 0],
           21: ['SD36-JP0', 'SD36-JP00', '浮幽さくら', 41, 0],
           22: ['SD36-JPP', 'SD36-JPP0', '灰流うらら', 5, 0],
           23: ['19SP-JP6', '1', '白棘鱏', 10, 0],
           24: ['DP22-JP0', 'DP22-JP00', '屋敷わらし', 56, -1],
           25: ['CP19-JP0', 'CP19-JP00', 'ダイナレスラー・パンクラトプス', 46, -1],
           26: ['YMAB-JP0', 'YMAB-JP00', '混源龍レヴィオニア', 1, 0],
           27: ['19PR-JP0', '19PR-JP00', 'サイバー・ドラゴン・ネクステア', 12, 0],
           28: ['RIRA-JP0', 'RIRA-JP00', '幻創龍ファンタズメイ', 80, 0],
           29: ['19TP-JP2', '19TP-JP20', '爆走軌道フライング・ペガサス', 16, 0],
           30: ['ST19-JP0', 'ST19-JP00', '儚無みずき', 45, 0],
           31: ['19SP-JP5', '19SP-JP50', 'カクリヨノチザクラ', 10, 0],
           32: ['SR08-JP0', 'SR08-JP00', '竜騎士ブラック・マジシャン・ガール', 32, 0],
           33: ['DBIC-JP0', 'DBIC-JP00', 'キメラテック・メガフリート・ドラゴン', 45, 0],
           34: ['20TH-JPC', '20TH-JPC0', '琰魔竜 レッド・デーモン・アビス', 100, -1],
           35: ['20CP-JPC', '20CP-JPC0', '深淵に潜む者', 10, 0],
           36: ['20CP-JPS', '20CP-JPS0', 'サイバー・ドラゴン・インフィニティ', 10, 0],
           37: ['DANE-JP0', 'DANE-JP00', '真竜皇V.F.D.', 80, 0],
           38: ['19TP-JP1', '19TP-JP10', '水晶機巧-ハリファイバー', 16, 0],
           39: ['19PP-JP0', '19PP-JP00', '閃刀姫-カガリ', 20, 0],
           40: ['JF19-JP0', 'JF19-JP00', 'サクリファイス・アニマ', 5, 0],
           41: ['SSD1-JP0', 'SSD1-JP00', '転生炎獣アルミラー', 21, 0],
           42: ['SSD2-JP0', 'SSD2-JP00', 'サンダー・ボルト', 21, 0],
           43: ['20TH-JPB', '20TH-JPB0', 'ハーピィの羽根帚', 36, 0],
           44: ['20TH-JPB', '20TH-JPBS', '死者蘇生', 6, 0],
           45: ['20TH-JPB', '20TH-JPBT', 'ミラクル・フュージョン', 6, 0],
           46: ['SD35-JP0', 'SD35-JP00', '超融合', 40, 0],
           47: ['SD35-JPP', 'SD35-JPP0', 'ドラゴン・目覚めの旋律', 5, 0],
           48: ['DMMD-JP0', 'DMMD-JP00', 'RUM-七皇の剣', 1, 0],
           49: ['LVP2-JP0', 'LVP2-JP00', '復活の福音', 100, 0],
           50: ['18SP-JP4', '18SP-JP40', 'ミレニアム・アイズ・サクリファイス', 10, 0],
           51: ['YCPC-JP0', 'YCPC-JP00', '屋敷わらし', 20, 0],
           52: ['DP21-JP0', 'DP21-JP00', '白棘鱏', 56, -1],
           53: ['18TP-JP4', '18TP-JP40', '18TP-JP401', 16, 0],
           54: ['RC03-JP0', 'RC03-JP00', 'RC03-JP001', 50, 0],}

Rare = ['Normal','Ultra''Ultimate','Secret','20th-Secret']

class MySpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = []





    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):

        start_urls = []

        for i in range(50,0,-1):

            start_urls.append("https://ygokamo.com/?s="+Package[i][2])
        for url in start_urls:
            yield Request(url, callback=self.parse)



    def parse(self, response):
        # 将我们得到的数据封装到一个 `MyspiderItem` 对象
        self.logger.info('Hi, this is an item page! %s', response.url)

        item = CardItem()
        k=[]


        #item["cardName"] = "card"
        #item["imgId"] = "1257564"
        #item["rare"] = "mormal"
        # 提取数据
        '''
        print(response.xpath('//a[@class="entry-card-wrap a-wrap border-element cf"]/@href').extract()[0])
        url1=[]
        url1.append(response.xpath('//a[@class="entry-card-wrap a-wrap border-element cf"]/@href').extract()[0])
        '''


        if (len(response.xpath('//strong/text()').extract()) == 0):
            print("???")
            print(response)
            print(response.xpath('//a[@class="entry-card-wrap a-wrap border-element cf" and (contains(@href,"cards"))]/@href').extract()[0])
            item['website']=response.xpath('//a[@class="entry-card-wrap a-wrap border-element cf" and (contains(@href,"cards"))]/@href').extract()[0]
            yield  Request(item['website'], callback=self.parse)

        else:

          s=response.xpath('//strong/text()').extract()
          for r in s:

           print('//strong[contains(text(),"' + r + '")]/parent::td/parent::tr/following-sibling::tr[position()<=5]/td[contains(text(),"円")]/text()')
           if (len(response.xpath('//strong[contains(text(),"' + r + '")]/parent::td/parent::tr/following-sibling::tr[position()<=5]/td[contains(text(),"円")]/text()').extract())!=0):
             a = len(response.xpath('//strong[contains(text(),"' + r + '")]/parent::td/parent::tr/following-sibling::tr[position()<=5]/td[contains(text(),"円")]/text()').extract())
             b=min(a,4)
             for p in range(0,b):
                k.append(int(response.xpath('//strong[contains(text(),"' + r + '")]/parent::td/parent::tr/following-sibling::tr[position()<=5]/td[contains(text(),"円")]/text()').extract()[p].strip("円")))
             print(k)
             item['price']=np.mean(k)
             item['pricelist']= str(k)
             k.clear()
             item['rare'] = r
             item['cardname'] = response.xpath('//meta[@property="og:title"]/@content').extract()[0]
             yield item
        print('gaoding')
        '''
        print(response.xpath('//strong[contains(text(),"Normal")]/parent::td/parent::tr/following-sibling::tr/td[contains(text(),"円")]/parent::tr/following-sibling::tr[1]/td[contains(text(),"円")]/parent::tr/preceding-sibling::tr[1]/td[1]/text()').extract())
        '''
        '''
        print(response.xpath('//td/parent::tr/preceding-sibling::tr[2]/strong[contains(text(),"Normal")]]/text()').extract())
        '''
        '''
        item["cardName"] = response.xpath('//span[contains(text(),"中文名称")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n","")
        item["enName"] = response.xpath('//span[contains(text(),"英文名称")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n", "")
        item["jpName"] = response.xpath('//span[contains(text(),"日文名称")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n", "")
        item["imgId"] = response.xpath('//span[contains(text(),"卡片密码")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n","")
        item["rare"] = response.xpath('//span[contains(text(),"稀有度")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n","")
        item["cardNumber"]=response.xpath('//span[contains(text(),"卡片编号")]/parent::td/following-sibling::td/text()').extract()[0].strip().replace("\n","")
        item["packageName"] = response.xpath('//td[@class="navigation-text"]/a[4]/text()').extract()[0]
        
        
        print(item["cardName"])
        print(item["enName"])
        print(item["jpName"])
        print(item["imgId"])
        print(item["rare"])
        '''

        # 将获取的数据交给pipelines



        '''
        for k in range(2,0,-1):
           for u in range(Package[k][3], Package[k][4],-1):

                url = "http://www.qi-wmcard.com/card/"+Package[k][2][:-1] + str(u)

            yield Request(url, callback=self.parse)
        '''


